#!/usr/bin/env python3
"""Runs the step scripts of dependabot-reusable.yml with a fake gh.

Each step runs as GitHub runs it: bash --noprofile --norc -eo pipefail.
The fake gh is in bin/. It is first in PATH.

Usage: python3 tests/dependabot-reusable/run_tests.py [path/to/dependabot-reusable.yml]
Needs bash 4 or later, jq, and PyYAML.
"""
import os, shutil, subprocess, sys, tempfile, yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WF = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, ".github", "workflows", "dependabot-reusable.yml")
BIN = os.path.join(HERE, "bin")
PATH = f"{BIN}{os.pathsep}{os.environ.get('PATH', '/usr/bin:/bin')}"
BASH = shutil.which("bash", path=PATH)
if not BASH or not shutil.which("jq", path=PATH):
    sys.exit("bash and jq must be in PATH")
print(subprocess.run([BASH, "-c", 'echo "bash $BASH_VERSION"'], capture_output=True, text=True).stdout.strip())
print(f"workflow: {WF}\n")
wf = yaml.safe_load(open(WF))
LABEL_SCRIPT = wf["env"]["ADD_LABEL_SCRIPT"]

JOB_ENV = {
    "GH_REPO": "x2od/demo", "HAS_TOKEN": "false", "PR_URL": "https://github.com/x2od/demo/pull/7",
    "PR_NUMBER": "7", "HEAD_SHA": "abcdef1234567890", "EVENT_ACTION": "opened", "CREATE_LABELS": "true",
    "MERGED_BY": "github-actions[bot]",
}
passed = failed = 0


def step(job, name):
    for s in wf["jobs"][job]["steps"]:
        if s.get("name") == name:
            return s
    raise KeyError(name)


def run(job, name, env=None, stub=None):
    s = step(job, name)
    d = tempfile.mkdtemp()
    e = {"PATH": PATH,"GITHUB_STEP_SUMMARY": f"{d}/summary",
         "GITHUB_OUTPUT": f"{d}/output", "GH_LOG": f"{d}/gh.log", "ADD_LABEL_SCRIPT": LABEL_SCRIPT}
    e.update(JOB_ENV)
    e.update({k: str(v) for k, v in (s.get("env") or {}).items() if "${{" not in str(v)})
    e.update(env or {})
    e.update(stub or {})
    for f in ("summary", "output", "gh.log"):
        open(f"{d}/{f}", "w").close()
    p = subprocess.run([BASH, "--noprofile", "--norc", "-eo", "pipefail", "-c", s["run"]],
                       env=e, capture_output=True, text=True)
    out = dict(l.split("=", 1) for l in open(f"{d}/output").read().splitlines() if "=" in l)
    return {"code": p.returncode, "summary": open(f"{d}/summary").read(), "out": out,
            "gh": open(f"{d}/gh.log").read(), "stdout": p.stdout + p.stderr}


def check(label, cond, r=None):
    global passed, failed
    if cond:
        passed += 1
        print(f"  PASS  {label}")
    else:
        failed += 1
        print(f"  FAIL  {label}")
        if r:
            print("        code:", r["code"]); print("        summary:", r["summary"].replace("\n", "\n                 "))
            print("        gh:", r["gh"].replace("\n", "\n            ")); print("        stdout:", r["stdout"])


