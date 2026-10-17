# x2od shared configuration

This repository holds the configuration that other x2od and dschach repositories use. This section describes each shared item and how to use it.

## Shared items

| Item                                                                                           | How another repository uses it                                                                 | Who can use it                                                       |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [Dependabot reusable workflow](#dependabot-reusable-workflow)                                  | A short workflow file with `uses: x2od/.github/.github/workflows/dependabot-reusable.yml@main` | Any repository. This repository is public.                           |
| [Renovate shared configuration](#renovate-shared-configuration)                                | `"extends": ["github>x2od/.github:renovate.json5"]` in its Renovate file                       | Any repository that runs Renovate                                    |
| [Workflow templates](#workflow-templates)                                                      | **Actions > New workflow**, in the section for the x2od organization                           | Repositories in the x2od organization only                           |
| [Community health files and issue templates](#community-health-files-and-organization-profile) | Nothing. GitHub uses them automatically.                                                       | Repositories in the x2od organization that have no file of their own |
| [Organization profile](#community-health-files-and-organization-profile)                       | Nothing. GitHub shows it on the organization page.                                             | Visitors to [github.com/x2od](https://github.com/x2od)               |

## Dependabot reusable workflow

The reusable workflow does 4 tasks for each Dependabot pull request:

1. It replaces the title scope with the package name (or the group name), to match the Renovate title style. For example, `build(deps-dev): bump js-yaml from 4.3.0 to 4.3.2` becomes `build(js-yaml): bump js-yaml from 4.3.0 to 4.3.2`. It replaces only a missing scope, `deps`, or `deps-dev`. It keeps all other scopes.
2. It adds the `dependabot` label.
3. It approves and merges the pull request. The inputs set this for each update level (major, minor, patch), for security updates, and for each dependency type.
4. After a successful merge, it adds the `dependabot` label and the `auto-merged` label, in 2 separate steps.

Each step writes its result to the job summary of the run. An error in a title step or a label step does not fail the run. An error in the approval or the merge fails the run.

### Files

| Type                         | File                                                                                                                                           |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Reusable workflow            | [`.github/workflows/dependabot-reusable.yml`](.github/workflows/dependabot-reusable.yml)                                                       |
| Workflow template (caller)   | [`workflow-templates/dependabot-approve-and-auto-merge.yml`](workflow-templates/dependabot-approve-and-auto-merge.yml)                         |
| Workflow template properties | [`workflow-templates/dependabot-approve-and-auto-merge.properties.json`](workflow-templates/dependabot-approve-and-auto-merge.properties.json) |
| Caller for this repository   | [`.github/workflows/dependabot-approve-and-auto-merge.yml`](.github/workflows/dependabot-approve-and-auto-merge.yml)                           |

The comments at the top of the reusable workflow give the full details. This README gives a summary.

### How to call the workflow

Add this file to `.github/workflows/` in the calling repository. Change the inputs as necessary.

```yaml
name: Dependabot update

on:
  pull_request_target:
    types: [opened, reopened, synchronize, edited, closed]

permissions: {}

jobs:
  dependabot:
    if: github.event.pull_request.user.login == 'dependabot[bot]'
    permissions:
      contents: write # merge the PR
      pull-requests: write # edit the title, approve, turn on auto-merge
      issues: write # create labels and add them to the PR
    uses: x2od/.github/.github/workflows/dependabot-reusable.yml@main
    with:
      autoapprove-minor: true
      autoapprove-patch: true
      automerge-minor: true
      automerge-patch: true
    secrets:
      token: ${{ secrets.DEPENDABOT_TOKEN_X2OD }} # optional
```

Follow these rules in the calling file:

- Use the `pull_request_target` event, not `pull_request`. On `pull_request`, Dependabot runs get a read-only `GITHUB_TOKEN`. On `pull_request_target`, the `GITHUB_TOKEN` can write. The reusable workflow never checks out or runs code from the pull request, so `pull_request_target` is safe here.
- Include all 5 event types. The `closed` type is necessary for task 4.
- Give the calling job all 3 permissions. A called workflow cannot get more permissions than its caller. If 1 permission is missing, GitHub does not start the run.
- Do not use `secrets: inherit`. Pass only the `token` secret.

### What runs, and when

The workflow has 2 jobs.

**Job `update`** runs on the `opened`, `reopened`, `synchronize`, and `edited` events. It runs only when the pull request author and the event actor are both `dependabot[bot]`. Thus, it does not approve a commit that a person pushed to a Dependabot branch.

| Step                        | What it does                                                                                                                                                                | On error                              |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| Fetch Dependabot metadata   | Reads the package names, the update type, and the dependency type. If a PAT is given and a security input is `true`, it also looks up the Dependabot security alert.        | Fails the job                         |
| Write the summary header    | Writes a table of the pull request details to the job summary.                                                                                                              | Fails the job                         |
| Replace the title scope     | Changes the title scope to the package name or the group name.                                                                                                              | Writes to the summary, then continues |
| Add the `dependabot` label  | Creates the label if it does not exist, then adds it.                                                                                                                       | Writes to the summary, then continues |
| Decide to approve and merge | Compares the event, the dependency type, the update level, and the security alert to the inputs. Approval and merge happen only on `opened`, `reopened`, and `synchronize`. | Fails the job on a bad input value    |
| Approve the PR              | Approves the head commit. It skips the approval if the token user already approved.                                                                                         | Fails the job                         |
| Merge the PR                | Merges as `merge-mode` sets (see below).                                                                                                                                    | Fails the job                         |
| Labels after the merge      | If this job merged the pull request, it adds the `dependabot` label and the `auto-merged` label.                                                                            | Writes to the summary, then continues |

The 3 merge modes:

| `merge-mode`     | What happens                                                                                                                                                                                                                                         |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auto` (default) | The job uses GitHub auto-merge if the repository allows it. GitHub merges after the required checks and reviews pass. If the repository does not allow auto-merge (for example, a private repository on a free plan), the job uses `wait`.           |
| `wait`           | The job waits for all checks, except the checks of this workflow, and then merges. A failed check, a new commit, or the time limit (`wait-timeout-minutes`) stops the merge. The pull request then stays open. The runner is busy for the full wait. |
| `now`            | The job merges at once, without a wait.                                                                                                                                                                                                              |

**Job `labels-after-merge`** runs on the `closed` event, only for a merged Dependabot pull request. It checks that the token user turned on auto-merge and that GitHub merged the pull request. Then it adds the `dependabot` label and the `auto-merged` label, in 2 steps. A label error writes to the summary and the run continues.

> [!IMPORTANT]
> GitHub does not start a new workflow run for a merge done with the `GITHUB_TOKEN`. So without the `token` secret, the `labels-after-merge` job does not run after an auto-merge. When the `update` job does the merge itself (`wait`, `now`, or a pull request that can merge at once), it adds the labels in the same job.

When a repository calls the workflow more than 1 time, only the call with `rename-title: true` edits the title and adds the labels.

### Inputs

All inputs are optional.

| Input                  | Type    | Default                                         | Description                                                                                                                                                                                                                   |
| ---------------------- | ------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `autoapprove-major`    | boolean | `false`                                         | Approve major updates.                                                                                                                                                                                                        |
| `autoapprove-minor`    | boolean | `false`                                         | Approve minor updates.                                                                                                                                                                                                        |
| `autoapprove-patch`    | boolean | `false`                                         | Approve patch updates.                                                                                                                                                                                                        |
| `automerge-major`      | boolean | `false`                                         | Turn on auto-merge for major updates.                                                                                                                                                                                         |
| `automerge-minor`      | boolean | `false`                                         | Turn on auto-merge for minor updates.                                                                                                                                                                                         |
| `automerge-patch`      | boolean | `false`                                         | Turn on auto-merge for patch updates.                                                                                                                                                                                         |
| `autoapprove-security` | boolean | `false`                                         | Approve updates that fix a Dependabot security alert, at all update levels. Needs the "token" secret with "Dependabot alerts: Read-only".                                                                                     |
| `automerge-security`   | boolean | `false`                                         | Turn on auto-merge for updates that fix a Dependabot security alert, at all update levels. Needs the "token" secret with "Dependabot alerts: Read-only".                                                                      |
| `dependency-types`     | string  | `direct:production,direct:development,indirect` | Comma-separated dependency types that this call can approve and merge. Valid values: direct:production, direct:development, indirect.                                                                                         |
| `rename-title`         | boolean | `true`                                          | Edit the title and add the labels. When you call this workflow more than 1 time, set this to false on all calls but 1.                                                                                                        |
| `create-labels`        | boolean | `true`                                          | Create the "dependabot" and "auto-merged" labels if they do not exist.                                                                                                                                                        |
| `merge-method`         | string  | `squash`                                        | The merge method: squash, merge, or rebase.                                                                                                                                                                                   |
| `merge-mode`           | string  | `auto`                                          | How to merge. "auto": use GitHub auto-merge if the repository allows it; if not, wait for the checks in the job, then merge. "wait": always wait for the checks in the job, then merge. "now": merge at once, without a wait. |
| `wait-timeout-minutes` | number  | `30`                                            | For a wait in the job: the maximum time to wait for the checks, from 1 to 50. After this time, the PR stays open.                                                                                                             |
| `token-user`           | string  | (empty)                                         | The login of the "token" user. Leave empty to find it automatically. The workflow uses it to find its own approvals and its own merges.                                                                                       |

### The `token` secret

The `token` secret is optional. Without it, the workflow uses the `GITHUB_TOKEN`, with 2 limits:

- GitHub does not start new workflow runs for actions done with the `GITHUB_TOKEN`. After an auto-merge, no `push` workflow (for example, a release workflow) runs on the base branch, and task 4 cannot run.
- The workflow cannot find security updates, because the Dependabot alert lookup needs a PAT.

Store the PAT 2 times, with the same name and the same value: as a **Dependabot secret** and as an **Actions secret**. Store both in the organization or in the repository (**Settings > Secrets and variables > Dependabot**, and **> Actions**). The x2od organization uses the name `DEPENDABOT_TOKEN_X2OD`.

| Run started by                                                            | Secrets that the run can read                                         | Job that needs it    |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------- |
| Dependabot (it opens or updates a pull request)                           | Dependabot secrets only. This is also true for `pull_request_target`. | `update`             |
| A person or a PAT (for example, the merge that starts the `closed` event) | Actions secrets only                                                  | `labels-after-merge` |

> [!WARNING]
> If the PAT is only an Actions secret, the `update` job gets an empty `token` and uses the `GITHUB_TOKEN`. The job summary then shows `Token: GITHUB_TOKEN`, and the approval and merge show `github-actions[bot]`.

A fine-grained PAT needs these repository permissions:

| Permission        | Access         | Why                                                                                                                              |
| ----------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Contents          | Read and write | Merge the pull request                                                                                                           |
| Pull requests     | Read and write | Edit the title, approve, turn on auto-merge                                                                                      |
| Issues            | Read and write | Create labels and add them to the pull request                                                                                   |
| Metadata          | Read-only      | GitHub adds this automatically                                                                                                   |
| Dependabot alerts | Read-only      | Only for `autoapprove-security` or `automerge-security`                                                                          |
| Workflows         | Read and write | Recommended if Dependabot updates GitHub Actions versions. GitHub can refuse to merge changes to `.github/workflows` without it. |

A classic PAT needs the `repo` scope and the `workflow` scope. A fine-grained PAT has 1 resource owner, so repositories under 2 owners (x2od and dschach) need 1 PAT for each owner.

### Repository settings

- **Allow auto-merge** (Settings > General): the `auto` mode uses it if it is on. If it is off, the job waits for the checks.
- **Allow GitHub Actions to create and approve pull requests** (Settings > Actions > General): necessary if you do not pass the `token` secret.
- **Dependabot security updates** (Settings > Code security): necessary for security update pull requests.

### Different rules for each dependency type

Call the workflow 2 or more times, with 1 job for each call. Give each call its own `dependency-types` value and its own booleans. Set `rename-title: false` on all calls but 1.

```yaml
jobs:
  production:
    uses: x2od/.github/.github/workflows/dependabot-reusable.yml@main
    with:
      dependency-types: direct:production
      autoapprove-patch: true
      automerge-patch: true
  development:
    uses: x2od/.github/.github/workflows/dependabot-reusable.yml@main
    with:
      dependency-types: direct:development
      rename-title: false
      autoapprove-minor: true
      autoapprove-patch: true
      automerge-minor: true
      automerge-patch: true
```

(Each job also needs the `if`, `permissions`, and `secrets` lines from the first example.)

## Renovate shared configuration

[`renovate.json5`](renovate.json5) holds the shared Renovate rules. A repository uses them with 1 line in its own Renovate file, for example `.github/renovate.json`:

```json
{
	"$schema": "https://docs.renovatebot.com/renovate-schema.json",
	"extends": ["github>x2od/.github:renovate.json5"]
}
```

The repository file can add or change rules. For example, [`.github/renovate.json`](.github/renovate.json) in this repository turns on lock file maintenance every Monday before 4 AM.

The shared rules do these things:

- **Commit messages and PR titles** use Conventional Commits, with the package name as the scope: `build(prettier): update devdependency prettier from 3.9.9 to 3.9.10` (from this repository's history).

  | Dependency                                                        | Type    |
  | ----------------------------------------------------------------- | ------- |
  | npm `dependencies`                                                | `deps`  |
  | npm `devDependencies`, `optionalDependencies`, `peerDependencies` | `build` |
  | GitHub Actions                                                    | `ci`    |

- **Approval and merge:** Renovate approves major, minor, and patch updates, but does not merge them. These packages merge automatically for minor and patch updates: Prettier packages, `lint-staged`, `marked`, `mocha`, `husky`, `release-please`, and all `@x2od/` packages. Merges use a pull request and a squash.
- **Approval on the Dependency Dashboard:** updates to the `renovate` package, and major updates to GitHub Actions, wait for approval on the Dependency Dashboard issue. Minor, patch, and digest updates to GitHub Actions are off.
- **Pre-release packages** (version below 1.0.0) are not approved or merged automatically.
- **Groups:** all Jest packages update together, and all ESLint plugins update together.
- **Version ranges:** npm ranges are bumped. Peer dependency ranges are widened.
- **Labels:** each pull request gets the `renovate` label and its update level (`major`, `minor`, or `patch`).
- **Other settings:** the Dependency Dashboard is on, vulnerability alerts are on, lock file maintenance is off (a repository can turn it on), and the time zone is `America/Los_Angeles`.

## Workflow templates

The [`workflow-templates`](workflow-templates) directory holds starter workflows. A person with write access to a repository in the x2od organization finds them under **Actions > New workflow**, in the section for the organization. Each template has a `.properties.json` file that gives its name, description, and icon. Repositories outside the x2od organization (for example, dschach repositories) do not see the templates. Copy the file by hand for those repositories.

| Template                                                                                      | What it does                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Dependabot Approve and Auto-Merge](workflow-templates/dependabot-approve-and-auto-merge.yml) | Calls the [Dependabot reusable workflow](#dependabot-reusable-workflow) 3 times, 1 time for each dependency type, and approves and merges all Dependabot PRs. Its comments explain how to combine dependency types in 1 call. |
| [Auto-Assign Issues](workflow-templates/issue-auto-assign.yml)                                | Assigns each new or edited issue to `dschach`, with `pozil/auto-assign-issue`.                                                                                                                                                |
| [PMD Analysis Action](workflow-templates/pmd-analysis-action.yml)                             | Runs PMD on `force-app` on each push and pull request to the default branch, and uploads the results as a SARIF file to code scanning. GitHub suggests it for repositories that have a `sfdx-project.json` file.              |

## Community health files and organization profile

GitHub uses these files as defaults for each repository in the x2od organization that does not have its own file:

| File                                       | Purpose                 |
| ------------------------------------------ | ----------------------- |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Code of conduct         |
| [`CONTRIBUTING.md`](CONTRIBUTING.md)       | Contribution guidelines |
| [`SECURITY.md`](SECURITY.md)               | Security policy         |

### Issue templates

The [`.github/ISSUE_TEMPLATE`](.github/ISSUE_TEMPLATE) folder holds 2 issue forms. GitHub shows them when a person opens a new issue in an x2od repository.

| Template                                                      | Title prefix | Label         | Assignee  | Fields                                                                                                                                    |
| ------------------------------------------------------------- | ------------ | ------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Bug Report](.github/ISSUE_TEMPLATE/bug_report.yml)           | `[BUG]: `    | `bug`         | `dschach` | Description, Salesforce release, environment, steps to reproduce, current behavior, expected behavior, log output, additional information |
| [Feature Request](.github/ISSUE_TEMPLATE/feature_request.yml) | `[FEAT]: `   | `enhancement` | (none)    | Problem, proposed solution, alternatives, additional context, Code of Conduct agreement                                                   |

> [!NOTE]
> GitHub uses the org templates only in a repository that has **no** `.github/ISSUE_TEMPLATE` folder of its own. If a repository has even 1 template of its own, GitHub shows only that repository's templates. To use the org templates in such a repository, delete its `.github/ISSUE_TEMPLATE` folder.

[`profile/README.md`](profile/README.md) is the text on the [x2od organization page](https://github.com/x2od).

---

# .github

## Purpose

This repository stores reusable workflows for GitHub and other configuration files for use across repositories, including Renovate and Codecov.

Wherever possible, existing multi-job workflow files have been broken down to single-job workflows here so they can be mixed-and-matched.

The central workflow files live here. The templates for the files to call these are in the `workflow-templates` directory

# Contents

## Workflows

### SFDX

#### Create Scratch Org and Apex Test

Script that creates a scratch org, deploys metadata, runs Apex tests, calls other workflow, and deletes scratch org

#### Lint LWC and LWC Test

Run LWC tests

#### Prettier Verify

Ensures npm modules are installed, runs Prettier, exits with error if code is unformatted

#### SFDX Scanner

### GitHub CI

#### Release Please

#### PMD (download)

#### PMD (action)

#### Copy ApexDox Site

### Package Updates

#### Dependabot

#### Renovate

A central configuration file, `renovate.json5` is referenced from other repositories using the `renovate.json` file at `/.github/renovate.json`.

## Templates

### Bug Report

Configured with a YAML template instead of markdown, this template allows for text fields and picklists

### Feature Request

This is a more traditional markdown template
