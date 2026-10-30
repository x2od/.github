# Changelog

## [0.1.2](https://github.com/x2od/.github/compare/v0.1.1...v0.1.2) (2026-10-30)


### ✨ Features

* **dependabot-reusable:** add per-type approve and merge inputs ([#167](https://github.com/x2od/.github/issues/167)) ([600b66f](https://github.com/x2od/.github/commit/600b66f020656b9a45800284dfc89c40699e7062))


### 🔧 Miscellaneous Chores

* **prettier:** remove JSON and JSON5 formatting overrides ([67ccaa6](https://github.com/x2od/.github/commit/67ccaa67889a772b7e3f3d11a47b914b882e52bc))


### 🐛 Bug Fixes

* **dependabot-reusable:** use build for indirect packages of devDependencies ([#166](https://github.com/x2od/.github/issues/166)) ([3ccde8f](https://github.com/x2od/.github/commit/3ccde8fec1080cc26f9e02a880288470716cc7d9))


### ⚡ Performance Improvements

* **dependabot:** combine three update jobs to one ([422a736](https://github.com/x2od/.github/commit/422a7361b5d46fbd19534c78e37ee6705ae31503))


### 👷 Continuous Integration

* **dependabot:** use 1 job in the Dependabot workflow template ([#168](https://github.com/x2od/.github/issues/168)) ([9ca0d9c](https://github.com/x2od/.github/commit/9ca0d9cf54e25d4606d28afc73425b44f5490dcb))
* **dependabot:** use the shared header comment in dependabot.yml ([3ccde8f](https://github.com/x2od/.github/commit/3ccde8fec1080cc26f9e02a880288470716cc7d9))
* document pull_request_target policy, rename Dependabot workflow ([#169](https://github.com/x2od/.github/issues/169)) ([0a4968f](https://github.com/x2od/.github/commit/0a4968f0ac1e28435baf08c0540c1b49e5402516))


### 📦 Build System

* **@x2od/prettier-config:** update devDependency @x2od/prettier-config from 0.5.0 to 0.6.0 ([#164](https://github.com/x2od/.github/issues/164)) ([e9dd8fd](https://github.com/x2od/.github/commit/e9dd8fd1f973a3d78a514815e9d5c16b7320d90e))
* **@x2od/prettier-config:** update devDependency @x2od/prettier-config from 0.6.0 to 0.7.0 ([#170](https://github.com/x2od/.github/issues/170)) ([6ae6a24](https://github.com/x2od/.github/commit/6ae6a2448f83bd72291c5c25b0a7acfef85da4ea))
* **dependabot:** rename dependabot update workflow ([8f6e484](https://github.com/x2od/.github/commit/8f6e484ce77de47ab7c21c237863fab23677981a))
* **follow-redirects:** bump follow-redirects from 1.16.0 to 1.16.1 ([#165](https://github.com/x2od/.github/issues/165)) ([ac34f6c](https://github.com/x2od/.github/commit/ac34f6c1ba6c0d4ac9f9f2989f3b64d5997a5680))
* **qs:** bump qs from 6.16.0 to 6.17.1 ([#172](https://github.com/x2od/.github/issues/172)) ([38820ac](https://github.com/x2od/.github/commit/38820acf7c6d7b4e02e242e833c99b2847f2808e))
* **undici:** bump undici from 8.11.2 to 8.12.3 ([#171](https://github.com/x2od/.github/issues/171)) ([c5a1e6e](https://github.com/x2od/.github/commit/c5a1e6eef68967f8411d426c3119f7bb39c52765))

## [0.1.1](https://github.com/x2od/.github/compare/v0.1.0...v0.1.1) (2026-10-20)


### ✨ Features

* **renovate:** combined shared preset for [@dschach](https://github.com/dschach) and [@x2od](https://github.com/x2od) ([#160](https://github.com/x2od/.github/issues/160)) ([dafdf6f](https://github.com/x2od/.github/commit/dafdf6f42164d41330da1a7e18c790ab602d012d))


### 🔧 Miscellaneous Chores

* exclude release please config from Prettier checks ([d4aa164](https://github.com/x2od/.github/commit/d4aa16450746a62ad0c645f6941b1990ec014f16))
* **renovate:** delete unused renovate.json5 preset ([#162](https://github.com/x2od/.github/issues/162)) ([8bb6b79](https://github.com/x2od/.github/commit/8bb6b7942d4cc26c195972247b0277264454737d))
* **renovate:** use renovate.jsonc shared preset from x2od/.github ([74e70aa](https://github.com/x2od/.github/commit/74e70aa264bdf2265c30ba2c83f46546089c4056))


### 👷 Continuous Integration

* **java-jdk:** update action java-jdk from 21.0.12+8.0.lts to v25 ([#151](https://github.com/x2od/.github/issues/151)) ([c5ef379](https://github.com/x2od/.github/commit/c5ef379d4d70d204b5365af4e6f3d035bf850950))


### 📦 Build System

* **@x2od/prettier-config:** update devdependency @x2od/prettier-config from 0.4.2 to 0.5.0 ([#161](https://github.com/x2od/.github/issues/161)) ([cb80669](https://github.com/x2od/.github/commit/cb80669b527d5794e3b71d0ab38759a7d982f35d))

## 0.1.0 (2026-10-20)


### ✨ Features

* add renovate & central config file ([#5](https://github.com/x2od/.github/issues/5)) ([f9b1d69](https://github.com/x2od/.github/commit/f9b1d6979afea9470feee726d8be1a5ac4db2d90))
* **dependabot:** add reusable Dependabot workflow ([#137](https://github.com/x2od/.github/issues/137)) ([de2af56](https://github.com/x2od/.github/commit/de2af56db6e124f5a90ce22957993769a401f1eb))
* new issue workflow template ([#10](https://github.com/x2od/.github/issues/10)) ([3ef8d11](https://github.com/x2od/.github/commit/3ef8d113a5c2ba7c04427b659b9be9e7b64b7e3d))
* **renovate:** copy json5 config to jsonc to set up mass migration ([cd1b2a2](https://github.com/x2od/.github/commit/cd1b2a207cf1cbbe397dbe192698ea7cd8d10be0))


### 🔧 Miscellaneous Chores

* delete unusable YAML PR template ([e37e5d7](https://github.com/x2od/.github/commit/e37e5d7c2a226d65a9babafc5020ef14d2e43312))
* delete workspace settings ([bd50d37](https://github.com/x2od/.github/commit/bd50d377580b3cbce1f77c89dcf53a8edc21bf95))
* **pmd:** start all PMD rules file ([c794713](https://github.com/x2od/.github/commit/c794713984aa1c93924c8e2c4cdaf88ecf1f3da7))
* **prettier:** use x2od shared config and override ([#145](https://github.com/x2od/.github/issues/145)) ([3feed8d](https://github.com/x2od/.github/commit/3feed8dc0d51a74c710a5d17f7907fc095c40bf8))
* pull request template update ([b36a70f](https://github.com/x2od/.github/commit/b36a70fa0274f2ba5e7a653a732ca09778acc51e))
* **release please:** bootstrap release please ([#156](https://github.com/x2od/.github/issues/156)) ([ead0e0c](https://github.com/x2od/.github/commit/ead0e0c2d57ba2d1eff07f138e3aaadddf70a222))
* **renovate:** allow some auto-merging ([#77](https://github.com/x2od/.github/issues/77)) ([8e0bf22](https://github.com/x2od/.github/commit/8e0bf22ebc04c59d43c6c9122783783d595dbb8a))
* **renovate:** enable lock file maintenance locally ([369007b](https://github.com/x2od/.github/commit/369007b9c7b84b50a80f16c1933008bedeb74d1b))
* **renovate:** Remove 'addLabels' from Renovate config ([00824bf](https://github.com/x2od/.github/commit/00824bfd175d6b3031593b5bda491ff7262b5472))
* **renovate:** update commitMessageTopic for various dependencies ([b2c2770](https://github.com/x2od/.github/commit/b2c277012620a0eca6d79ce71cf8443279a30d2a))
* **renovate:** update config ([#85](https://github.com/x2od/.github/issues/85)) ([ae6e22f](https://github.com/x2od/.github/commit/ae6e22f613c4ae552c489b1013cbfad878ce1308))
* **renovate:** update package matching and commit messages ([66c6536](https://github.com/x2od/.github/commit/66c6536718873c7d6cc8a68c5b855bf203962530))
* **renovate:** various updates ([b4d9426](https://github.com/x2od/.github/commit/b4d94267b61eda5de5ac1c12f6d7480e08998fa4))
* **renovat:** update renovate configuration ([9261537](https://github.com/x2od/.github/commit/9261537c7fa727e65574e512cddb3cd282743177))
* simplify PR template ([b97ccd6](https://github.com/x2od/.github/commit/b97ccd6eacbf1f1fd17620fe55f36e7eeb2dc2ca))
* update project files ([6e5ed9a](https://github.com/x2od/.github/commit/6e5ed9a904b67a6df9de49bf6096f56025f13e65))


### 📝 Documentation

* add README headings ([#11](https://github.com/x2od/.github/issues/11)) ([086abed](https://github.com/x2od/.github/commit/086abed0f9c66c35768474ae83e5ce2a79dff2d4))
* add README headings ([#11](https://github.com/x2od/.github/issues/11)) ([79359b3](https://github.com/x2od/.github/commit/79359b37b9f1766f348e9bc77a45cf7efba976c2))
* **contributing:** add CONTRIBUTING template file ([05576bd](https://github.com/x2od/.github/commit/05576bd9086c1df45c73a7c6878fbafbf8170225))
* **dependabot:** store the PAT as a Dependabot secret and an Actions secret ([#138](https://github.com/x2od/.github/issues/138)) ([9ea2a7c](https://github.com/x2od/.github/commit/9ea2a7c3b54e0ed30a7d0e294fbf4b3e64865e69))
* **pull-request:** create pull request template ([7c2e949](https://github.com/x2od/.github/commit/7c2e9495d01fef86f0231756ad931a2bdddfe465))
* update readme for renovate shared config ([a60ea1e](https://github.com/x2od/.github/commit/a60ea1e78bba5bbefa83001ea6f7e6199e458520))
* update security ([9c5c0dc](https://github.com/x2od/.github/commit/9c5c0dce3500cdc74b61ca46707b15659c496e80))


### 🐛 Bug Fixes

* **dependabot:** retry the merge after "Base branch was modified" ([#139](https://github.com/x2od/.github/issues/139)) ([75a111f](https://github.com/x2od/.github/commit/75a111f348dcc6b2979a46a690567a9a9045814c))
* fix husky installation ([4eb2089](https://github.com/x2od/.github/commit/4eb2089d743408f06f046e77b10eb65e7fcfc4c1))
* **pmd:** correct violationSuppressXPath and format allPMDRules.xml ([#154](https://github.com/x2od/.github/issues/154)) ([aa01ac3](https://github.com/x2od/.github/commit/aa01ac30cd707c7618f0e10a764eb5a14976ebdd))
* **prettier:** set xmlWhitespaceSensitivity to preserve from base ([93bf159](https://github.com/x2od/.github/commit/93bf159fd2b5f9b5ce1c44787f7db0a63827783d))
* **renovate:** fix org config file ([a2992a6](https://github.com/x2od/.github/commit/a2992a6de2cb59f612d464b9cbff367913cf66ed))
* **renovate:** undo bad config Prettier formatting ([d83f802](https://github.com/x2od/.github/commit/d83f8029de0b0f50ece1c95518688e43a987980f))


### ♻️ Code Refactoring

* **prettier:** reconcile local override with @x2od/prettier-config ([#153](https://github.com/x2od/.github/issues/153)) ([8d5646a](https://github.com/x2od/.github/commit/8d5646a7bf626335dfd3d4ca302882b22227ff7c))


### 🎨 Styles

* **prettier:** update config and run Prettier ([#149](https://github.com/x2od/.github/issues/149)) ([0bf7514](https://github.com/x2od/.github/commit/0bf75147f958d95067ae0fae85fe2869f3613e09))


### 👷 Continuous Integration

* **actions/checkout:** update actions/checkout action from v4 to v6 ([#79](https://github.com/x2od/.github/issues/79)) ([b81f845](https://github.com/x2od/.github/commit/b81f845645c7b7c6d46e80a4549ca041f0a343fc))
* **actions/checkout:** update actions/checkout action from v4 to v6.0.2 ([b81f845](https://github.com/x2od/.github/commit/b81f845645c7b7c6d46e80a4549ca041f0a343fc))
* **actions/checkout:** update actions/checkout action from v6.1.0 to v7 ([#123](https://github.com/x2od/.github/issues/123)) ([0024783](https://github.com/x2od/.github/commit/002478354a9fcce145242cb4bb16596fbda3aaaa))
* **actions/setup-java:** update actions/setup-java action from v4 to v5 ([#80](https://github.com/x2od/.github/issues/80)) ([ea62ea2](https://github.com/x2od/.github/commit/ea62ea27964b9e86bf1280ce9e877232952a77ab))
* **actions/setup-java:** update actions/setup-java action from v4 to v5.2.0 ([ea62ea2](https://github.com/x2od/.github/commit/ea62ea27964b9e86bf1280ce9e877232952a77ab))
* **actions/setup-java:** update actions/setup-java action from v5.7.0 to v6 ([#147](https://github.com/x2od/.github/issues/147)) ([10bbf0e](https://github.com/x2od/.github/commit/10bbf0ed954b52271eda7142ba90123102555c74))
* add dependabot auto-merge workflow template ([4bbb288](https://github.com/x2od/.github/commit/4bbb28841d1b7e12c9eaf71dae70279960e2fee1))
* create 2 templates ([#3](https://github.com/x2od/.github/issues/3)) ([eb6a84a](https://github.com/x2od/.github/commit/eb6a84a9b2b0dee528d308fd856c7b902372b206))
* **dependabot/fetch-metadata:** update dependabot/fetch-metadata action from v1 to v2 ([#36](https://github.com/x2od/.github/issues/36)) ([3817be2](https://github.com/x2od/.github/commit/3817be2ae3ec5ae013e296dd4ead4e54dcb126ad))
* **dependabot/fetch-metadata:** update dependabot/fetch-metadata action from v2 to v3 ([#82](https://github.com/x2od/.github/issues/82)) ([5d91da2](https://github.com/x2od/.github/commit/5d91da207f60157a9c85950e30abe90f44eb3e10))
* **dependabot/fetch-metadata:** update dependabot/fetch-metadata action from v2 to v3.1.0 ([5d91da2](https://github.com/x2od/.github/commit/5d91da207f60157a9c85950e30abe90f44eb3e10))
* **dependabot:** add Dependabot auto-handling ([6b7cb6e](https://github.com/x2od/.github/commit/6b7cb6e808cc0b82058fe9aa01736d8c28f10a13))
* **dependabot:** add Dependabot auto-handling ([b61ea4a](https://github.com/x2od/.github/commit/b61ea4a835afe9f3cc0876a0811439a888db3904))
* **dependabot:** remove auto-label dependabot PRs ([faae344](https://github.com/x2od/.github/commit/faae3440caf6f3403c47cd7811b48cbf8bcd7285))
* **dependabot:** remove dependabot to use Renovate ([99c1d2b](https://github.com/x2od/.github/commit/99c1d2bebcf670df7c31a3c74daee24c2015e951))
* **dependabot:** test the reusable workflow on each pull request ([#146](https://github.com/x2od/.github/issues/146)) ([2db94a0](https://github.com/x2od/.github/commit/2db94a08dd9358a06a52071e42ffc2e4e4cf37c8))
* do not auto-assign PRs for review ([8364f04](https://github.com/x2od/.github/commit/8364f04224e0ec9400fb1728f506205082859750))
* **github/codeql-action:** update github/codeql-action action from v3 to v4 ([#81](https://github.com/x2od/.github/issues/81)) ([b4ed914](https://github.com/x2od/.github/commit/b4ed9140c139ff58d4c16076ff0d9bc056ae22f8))
* **github/codeql-action:** update github/codeql-action action from v3 to v4.35.2 ([b4ed914](https://github.com/x2od/.github/commit/b4ed9140c139ff58d4c16076ff0d9bc056ae22f8))
* **pmd/pmd-github-action:** Update pmd/pmd-github-action action from v1 to v2 ([#31](https://github.com/x2od/.github/issues/31)) ([2ffb5cb](https://github.com/x2od/.github/commit/2ffb5cb76d59b07f0cc43f2400694c5ad2acb6cc))
* **pozil/auto-assign-issue:** bump pozil/auto-assign-issue from 1 to 2 ([#37](https://github.com/x2od/.github/issues/37)) ([0f29487](https://github.com/x2od/.github/commit/0f294871e450410c38a0331141b72c1bce32e382))
* **pozil/auto-assign-issue:** update pozil/auto-assign-issue action from v1 to v2 ([#86](https://github.com/x2od/.github/issues/86)) ([9052f48](https://github.com/x2od/.github/commit/9052f487b6f01679f7f9b9d8614c0abceecc27c6))
* **pozil/auto-assign-issue:** update pozil/auto-assign-issue action from v2.2.0 to v3 ([#94](https://github.com/x2od/.github/issues/94)) ([e688654](https://github.com/x2od/.github/commit/e68865499d413cb1baccc99e872ce8dc32616344))
* **pozil/auto-assign-issue:** update pozil/auto-assign-issue action from v3.0.0 to v4 ([#124](https://github.com/x2od/.github/issues/124)) ([f5a256e](https://github.com/x2od/.github/commit/f5a256e261f926638cb469aced72ca8b7c7cae87))
* **renovate:** disable automerge ([#67](https://github.com/x2od/.github/issues/67)) ([de59e3a](https://github.com/x2od/.github/commit/de59e3aaf4661765107f13cc938dd2a961fdec94))
* **renovate:** fix github-actions major update commit message extra ([8af7fd1](https://github.com/x2od/.github/commit/8af7fd1c61e06cfb69cf5c3caf548d22d15f4bfb))
* **renovate:** group eslint updates ([239b7c7](https://github.com/x2od/.github/commit/239b7c77e597767d40784d14b20470732ee10acf))
* **renovate:** group jest updates ([20ece3a](https://github.com/x2od/.github/commit/20ece3a0174bebff8e21419e2de005d613b07594))
* **renovate:** set global commit message ([3e1cdf6](https://github.com/x2od/.github/commit/3e1cdf6997c1726aeed2205ed2c7e277a6a8e138))
* **renovate:** set group update scopes ([c87d3ff](https://github.com/x2od/.github/commit/c87d3ffa882806048915c788df63e6eb36366319))
* **renovate:** stop eslint & jest groupings, keep eslint v9 ([c792a81](https://github.com/x2od/.github/commit/c792a813f6db553d59248d7414184efc81a7e9c5))
* **renovate:** update renovate config ([#72](https://github.com/x2od/.github/issues/72)) ([68703dd](https://github.com/x2od/.github/commit/68703dd3531aa3dbf28e19ec69fa39d8191ba06e))
* **updates:** update renovate & dependabot configs ([#6](https://github.com/x2od/.github/issues/6)) ([2f62468](https://github.com/x2od/.github/commit/2f6246803069adadb083ffd2d52e4ad108e067e7))


### 📦 Build System

* **@prettier/plugin-xml:** update devdependency @prettier/plugin-xml from 3.4.1 to 3.4.2 ([#91](https://github.com/x2od/.github/issues/91)) ([06dd242](https://github.com/x2od/.github/commit/06dd242aac11b94dae460e3ea84c656faac09eec))
* **@prettier/plugin-xml:** update devdependency @prettier/plugin-xml from 3.4.2 to 3.4.2 ([#76](https://github.com/x2od/.github/issues/76)) ([4856f0f](https://github.com/x2od/.github/commit/4856f0fc00ef70915ff85c3557d00845c763282f))
* **@x2od/prettier-config:** install @x2od/prettier-config ([#83](https://github.com/x2od/.github/issues/83)) ([1e29476](https://github.com/x2od/.github/commit/1e2947656d92b16aef35e194463dbc9584671a69))
* **@x2od/prettier-config:** update devdependency @x2od/prettier-config from 0.0.6 to 0.0.7 ([#97](https://github.com/x2od/.github/issues/97)) ([418d90c](https://github.com/x2od/.github/commit/418d90cbb5f355f95d5b79cc1fb13c54cb67f940))
* **@x2od/prettier-config:** update devdependency @x2od/prettier-config from 0.0.7 to 0.0.8 ([#115](https://github.com/x2od/.github/issues/115)) ([7098eb9](https://github.com/x2od/.github/commit/7098eb99a9ecdbe5b308b8acf9817d91e0ae74b7))
* **@x2od/prettier-config:** update devdependency @x2od/prettier-config from 0.0.8 to 0.1.0 ([#117](https://github.com/x2od/.github/issues/117)) ([ead1c7e](https://github.com/x2od/.github/commit/ead1c7e370031c8c08702eb403184a231172278d))
* **@x2od/prettier-config:** update devdependency @x2od/prettier-config from 0.1.0 to 0.2.0 ([#133](https://github.com/x2od/.github/issues/133)) ([d334de6](https://github.com/x2od/.github/commit/d334de6c5f5b76e8cd738f934c7964de14fda93e))
* **@x2od/prettier-config:** update devdependency @x2od/prettier-config from 0.2.0 to 0.3.0 ([#134](https://github.com/x2od/.github/issues/134)) ([3453387](https://github.com/x2od/.github/commit/345338790a932299a6097129264feaa4ed98f7a7))
* **@x2od/prettier-config:** update devdependency @x2od/prettier-config from 0.3.0 to 0.3.1 ([#136](https://github.com/x2od/.github/issues/136)) ([608bfd7](https://github.com/x2od/.github/commit/608bfd7dae7d563aeb3d6ed8d0462a4d3a4450ae))
* **@x2od/prettier-config:** update devdependency @x2od/prettier-config from 0.3.1 to 0.4.0 ([#148](https://github.com/x2od/.github/issues/148)) ([3c8b51f](https://github.com/x2od/.github/commit/3c8b51fe09b065235ff39027be3d40f4c4278547))
* **@x2od/prettier-config:** update devdependency @x2od/prettier-config from 0.4.0 to 0.4.2 ([#152](https://github.com/x2od/.github/issues/152)) ([65c2df2](https://github.com/x2od/.github/commit/65c2df229c18bb20d262a5be5d8df583202955e3))
* add central project config & PMD files ([26eceec](https://github.com/x2od/.github/commit/26eceece2212151d557a1e2dc19d7f1ce85e00ca))
* add prune script ([cd282df](https://github.com/x2od/.github/commit/cd282df21964d41add2101795593b6e5efaf143f))
* add prune script ([61d4277](https://github.com/x2od/.github/commit/61d42773fab17ca2185ef8ec5b50f92c8ba397dd))
* auto-assign PRs ([2694523](https://github.com/x2od/.github/commit/2694523ac51b7dcc61f56ab4e66579cd0cc89ca6))
* **axios:** bump axios from 1.18.1 to 1.20.0 ([#140](https://github.com/x2od/.github/issues/140)) ([41e6f39](https://github.com/x2od/.github/commit/41e6f395c10724d089b33dee92ea817ce6376e4a))
* bump axios from 1.18.1 to 1.20.0 ([41e6f39](https://github.com/x2od/.github/commit/41e6f395c10724d089b33dee92ea817ce6376e4a))
* bump joi from 18.2.3 to 18.3.0 ([55018a3](https://github.com/x2od/.github/commit/55018a37292d889d962a156f7e20dc6d012559d1))
* bump moment from 2.30.1 to 2.31.0 ([a9b583e](https://github.com/x2od/.github/commit/a9b583e3a57b1341ca78232a06a4687c5dbe1bec))
* bump renovate from 37.191.0 to 37.210.0 ([#7](https://github.com/x2od/.github/issues/7)) ([34995e8](https://github.com/x2od/.github/commit/34995e80be730641ad981fb830361965fac838d8))
* **husky:** bump husky from 9.0.10 to 9.0.11 ([#4](https://github.com/x2od/.github/issues/4)) ([574d825](https://github.com/x2od/.github/commit/574d82579868c0117803862ac2918bae2d08e5d8))
* **husky:** update dependency husky from 9.0.11 to 9.1.0 ([#49](https://github.com/x2od/.github/issues/49)) ([cf83ce7](https://github.com/x2od/.github/commit/cf83ce7fa84d9fdb225fe7e905b82114651fecba))
* **husky:** update dependency husky from 9.1.0 to 9.1.1 ([#50](https://github.com/x2od/.github/issues/50)) ([1943589](https://github.com/x2od/.github/commit/19435899f20634fc7f6eca16c38489b4e27cefd0))
* **husky:** update dependency husky from 9.1.1 to 9.1.2 ([#51](https://github.com/x2od/.github/issues/51)) ([eaa071c](https://github.com/x2od/.github/commit/eaa071c39d27e8e6b597670c232c4d3b7d1133ab))
* **husky:** update dependency husky from 9.1.2 to 9.1.3 ([#52](https://github.com/x2od/.github/issues/52)) ([8199f5d](https://github.com/x2od/.github/commit/8199f5dc36c6467fae291cff58b0373467deaf26))
* **husky:** update dependency husky from 9.1.3 to 9.1.4 ([#53](https://github.com/x2od/.github/issues/53)) ([6f47eea](https://github.com/x2od/.github/commit/6f47eeaa697b7eb1f63a2d9fb50c5afae1a7fd23))
* **husky:** update dependency husky from 9.1.4 to 9.1.5 ([#56](https://github.com/x2od/.github/issues/56)) ([446d866](https://github.com/x2od/.github/commit/446d8664b08f91b8c903a2667f6342a388196bd2))
* **husky:** update dependency husky from 9.1.5 to 9.1.6 ([#58](https://github.com/x2od/.github/issues/58)) ([b23c20f](https://github.com/x2od/.github/commit/b23c20f3f87222bafffb87a271d40feecd6f27ad))
* **husky:** update dependency husky from 9.1.6 to 9.1.7 ([#59](https://github.com/x2od/.github/issues/59)) ([4b2e700](https://github.com/x2od/.github/commit/4b2e700465309dba450a92f21604b27756b5fe35))
* **husky:** update husky files ([c7afbd4](https://github.com/x2od/.github/commit/c7afbd42092f43be369f9aff6d28ee1a908d9fe7))
* install renovate ([ae6e22f](https://github.com/x2od/.github/commit/ae6e22f613c4ae552c489b1013cbfad878ce1308))
* install Renovate ([5059626](https://github.com/x2od/.github/commit/5059626803b612ce8553f5c00d9bbfa96bc133b4))
* **issues:** add issue auto-assign workflow template ([086abed](https://github.com/x2od/.github/commit/086abed0f9c66c35768474ae83e5ce2a79dff2d4))
* **issues:** add issue auto-assign workflow template ([79359b3](https://github.com/x2od/.github/commit/79359b37b9f1766f348e9bc77a45cf7efba976c2))
* **joi:** bump joi from 18.2.3 to 18.3.0 ([#141](https://github.com/x2od/.github/issues/141)) ([55018a3](https://github.com/x2od/.github/commit/55018a37292d889d962a156f7e20dc6d012559d1))
* **lint-staged:** update dependency lint-staged from 15.2.10 to 15.2.11 ([#63](https://github.com/x2od/.github/issues/63)) ([e49d4f1](https://github.com/x2od/.github/commit/e49d4f16a6490a314bc8b503abeee35855847994))
* **lint-staged:** update dependency lint-staged from 15.2.11 to 15.3.0 ([#64](https://github.com/x2od/.github/issues/64)) ([8876100](https://github.com/x2od/.github/commit/8876100ec487f2823069b3b70930d00a61bc29d2))
* **lint-staged:** update dependency lint-staged from 15.2.2 to 15.2.4 ([#39](https://github.com/x2od/.github/issues/39)) ([d1ad230](https://github.com/x2od/.github/commit/d1ad2300fcde31a819acd5732298f0b2fe54fb5a))
* **lint-staged:** update dependency lint-staged from 15.2.4 to 15.2.5 ([#40](https://github.com/x2od/.github/issues/40)) ([2a777cb](https://github.com/x2od/.github/commit/2a777cb079625fac0fc0805cb0b3d8f338a1779c))
* **lint-staged:** update dependency lint-staged from 15.2.5 to 15.2.6 ([#45](https://github.com/x2od/.github/issues/45)) ([4b781e0](https://github.com/x2od/.github/commit/4b781e09467f033b9810858902971db6a6010cfb))
* **lint-staged:** update dependency lint-staged from 15.2.6 to 15.2.7 ([#46](https://github.com/x2od/.github/issues/46)) ([df861d8](https://github.com/x2od/.github/commit/df861d8ba401440d2c7c0f158c8e9e5be6855a67))
* **lint-staged:** update dependency lint-staged from 15.2.7 to 15.2.8 ([#54](https://github.com/x2od/.github/issues/54)) ([1724d78](https://github.com/x2od/.github/commit/1724d78465c01cb94b155d53f4d6437756fde34c))
* **lint-staged:** update dependency lint-staged from 15.2.8 to 15.2.9 ([#55](https://github.com/x2od/.github/issues/55)) ([b90989e](https://github.com/x2od/.github/commit/b90989ec611e0ef563628ec9e74687b2b9c1ed0f))
* **lint-staged:** update dependency lint-staged from 15.2.9 to 15.2.10 ([#57](https://github.com/x2od/.github/issues/57)) ([0f8fc3f](https://github.com/x2od/.github/commit/0f8fc3f582b5accaac3af83ae66ab7e6ed3fc928))
* **lint-staged:** update dependency lint-staged from 15.3.0 to 15.4.0 ([#65](https://github.com/x2od/.github/issues/65)) ([541d9b1](https://github.com/x2od/.github/commit/541d9b1210c38cd2edff8a9794deb73427c6314d))
* **lint-staged:** update dependency lint-staged from 15.4.0 to 15.4.1 ([#66](https://github.com/x2od/.github/issues/66)) ([cff0ca5](https://github.com/x2od/.github/commit/cff0ca54063768656b3e59fbd40789ec2251fdac))
* **lint-staged:** update dependency lint-staged from 15.4.1 to 15.5.2 ([#68](https://github.com/x2od/.github/issues/68)) ([4e4d450](https://github.com/x2od/.github/commit/4e4d4504053b3d350959ebadcd97c63d17cf43ab))
* **lint-staged:** update dependency lint-staged from 15.5.2 to 16.1.0 ([#73](https://github.com/x2od/.github/issues/73)) ([e1fe70f](https://github.com/x2od/.github/commit/e1fe70fcadef3fa9f2cf24a3f448fc23bb274f7a))
* **lint-staged:** update dependency lint-staged from 16.1.0 to 16.4.0 ([#74](https://github.com/x2od/.github/issues/74)) ([9b0818e](https://github.com/x2od/.github/commit/9b0818e22a12ab4d837fd796a97713ae446b182b))
* **lint-staged:** update devdependency lint-staged from 16.4.0 to 17.0.5 ([#93](https://github.com/x2od/.github/issues/93)) ([e49d8e2](https://github.com/x2od/.github/commit/e49d8e2026443422a20506100241bb58e4788662))
* **lint-staged:** update devdependency lint-staged from 17.0.5 to 17.0.5 ([#95](https://github.com/x2od/.github/issues/95)) ([c064407](https://github.com/x2od/.github/commit/c0644079a87e13c2b0049ecde6ae5bd391c35d54))
* **lint-staged:** update devdependency lint-staged from 17.0.5 to 17.0.6 ([#99](https://github.com/x2od/.github/issues/99)) ([1283d6a](https://github.com/x2od/.github/commit/1283d6ac1fdd5a67844bc62c87f21e48730ee005))
* **lint-staged:** update devdependency lint-staged from 17.0.6 to 17.0.7 ([#100](https://github.com/x2od/.github/issues/100)) ([d48e74c](https://github.com/x2od/.github/commit/d48e74cebc50b2054c03b205a7b6bfac5fe5ffac))
* **lint-staged:** update devdependency lint-staged from 17.0.7 to 17.0.8 ([#104](https://github.com/x2od/.github/issues/104)) ([4b55267](https://github.com/x2od/.github/commit/4b55267863112bbe8acce2458d8ee2b5a6cabbaa))
* **lint-staged:** update devdependency lint-staged from 17.0.8 to 17.1.0 ([#116](https://github.com/x2od/.github/issues/116)) ([0ae340b](https://github.com/x2od/.github/commit/0ae340b6eb18b8da82c8f82227f3b01512ebaa63))
* **lint-staged:** update devdependency lint-staged from 17.1.0 to 17.1.1 ([#119](https://github.com/x2od/.github/issues/119)) ([e5f97f8](https://github.com/x2od/.github/commit/e5f97f88759ddd65e9002925c209d3987b3ecd98))
* **lint-staged:** update devdependency lint-staged from 17.1.1 to 17.2.0 ([#120](https://github.com/x2od/.github/issues/120)) ([6f4dd0b](https://github.com/x2od/.github/commit/6f4dd0b8c3f68f298371d9cc94bf13cdfe0d6483))
* **lint-staged:** update devdependency lint-staged from 17.2.0 to 17.3.0 ([#121](https://github.com/x2od/.github/issues/121)) ([fb53671](https://github.com/x2od/.github/commit/fb53671a50c06f1521d3d3a252df41f54e53ddf7))
* **lint-staged:** update devdependency lint-staged from 17.3.0 to 17.4.1 ([#125](https://github.com/x2od/.github/issues/125)) ([8a693b3](https://github.com/x2od/.github/commit/8a693b351d7f4ade27d934227e915d730c7ee2ad))
* **lint-staged:** update devdependency lint-staged from 17.4.1 to 17.5.0 ([#126](https://github.com/x2od/.github/issues/126)) ([9e94a9a](https://github.com/x2od/.github/commit/9e94a9ae2ea4c51e75da3517c49c97063d9712c3))
* **lint-staged:** update devdependency lint-staged from 17.5.0 to 17.5.1 ([#127](https://github.com/x2od/.github/issues/127)) ([44c1254](https://github.com/x2od/.github/commit/44c12549a096eafb8cc9535b67957b70e9c8b10e))
* **lint-staged:** update devdependency lint-staged from 17.5.1 to 17.6.0 ([#132](https://github.com/x2od/.github/issues/132)) ([1a1aee5](https://github.com/x2od/.github/commit/1a1aee5667ad5c3cdf8e201826ae9b1bd6e871c9))
* **moment:** bump moment from 2.30.1 to 2.31.0 ([#143](https://github.com/x2od/.github/issues/143)) ([a9b583e](https://github.com/x2od/.github/commit/a9b583e3a57b1341ca78232a06a4687c5dbe1bec))
* **prettier:** update dependency prettier from 3.2.5 to 3.3.0 ([#41](https://github.com/x2od/.github/issues/41)) ([f9e779d](https://github.com/x2od/.github/commit/f9e779dcb58f9c1e90493ceee99177957f4b1fdf))
* **prettier:** update dependency prettier from 3.3.0 to 3.3.1 ([#42](https://github.com/x2od/.github/issues/42)) ([7eb0556](https://github.com/x2od/.github/commit/7eb05560c148a84115c42a8b7d8eaf2a8339ca75))
* **prettier:** update dependency prettier from 3.3.1 to 3.3.2 ([#43](https://github.com/x2od/.github/issues/43)) ([715aaaf](https://github.com/x2od/.github/commit/715aaaf7ef075045e6d335aaee4f329475a92081))
* **prettier:** update dependency prettier from 3.3.2 to 3.3.3 ([#48](https://github.com/x2od/.github/issues/48)) ([23a0761](https://github.com/x2od/.github/commit/23a0761643647dcd91f3668be3f9af28fdae9f2a))
* **prettier:** update dependency prettier from 3.3.3 to 3.4.0 ([#60](https://github.com/x2od/.github/issues/60)) ([893f570](https://github.com/x2od/.github/commit/893f57074744add509cf3003df7ed718b91b2078))
* **prettier:** update dependency prettier from 3.4.0 to 3.4.1 ([#61](https://github.com/x2od/.github/issues/61)) ([0e70b9b](https://github.com/x2od/.github/commit/0e70b9ba5715d1c593d27d6486d19eca194b9f47))
* **prettier:** update dependency prettier from 3.4.1 to 3.4.2 ([#62](https://github.com/x2od/.github/issues/62)) ([5454136](https://github.com/x2od/.github/commit/5454136b1519c8305c6f3aa6bc11af17b373c80c))
* **prettier:** update dependency prettier from 3.4.2 to 3.5.3 ([#69](https://github.com/x2od/.github/issues/69)) ([705b7a4](https://github.com/x2od/.github/commit/705b7a4ec7da8c1b093699cadfd676d552d83511))
* **prettier:** update dependency prettier from 3.5.3 to 3.8.3 ([#75](https://github.com/x2od/.github/issues/75)) ([016adaa](https://github.com/x2od/.github/commit/016adaabc6951a4b8e252dded7cc1088ceece2fc))
* **prettier:** update devdependency prettier from 3.8.3 to 3.8.4 ([#102](https://github.com/x2od/.github/issues/102)) ([2587847](https://github.com/x2od/.github/commit/25878478ebe48deb03e4019c12671a9f53a182aa))
* **prettier:** update devdependency prettier from 3.8.4 to 3.8.5 ([#109](https://github.com/x2od/.github/issues/109)) ([c386392](https://github.com/x2od/.github/commit/c3863921664a9f03670c3c02b57d04f244c18a01))
* **prettier:** update devdependency prettier from 3.8.5 to 3.9.0 ([#110](https://github.com/x2od/.github/issues/110)) ([d991ea7](https://github.com/x2od/.github/commit/d991ea7c41b6c1bd0680940e8604a6dcba4560e1))
* **prettier:** update devdependency prettier from 3.9.0 to 3.9.1 ([#111](https://github.com/x2od/.github/issues/111)) ([58408f4](https://github.com/x2od/.github/commit/58408f461f6c15aa93df2e341e9f1fd80f2487e6))
* **prettier:** update devdependency prettier from 3.9.1 to 3.9.3 ([#112](https://github.com/x2od/.github/issues/112)) ([c96cf30](https://github.com/x2od/.github/commit/c96cf30a5697e0da90a1f34572671da44790b4fa))
* **prettier:** update devdependency prettier from 3.9.3 to 3.9.4 ([#113](https://github.com/x2od/.github/issues/113)) ([7b66412](https://github.com/x2od/.github/commit/7b664123135380d1ecaf7dd0d7c948abdc994f57))
* **prettier:** update devdependency prettier from 3.9.4 to 3.9.5 ([#114](https://github.com/x2od/.github/issues/114)) ([f527337](https://github.com/x2od/.github/commit/f5273374ebcb40098b61bc676c07c29147569a05))
* **prettier:** update devdependency prettier from 3.9.5 to 3.9.6 ([#118](https://github.com/x2od/.github/issues/118)) ([b521e9c](https://github.com/x2od/.github/commit/b521e9c5019c351d2a4c66bd908763a0d40e4c88))
* **prettier:** update devdependency prettier from 3.9.6 to 3.9.7 ([#129](https://github.com/x2od/.github/issues/129)) ([755b96f](https://github.com/x2od/.github/commit/755b96fa830877f0fa354cb500d7ff8116752f03))
* **prettier:** update devdependency prettier from 3.9.7 to 3.9.8 ([#130](https://github.com/x2od/.github/issues/130)) ([ff98593](https://github.com/x2od/.github/commit/ff98593c2090deaf5571326b46d8d6ca4ebe8549))
* **prettier:** update devdependency prettier from 3.9.8 to 3.9.9 ([#131](https://github.com/x2od/.github/issues/131)) ([1d74d88](https://github.com/x2od/.github/commit/1d74d88d5ff640bfaa7683154d31043a5ff779c8))
* **prettier:** update devdependency prettier from 3.9.9 to 3.9.10 ([#135](https://github.com/x2od/.github/issues/135)) ([f60ea11](https://github.com/x2od/.github/commit/f60ea112849f276076deeff67251fe2fb8dd7684))
* **prettier:** update prettier config ([446f8bc](https://github.com/x2od/.github/commit/446f8bcd64dd4f8e5e37df7576fd20a7755bcf9d))
* **renovate:** add scope to Github actions updates ([8b4bd4c](https://github.com/x2od/.github/commit/8b4bd4c43121304cd614030af2f26b4733ada8bf))
* **renovate:** auto-label auto-merged PRs ([be6aee9](https://github.com/x2od/.github/commit/be6aee919808392efa401a81b8be96b4e8145bc2))
* **renovate:** bump renovate from 37.210.0 to 37.214.1 ([#9](https://github.com/x2od/.github/issues/9)) ([7c29456](https://github.com/x2od/.github/commit/7c29456db90ad8c0666906136fdb47289e5f76fc))
* **renovate:** bump renovate from 37.210.0 to 37.214.1 ([#9](https://github.com/x2od/.github/issues/9)) ([5b09e7a](https://github.com/x2od/.github/commit/5b09e7a7be8e0d8fb0613b583d995ca11cd2ea0a))
* **renovate:** bump renovate from 37.214.1 to 37.219.5 ([#13](https://github.com/x2od/.github/issues/13)) ([3b5d1eb](https://github.com/x2od/.github/commit/3b5d1eb765da325006a46c72eb94c7045743fd8c))
* **renovate:** bump renovate from 37.219.5 to 37.262.1 ([#29](https://github.com/x2od/.github/issues/29)) ([2ff38f1](https://github.com/x2od/.github/commit/2ff38f160c8b3bd9b1e46eb69078883c36159677))
* **renovate:** remove auto-merge label from renovate PRs ([c20b9ac](https://github.com/x2od/.github/commit/c20b9ac876d89cf581bf63808d436a9d34fc0cb1))
* **renovate:** test no v on github-actions update message ([25137f0](https://github.com/x2od/.github/commit/25137f0ce2506c385243cb87d84964600eae622f))
* **renovate:** update config file description ([5bfe80e](https://github.com/x2od/.github/commit/5bfe80e1c359cb57428ee426bc551b0f667b04bd))
* **renovate:** update devdependency renovate from 43.139.6 to 44.126.1 ([#122](https://github.com/x2od/.github/issues/122)) ([106f26d](https://github.com/x2od/.github/commit/106f26d9ed30d7a97f8ec70ee77d62e3567a5e6e))
* **renovate:** update devdependency renovate from 44.149.1 to 44.165.1 ([#144](https://github.com/x2od/.github/issues/144)) ([fc86e6b](https://github.com/x2od/.github/commit/fc86e6bb20d4aa37bcec17e48627ef3b93843a8e))
* **renovate:** update devdependency renovate from 44.165.1 to 44.171.1 ([#150](https://github.com/x2od/.github/issues/150)) ([cfd8e0b](https://github.com/x2od/.github/commit/cfd8e0b096c5aaf7c452115f77e2402a04268b59))


### ⬆️ Dependencies

* **brace-expansion:** bump brace-expansion from 1.1.14 to 1.1.21 ([#142](https://github.com/x2od/.github/issues/142)) ([c138353](https://github.com/x2od/.github/commit/c138353584756bf11fd013e495b5075d6ea56b8b))
* **renovate:** allow lowercase commit messages ([671a2a6](https://github.com/x2od/.github/commit/671a2a6230f57d44a5708e3ef69382dea7225cb9))
* **renovate:** make validation on-demand ([207d514](https://github.com/x2od/.github/commit/207d514a80546d7b946e879de58dccf8dea62b18))