TITLE = "Replace the title scope with the package name"
print("Title")
cases = [
    ("deps-dev scope", "build(deps-dev): bump js-yaml from 4.3.0 to 4.3.2", "js-yaml", "", "build(js-yaml): bump js-yaml from 4.3.0 to 4.3.2"),
    ("deps scope", "chore(deps): bump axios from 1.0.0 to 1.1.0", "axios", "", "chore(axios): bump axios from 1.0.0 to 1.1.0"),
    ("no scope (prefix only)", "deps: bump axios from 1.0.0 to 1.1.0", "axios", "", "deps(axios): bump axios from 1.0.0 to 1.1.0"),
    ("breaking !", "build(deps)!: bump x from 1 to 2", "x", "", "build(x)!: bump x from 1 to 2"),
    ("group uses group name", "build(deps-dev): bump the dev-deps group with 3 updates", "a, b, c", "dev-deps", "build(dev-deps): bump the dev-deps group with 3 updates"),
    ("scoped package @x/y", "build(deps-dev): bump @x2od/prettier-config from 0.3.0 to 0.3.1", "@x2od/prettier-config", "", "build(@x2od/prettier-config): bump @x2od/prettier-config from 0.3.0 to 0.3.1"),
]
for label, title, names, group, expect in cases:
    r = run("update", TITLE, {"PACKAGE_NAMES": names, "DEPENDENCY_GROUP": group}, {"STUB_TITLE": title})
    check(label, r["code"] == 0 and f"-f title={expect}" in r["gh"] and f"New: `{expect}`" in r["summary"], r)

for label, title, names, msg in [
    ("custom scope kept", "build(npm): bump x from 1 to 2", "x", "is not a Dependabot default"),
    ("not conventional", "Bump x from 1 to 2", "x", "not in Conventional Commits form"),
    ("already correct", "build(x): bump x from 1 to 2", "x", "already correct"),
    ("no names", "build(deps): bump x", "", "has no package names"),
]:
    r = run("update", TITLE, {"PACKAGE_NAMES": names, "DEPENDENCY_GROUP": ""}, {"STUB_TITLE": title})
    check(label, r["code"] == 0 and "PATCH" not in r["gh"] and msg in r["summary"], r)

r = run("update", TITLE, {"PACKAGE_NAMES": "x", "DEPENDENCY_GROUP": ""}, {"STUB_TITLE": "build(deps): bump x", "STUB_PATCH_ERR": "HTTP 403: Resource not accessible"})
check("PATCH error does not fail the step", r["code"] == 0 and "Could not change the title" in r["summary"] and "::warning" in r["stdout"], r)
r = run("update", TITLE, {"PACKAGE_NAMES": "x"}, {"STUB_TITLE_ERR": "HTTP 500"})
check("title read error does not fail the step", r["code"] == 0 and "Could not read the title" in r["summary"], r)

print("Labels")
LBL = "Add the dependabot label"
r = run("update", LBL)
check("label exists, add ok", r["code"] == 0 and "Added the `dependabot` label" in r["summary"] and "-f name=" not in r["gh"], r)
r = run("update", LBL, stub={"STUB_DEPENDABOT_LABEL_MISSING": "1"})
check("label missing, create then add", r["code"] == 0 and "Created the `dependabot` label" in r["summary"] and "Added the" in r["summary"], r)
r = run("update", LBL, {"CREATE_LABELS": "false"}, {"STUB_DEPENDABOT_LABEL_MISSING": "1", "STUB_ADD_DEPENDABOT_ERR": "HTTP 422: Label does not exist"})
check("create-labels false, add fails silently", r["code"] == 0 and "-f name=" not in r["gh"] and "Could not add the `dependabot` label" in r["summary"] and "::warning" in r["stdout"], r)
r = run("update", LBL, stub={"STUB_DEPENDABOT_LABEL_MISSING": "1", "STUB_CREATE_ERR": "HTTP 403: Resource not accessible by integration", "STUB_ADD_DEPENDABOT_ERR": "HTTP 422\nmultiline"})
check("create fails, add fails, step still ok", r["code"] == 0 and "Could not create" in r["summary"] and "Could not add" in r["summary"] and "multiline" in r["summary"], r)

print("Decide")
DEC = "Decide to approve and merge"
base = {"DEPENDENCY_TYPE": "direct:development", "UPDATE_TYPE": "version-update:semver-patch", "GHSA_ID": "", "ALERT_OUTCOME": "",
        "DEPENDENCY_TYPES": "direct:production,direct:development,indirect", "MERGE_METHOD": "squash", "MERGE_MODE": "auto", "WAIT_TIMEOUT_MINUTES": "30",
        **{f"{a}_{l}": "false" for a in ("APPROVE", "MERGE") for l in ("MAJOR", "MINOR", "PATCH", "SECURITY")}}


def dec(**kw):
    return run("update", DEC, {**base, **kw})


r = dec(APPROVE_PATCH="true", MERGE_PATCH="true")
check("patch approve+merge", r["code"] == 0 and r["out"] == {"approve": "true", "merge": "true", "level": "patch"}, r)
r = dec(APPROVE_PATCH="true", MERGE_MINOR="true")
check("patch approve only", r["out"]["approve"] == "true" and r["out"]["merge"] == "false" and "`automerge-patch` is `false`" in r["summary"], r)
r = dec(UPDATE_TYPE="version-update:semver-major", APPROVE_PATCH="true", MERGE_PATCH="true")
check("major not allowed", r["out"]["approve"] == "false" and r["out"]["merge"] == "false", r)
r = dec(MERGE_MINOR="true", UPDATE_TYPE="version-update:semver-minor")
check("merge without approval warns", r["out"]["merge"] == "true" and "Merge without approval" in r["summary"], r)
r = dec(APPROVE_PATCH="true", MERGE_PATCH="true", DEPENDENCY_TYPES=" direct:production , indirect ")
check("type not in list (with spaces)", r["out"]["approve"] == "false" and "is not in `dependency-types`" in r["summary"], r)
r = dec(APPROVE_PATCH="true", DEPENDENCY_TYPES=" direct:production , direct:development ")
check("type in list (with spaces)", r["out"]["approve"] == "true", r)
r = dec(APPROVE_PATCH="true", EVENT_ACTION="edited")
check("edited event never approves", r["out"]["approve"] == "false" and "`edited` event" in r["summary"], r)
r = dec(APPROVE_PATCH="true", UPDATE_TYPE="")
check("non-semver skipped", r["out"]["approve"] == "false" and "not a semver" in r["summary"], r)
r = dec(UPDATE_TYPE="version-update:semver-major", GHSA_ID="GHSA-xxxx", APPROVE_SECURITY="true", MERGE_SECURITY="true", HAS_TOKEN="true", ALERT_OUTCOME="success")
check("security major approve+merge", r["out"]["approve"] == "true" and r["out"]["merge"] == "true" and "GHSA-xxxx" in r["summary"], r)
r = dec(UPDATE_TYPE="", GHSA_ID="GHSA-xxxx", APPROVE_SECURITY="true", HAS_TOKEN="true", ALERT_OUTCOME="success")
check("security non-semver approve", r["out"]["approve"] == "true" and r["out"]["merge"] == "false", r)
r = dec(APPROVE_SECURITY="true", HAS_TOKEN="false")
check("security without token notes it", "needs the `token` secret" in r["summary"], r)
r = dec(APPROVE_SECURITY="true", HAS_TOKEN="true", ALERT_OUTCOME="failure")
check("security lookup failed notes it", "lookup failed" in r["summary"], r)
r = dec(MERGE_METHOD="fast-forward")
check("bad merge-method fails", r["code"] == 1 and "::error" in r["stdout"], r)
r = dec(MERGE_MODE="later")
check("bad merge-mode fails", r["code"] == 1 and "`merge-mode`" in r["summary"], r)
for bad in ("0", "51", "abc", "2.5"):
    r = dec(WAIT_TIMEOUT_MINUTES=bad)
    check(f"bad wait-timeout-minutes {bad} fails", r["code"] == 1 and "`wait-timeout-minutes`" in r["summary"], r)
r = dec(WAIT_TIMEOUT_MINUTES="50", MERGE_MODE="wait", APPROVE_PATCH="true")
check("wait-timeout 50 + wait mode ok", r["code"] == 0 and r["out"]["approve"] == "true", r)

print("Approve")
APP = "Approve the PR"
r = run("update", APP, {"TOKEN_USER": "github-actions[bot]", "LEVEL": "patch"}, {"STUB_REVIEWS": ""})
check("approves with commit id", r["code"] == 0 and "commit_id=abcdef1234567890" in r["gh"] and "Approved the PR at commit `abcdef1`" in r["summary"], r)
r = run("update", APP, {"TOKEN_USER": "github-actions[bot]", "LEVEL": "patch"}, {"STUB_REVIEWS": "COMMENTED\nAPPROVED\n"})
check("already approved skips", r["code"] == 0 and "-X POST" not in r["gh"] and "already approved" in r["summary"], r)
r = run("update", APP, {"TOKEN_USER": "github-actions[bot]", "LEVEL": "patch"}, {"STUB_REVIEWS": "APPROVED\nDISMISSED\n"})
check("dismissed approval re-approves", "-X POST" in r["gh"], r)
r = run("update", APP, {"TOKEN_USER": "github-actions[bot]", "LEVEL": "patch"}, {"STUB_REVIEWS_ERR": "HTTP 500"})
check("reviews read error still approves (pipefail safe)", r["code"] == 0 and "-X POST" in r["gh"], r)
r = run("update", APP, {"TOKEN_USER": "", "LEVEL": ""}, {})
check("unknown token user approves", r["code"] == 0 and "reviews --jq" not in r["gh"] and "-X POST" in r["gh"], r)
r = run("update", APP, {"TOKEN_USER": "github-actions[bot]", "LEVEL": "patch"}, {"STUB_APPROVE_ERR": "HTTP 422: GitHub Actions is not permitted to approve pull requests."})
check("approve error fails the job with hints", r["code"] == 1 and "Allow GitHub Actions to create and approve" in r["summary"], r)

print("Merge")
MRG = "Merge the PR"
M = {"MERGE_METHOD": "squash", "MERGE_MODE": "auto", "WAIT_TIMEOUT_MINUTES": "30", "CALLER_WORKFLOW": "Dependabot update",
     "POLL_SECONDS": "0", "NO_CHECKS_GRACE_SECONDS": "0"}
def mrg(env=None, stub=None):
    return run("update", MRG, {**M, **(env or {})}, stub)
# auto mode
r = mrg(stub={"STUB_STATUS": "OPEN false", "STUB_STATE_AFTER": "OPEN"})
check("auto: auto-merge on, GITHUB_TOKEN note", r["code"] == 0 and "--auto --squash --match-head-commit abcdef1234567890" in r["gh"] and r["out"]["merged-now"] == "false" and "will not be added" in r["summary"], r)
r = mrg({"MERGE_METHOD": "rebase", "HAS_TOKEN": "true"}, {"STUB_STATE_AFTER": "OPEN"})
check("auto: with PAT, no note", r["code"] == 0 and "--rebase" in r["gh"] and "will not be added" not in r["summary"], r)
r = mrg(stub={"STUB_STATE_AFTER": "MERGED"})
check("auto: immediate merge sets merged-now", r["out"].get("merged-now") == "true" and "Merged the PR" in r["summary"], r)
r = mrg(stub={"STUB_STATUS": "OPEN true"})
check("auto-merge already on skips", r["code"] == 0 and "pr merge" not in r["gh"] and "already on" in r["summary"], r)
r = mrg(stub={"STUB_STATUS": "CLOSED false"})
check("closed PR skips", r["code"] == 0 and "pr merge" not in r["gh"], r)
r = mrg(stub={"STUB_MERGE_ERR": "GraphQL: Merge method squash is not allowed"})
check("auto: other merge error fails with hints", r["code"] == 1 and "merges are allowed" in r["summary"], r)
# auto falls back to wait
ok_checks = '[{"name":"lint","workflow":"PR Validation","bucket":"pass"},{"name":"production / Title, label, approve, and merge","workflow":"Dependabot update","bucket":"pending"}]'
r = mrg(stub={"STUB_ALLOW": "false", "STUB_CHECKS": ok_checks})
check("auto + setting off -> wait -> merge", r["code"] == 0 and "does not allow auto-merge" in r["summary"] and "--auto" not in r["gh"]
      and "gh pr merge https://github.com/x2od/demo/pull/7 --squash --match-head-commit" in r["gh"] and r["out"]["merged-now"] == "true", r)
r = mrg(stub={"STUB_ALLOW": "unknown", "STUB_AUTO_MERGE_ERR": "GraphQL: Auto merge is not allowed for this repository (enablePullRequestAutoMerge)", "STUB_CHECKS": ok_checks})
check("auto + setting unreadable + auto-merge error -> wait -> merge", r["code"] == 0 and "Auto-merge is not available" in r["summary"] and r["out"]["merged-now"] == "true", r)
r = mrg(stub={"STUB_ALLOW_ERR": "HTTP 403", "STUB_AUTO_MERGE_ERR": "Pull request is in unstable status"})
check("auto + setting unreadable + other error -> fail", r["code"] == 1, r)
# wait mode
W = {"MERGE_MODE": "wait"}
r = mrg(W, {"STUB_CHECKS": ok_checks})
check("wait: own pending check ignored, merges", r["code"] == 0 and "All 1 other checks passed" in r["summary"] and "allow_auto_merge" not in r["gh"] and r["out"]["merged-now"] == "true", r)
r = mrg({**W, "NO_CHECKS_GRACE_SECONDS": "100"}, {"STUB_CHECKS_1": "", "STUB_CHECKS_2": '[{"name":"lint","workflow":"CI","bucket":"pending"}]',
            "STUB_CHECKS_3": '[{"name":"lint","workflow":"CI","bucket":"pass"},{"name":"test","workflow":"CI","bucket":"skipping"}]', "STUB_CHECKS_EXIT": "8"})
check("wait: polls (no checks yet, pending, pass) then merges; exit 8 ignored", r["code"] == 0 and r["gh"].count("pr checks") == 3 and "All 2 other checks" in r["summary"] and r["out"]["merged-now"] == "true", r)
r = mrg(W, {"STUB_CHECKS": '[{"name":"lint","workflow":"CI","bucket":"fail"},{"name":"test","workflow":"CI","bucket":"cancel"},{"name":"x","workflow":"CI","bucket":"pending"}]'})
check("wait: failed check -> no merge, step ok", r["code"] == 0 and "pr merge" not in r["gh"] and "`lint, test`" in r["summary"] and "::warning" in r["stdout"], r)
r = mrg(W, {"STUB_CHECKS": '[{"name":"lint","workflow":"Dependabot update","bucket":"fail"}]'})
check("wait: only own-workflow checks -> treated as no checks -> merge", r["code"] == 0 and "No other checks started" in r["summary"] and r["out"]["merged-now"] == "true", r)
r = mrg(W, {"STUB_CHECKS_EXIT": "1"})
check("wait: no checks at all (gh exit 1) -> merge after grace", r["code"] == 0 and "No other checks started" in r["summary"], r)
r = mrg(W, {"STUB_HEAD": "9999999aaaa OPEN", "STUB_CHECKS": ok_checks})
check("wait: new head commit -> no merge", r["code"] == 0 and "pr merge" not in r["gh"] and "A new commit (`9999999`)" in r["summary"], r)
r = mrg(W, {"STUB_HEAD": "abcdef1234567890 MERGED"})
check("wait: PR merged by someone during wait -> stop", r["code"] == 0 and "pr merge" not in r["gh"] and "became `MERGED`" in r["summary"], r)
r = mrg({**W, "WAIT_TIMEOUT_MINUTES": "0", "NO_CHECKS_GRACE_SECONDS": "100"}, {"STUB_CHECKS": '[{"name":"lint","workflow":"CI","bucket":"pending"}]'})
check("wait: timeout -> no merge, step ok", r["code"] == 0 and "pr merge" not in r["gh"] and "did not finish in 0 minutes" in r["summary"], r)
r = mrg(W, {"STUB_CHECKS": ok_checks, "STUB_MERGE_ERR": "Pull request is not mergeable"})
check("wait: final merge error fails with hints", r["code"] == 1 and "::error" in r["stdout"], r)
r = mrg(W, {"STUB_CHECKS": "not json"})
check("wait: bad JSON treated as no checks", r["code"] == 0 and "No other checks started" in r["summary"], r)
# retry after "Base branch was modified"
BASE = "GraphQL: Base branch was modified. Review and try the merge again. (mergePullRequest)"
R0 = {"MERGE_RETRY_SECONDS": "0"}
r = mrg({**R0, "MERGE_MODE": "now"}, {"STUB_MERGE_FAIL_TIMES": "2", "STUB_MERGE_FAIL_MSG": BASE})
check("retry: now mode merges on attempt 3", r["code"] == 0 and r["gh"].count("pr merge") == 3 and "attempt 3" in r["summary"] and "::notice" in r["stdout"] and r["out"]["merged-now"] == "true", r)
r = mrg({**R0, "MERGE_MODE": "now"}, {"STUB_MERGE_FAIL_TIMES": "9", "STUB_MERGE_FAIL_MSG": BASE})
check("retry: gives up after 4 attempts with the real error", r["code"] == 1 and r["gh"].count("pr merge") == 4 and "Base branch was modified" in r["summary"] and "Retry" not in r["summary"], r)
r = mrg({**R0, "MERGE_MODE": "now"}, {"STUB_MERGE_FAIL_TIMES": "9", "STUB_MERGE_FAIL_MSG": "Pull request is not mergeable"})
check("retry: other errors fail at once", r["code"] == 1 and r["gh"].count("pr merge") == 1, r)
r = mrg({**R0, "MERGE_MODE": "wait"}, {"STUB_CHECKS": ok_checks, "STUB_MERGE_FAIL_TIMES": "1", "STUB_MERGE_FAIL_MSG": BASE})
check("retry: wait mode merges on attempt 2", r["code"] == 0 and r["gh"].count("pr merge") == 2 and r["out"]["merged-now"] == "true", r)
r = mrg({**R0}, {"STUB_MERGE_FAIL_TIMES": "1", "STUB_MERGE_FAIL_MSG": BASE, "STUB_STATE_AFTER": "OPEN"})
check("retry: auto mode turns on auto-merge on attempt 2", r["code"] == 0 and r["gh"].count("--auto") == 2 and "Turned on auto-merge" in r["summary"], r)
r = mrg({**R0}, {"STUB_ALLOW": "unknown", "STUB_MERGE_FAIL_TIMES": "9", "STUB_MERGE_FAIL_MSG": "GraphQL: Auto merge is not allowed for this repository", "STUB_CHECKS": ok_checks})
check("retry: auto-merge error is not retried; job moves to wait", r["gh"].count("--auto") == 1 and "Auto-merge is not available" in r["summary"], r)

# now mode
r = mrg({"MERGE_MODE": "now"})
check("now: merges at once without --auto or checks", r["code"] == 0 and "--auto" not in r["gh"] and "pr checks" not in r["gh"] and r["out"]["merged-now"] == "true", r)

print("After-merge labels in the update job")
r = run("update", "Add the dependabot label after the merge")
check("header + dependabot label", r["code"] == 0 and "Labels after the merge" in r["summary"] and "Added the `dependabot`" in r["summary"], r)
r = run("update", "Add the auto-merged label after the merge", stub={"STUB_ADD_AUTOMERGED_ERR": "HTTP 403"})
check("auto-merged label error is silent", r["code"] == 0 and "Could not add the `auto-merged`" in r["summary"], r)

print("Closed job")
CHK = "Check that this workflow merged the PR"
r = run("labels-after-merge", CHK, {"TOKEN_USER": "dschach", "MERGED_BY": "dschach"}, {"STUB_LABELS": "dependencies\n", "STUB_EVENTS": "auto_squash_enabled dschach\n"})
check("PAT auto-merge -> auto=true", r["out"]["auto"] == "true", r)
r = run("labels-after-merge", CHK, {"TOKEN_USER": "dschach", "MERGED_BY": "dschach"}, {"STUB_LABELS": "", "STUB_EVENTS": "auto_squash_enabled dschach\nauto_merge_disabled dschach\n"})
check("auto-merge disabled then manual merge -> false", r["out"]["auto"] == "false" and "not with auto-merge" in r["summary"], r)
r = run("labels-after-merge", CHK, {"TOKEN_USER": "dschach", "MERGED_BY": "dschach"}, {"STUB_LABELS": "", "STUB_EVENTS": ""})
check("manual merge by PAT owner -> false", r["out"]["auto"] == "false", r)
r = run("labels-after-merge", CHK, {"TOKEN_USER": "github-actions[bot]", "MERGED_BY": "dschach"}, {})
check("merged by a person -> false", r["out"]["auto"] == "false" and "merged the PR, not the workflow" in r["summary"], r)
r = run("labels-after-merge", CHK, {"TOKEN_USER": "dschach", "MERGED_BY": "dschach"}, {"STUB_LABELS": "dependabot\nauto-merged\n"})
check("already labeled -> nothing to do", r["out"]["auto"] == "false" and "already has" in r["summary"], r)
r = run("labels-after-merge", CHK, {"TOKEN_USER": "", "MERGED_BY": "dschach"}, {})
check("unknown token user -> false with hint", r["out"]["auto"] == "false" and "token-user" in r["summary"], r)

print("Token user")
TU = "Find the token user"
r = run("update", TU, {"TOKEN_USER_INPUT": "", "HAS_TOKEN": "false"})
check("GITHUB_TOKEN -> github-actions[bot]", r["out"]["login"] == "github-actions[bot]", r)
r = run("update", TU, {"TOKEN_USER_INPUT": "", "HAS_TOKEN": "true"}, {"STUB_USER": "dschach"})
check("PAT -> api user", r["out"]["login"] == "dschach", r)
r = run("update", TU, {"TOKEN_USER_INPUT": "", "HAS_TOKEN": "true"}, {"STUB_USER_ERR": "HTTP 403"})
check("PAT api user fails -> empty + warning", r["code"] == 0 and r["out"]["login"] == "" and "::warning" in r["stdout"], r)
r = run("update", TU, {"TOKEN_USER_INPUT": "my-bot", "HAS_TOKEN": "true"})
check("input wins", r["out"]["login"] == "my-bot" and r["gh"] == "", r)
r = run("labels-after-merge", TU, {"TOKEN_USER_INPUT": "", "HAS_TOKEN": "true"}, {"STUB_USER_ERR": "HTTP 403"})
check("closed job: api user fails -> empty", r["code"] == 0 and r["out"]["login"] == "", r)

print("Summary header")
r = run("update", "Write the summary header", {"DEPENDENCY_NAMES": "a, b", "DEPENDENCY_GROUP": "", "DEPENDENCY_TYPE": "direct:production",
                                              "UPDATE_TYPE": "", "PREVIOUS_VERSION": "", "NEW_VERSION": "", "ECOSYSTEM": "npm", "TOKEN_USER": "x"})
check("header with empty optional rows", r["code"] == 0 and "| Group" not in r["summary"] and "not semver" in r["summary"] and "GITHUB_TOKEN" in r["summary"], r)

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
