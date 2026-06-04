# Changelog

## [2.13.0](https://github.com/lmnt-com/lmnt-python/compare/v2.12.0...v2.13.0) (2026-06-04)


### Features

* allow lmnt.* subpackages from other distributions ([8efe4fe](https://github.com/lmnt-com/lmnt-python/commit/8efe4feed05ca8aaf86141f657b50c1fcc92e2b4))
* **api:** api update ([1600dfa](https://github.com/lmnt-com/lmnt-python/commit/1600dfa7a934aecfd75ec7a521f6f58f57a5755a))
* **api:** api update ([0624669](https://github.com/lmnt-com/lmnt-python/commit/062466911e46a88bedabc743af0e513b6fe0bf19))
* **api:** api update ([06b6c09](https://github.com/lmnt-com/lmnt-python/commit/06b6c097add6174d10b9828c79ecc357994cf35a))
* **api:** api update ([cc170c1](https://github.com/lmnt-com/lmnt-python/commit/cc170c18626b129a12e2856af514d714abc99073))
* **api:** api update ([0cf7bb9](https://github.com/lmnt-com/lmnt-python/commit/0cf7bb99d2c337276015b3fad88bb63fb51d7749))
* **api:** regenerate for LMNT API 1.1 ([e1c0cb2](https://github.com/lmnt-com/lmnt-python/commit/e1c0cb22c68bee0abda341d3879277b74324ed98))
* **api:** speech session improvements for API 1.1 ([04ce21e](https://github.com/lmnt-com/lmnt-python/commit/04ce21eefeae58c1081ebedb8f52527a41e77220))
* **api:** target API version 1.2 ([0e8dda2](https://github.com/lmnt-com/lmnt-python/commit/0e8dda2bf5376dc2d4eb187586a031c4e5de23c7))
* **client:** support file upload requests ([1d249d2](https://github.com/lmnt-com/lmnt-python/commit/1d249d2c8bb6a68f6ddacfca21d1b57321118f3e))
* improve future compat with pydantic v3 ([a1789ff](https://github.com/lmnt-com/lmnt-python/commit/a1789ff5ce84acc3c68acb5ab7080d853c779351))
* support resets in websocket speech sessions ([f6305f0](https://github.com/lmnt-com/lmnt-python/commit/f6305f0c8a4b790a4a00796d661b2ff1129c2612))
* **types:** replace List[str] with SequenceNotStr in params ([6ab9b05](https://github.com/lmnt-com/lmnt-python/commit/6ab9b052588fec354bb92590947d33953701012e))


### Bug Fixes

* avoid newer type syntax ([5ac3ffa](https://github.com/lmnt-com/lmnt-python/commit/5ac3ffa630232d1f00cb5c6e22f1bece932da1fd))
* clean up links ([c648d4d](https://github.com/lmnt-com/lmnt-python/commit/c648d4d8a29ebeb133ddf55b8f622ed13d6d0f85))
* **docs:** cleanup README.md ([f4427b6](https://github.com/lmnt-com/lmnt-python/commit/f4427b61ddbead564ed11f684ddc8e5012aea15a))
* extend lmnt.lib path for sibling distributions ([f848612](https://github.com/lmnt-com/lmnt-python/commit/f848612d1c0e9747c053b655fc51eac38635626e))
* **parsing:** ignore empty metadata ([c47d447](https://github.com/lmnt-com/lmnt-python/commit/c47d447eb05e4861882d65a8e67fc324b12a7a88))
* **parsing:** parse extra field types ([b6c94de](https://github.com/lmnt-com/lmnt-python/commit/b6c94de047a2403d4359b759ab159fce68bc5da7))
* replace ava with leah ([050a3d6](https://github.com/lmnt-com/lmnt-python/commit/050a3d6850a34c99080fb47552d2756b93dd27ab))


### Chores

* bump nox and use session.run_install for uv sync ([74c4425](https://github.com/lmnt-com/lmnt-python/commit/74c4425f6a1c3ebc9c0c835cb04890889c650f44))
* do not install brew dependencies in ./scripts/bootstrap by default ([dbe6074](https://github.com/lmnt-com/lmnt-python/commit/dbe6074fcb6b4efb3a530f18bb6cd7f636fc0424))
* drop pydantic v1 support ([104c7f7](https://github.com/lmnt-com/lmnt-python/commit/104c7f7897439852fbc2c2e82d4b562948fd342b))
* drop python 3.8 fallbacks and rye references ([6138efa](https://github.com/lmnt-com/lmnt-python/commit/6138efa6e75e238a370890f5d8877e28c1d50727))
* drop unused pydantic BaseModel import ([8c43e92](https://github.com/lmnt-com/lmnt-python/commit/8c43e92a6382ee4d737566bdadf81c71034ac5b6))
* fix import ordering in generated types ([094c4b9](https://github.com/lmnt-com/lmnt-python/commit/094c4b9f5b55bbd2633f7bb562f3198834ce0b40))
* generate api_resources tests from carbonsteel ([b9262db](https://github.com/lmnt-com/lmnt-python/commit/b9262dbf0edfe3deae4253917588634a1a4d5ec0))
* generate api.md from carbonsteel ([8d72de7](https://github.com/lmnt-com/lmnt-python/commit/8d72de7c0ed5e8acbb6642d48b3136c1237675cf))
* generate websocket types and sessions from asyncapi.yaml ([5150f43](https://github.com/lmnt-com/lmnt-python/commit/5150f436880efa15fe84d78ef6ce36657ef4f763))
* improve example values ([5f479a6](https://github.com/lmnt-com/lmnt-python/commit/5f479a6a87c337bd45d6ba25007568a2f1f9f714))
* **internal:** add Sequence related utils ([1eeba39](https://github.com/lmnt-com/lmnt-python/commit/1eeba39463b5fe2ae4de305ddc1aab5c4ca397b5))
* **internal:** fix ruff target version ([c568ed4](https://github.com/lmnt-com/lmnt-python/commit/c568ed4b54998bd082e34ed584400281bbd68828))
* **internal:** move mypy configurations to `pyproject.toml` file ([dcabfa7](https://github.com/lmnt-com/lmnt-python/commit/dcabfa72bfa6726a7ad6948d5046aaacf160cf69))
* **internal:** update comment in script ([b0a4944](https://github.com/lmnt-com/lmnt-python/commit/b0a4944ffc139a3830d1f4eaecea476444d8c27d))
* **internal:** update pydantic dependency ([278c930](https://github.com/lmnt-com/lmnt-python/commit/278c93009ae6b7affd8edb18d14cc81bf58e702f))
* **internal:** update pyright exclude list ([499e83d](https://github.com/lmnt-com/lmnt-python/commit/499e83d0641f49c8341eee48cdcfda6d9ab7091f))
* migrate from rye to uv ([a845166](https://github.com/lmnt-com/lmnt-python/commit/a845166a810d411ece2675ff20bf74c88d3f9ad3))
* **project:** add settings file for vscode ([d40f40b](https://github.com/lmnt-com/lmnt-python/commit/d40f40b1b0c5dc5b99c60e8fc825a9645ae76aa0))
* regenerate from new code generator ([c4bb01b](https://github.com/lmnt-com/lmnt-python/commit/c4bb01b3c2b871f17085605b32d4bcb4f3662080))
* regenerate from new code generator ([cc0b428](https://github.com/lmnt-com/lmnt-python/commit/cc0b42810cbd5d37b5d4821967dc3070774f1638))
* regenerate sdk ([e20c385](https://github.com/lmnt-com/lmnt-python/commit/e20c3856d1bd9a8373576df20f1211c2aff3e66a))
* regenerate sdk ([8004007](https://github.com/lmnt-com/lmnt-python/commit/80040072ee6b3999123a8dbf07fb0713f63bc62f))
* register runtime files in manifest ([e117e4b](https://github.com/lmnt-com/lmnt-python/commit/e117e4be5f79a2384cbf7528fbf73595e6cbc312))
* remove devcontainer config ([c1da477](https://github.com/lmnt-com/lmnt-python/commit/c1da477276c091dae6919f6e029eab81e4b74387))
* remove MIGRATING.md ([9bbb761](https://github.com/lmnt-com/lmnt-python/commit/9bbb76196a3f1b9262001ac56077d12566b621cf))
* remove SECURITY.md ([22341da](https://github.com/lmnt-com/lmnt-python/commit/22341da2983ef4d379a086b2029dcf6de0eb9704))
* remove stainless sync state files ([380b363](https://github.com/lmnt-com/lmnt-python/commit/380b363570c578ca76dc1ec91b63daf0fec10235))
* replace X-Stainless-* request headers with X-Lmnt-* ([7062321](https://github.com/lmnt-com/lmnt-python/commit/70623215c5259739570bcfac100b7572fc602437))
* silence pyright on request_id field overrides and list narrowing ([f8bf9bd](https://github.com/lmnt-com/lmnt-python/commit/f8bf9bdddca2c50fb475ea8c06d8d3387b2ebb40))
* **tests:** simplify `get_platform` test ([c8a3b08](https://github.com/lmnt-com/lmnt-python/commit/c8a3b081e15e9bc5cfa3e36ae926c5f187ae9240))
* **types:** change optional parameter type from NotGiven to Omit ([71e130d](https://github.com/lmnt-com/lmnt-python/commit/71e130d57a10f4a17690f6f48f15ed65b97993f7))
* update @stainless-api/prism-cli to v5.15.0 ([bd8d3ab](https://github.com/lmnt-com/lmnt-python/commit/bd8d3ab0239e85912886079d281ed69043f2ef8b))


### Documentation

* link LMNT API reference in README intro ([721854b](https://github.com/lmnt-com/lmnt-python/commit/721854b0acd967cc5217c4815a472665b71330bf))
* refresh speech session descriptions ([3226e7a](https://github.com/lmnt-com/lmnt-python/commit/3226e7ad425aeb00c2289dfb49fe573acef55b7a))
* streamline README and drop examples/ ([2d5b925](https://github.com/lmnt-com/lmnt-python/commit/2d5b925e5814b3fcc2219c749e3730d6d0cf926d))

## [2.6.1](https://github.com/lmnt-com/lmnt-python/compare/v2.6.0...v2.6.1) (2026-05-19)


### Chores

* regenerate sdk ([e20c385](https://github.com/lmnt-com/lmnt-python/commit/e20c3856d1bd9a8373576df20f1211c2aff3e66a))
* replace X-Stainless-* request headers with X-Lmnt-* ([7062321](https://github.com/lmnt-com/lmnt-python/commit/70623215c5259739570bcfac100b7572fc602437))

## [2.6.0](https://github.com/lmnt-com/lmnt-python/compare/v2.5.1...v2.6.0) (2026-05-09)


### Features

* **api:** regenerate for LMNT API 1.1 ([e1c0cb2](https://github.com/lmnt-com/lmnt-python/commit/e1c0cb22c68bee0abda341d3879277b74324ed98))
* **api:** speech session improvements for API 1.1 ([04ce21e](https://github.com/lmnt-com/lmnt-python/commit/04ce21eefeae58c1081ebedb8f52527a41e77220))


### Chores

* bump nox and use session.run_install for uv sync ([74c4425](https://github.com/lmnt-com/lmnt-python/commit/74c4425f6a1c3ebc9c0c835cb04890889c650f44))
* drop pydantic v1 support ([104c7f7](https://github.com/lmnt-com/lmnt-python/commit/104c7f7897439852fbc2c2e82d4b562948fd342b))
* drop unused pydantic BaseModel import ([8c43e92](https://github.com/lmnt-com/lmnt-python/commit/8c43e92a6382ee4d737566bdadf81c71034ac5b6))
* regenerate sdk ([8004007](https://github.com/lmnt-com/lmnt-python/commit/80040072ee6b3999123a8dbf07fb0713f63bc62f))
* silence pyright on request_id field overrides and list narrowing ([f8bf9bd](https://github.com/lmnt-com/lmnt-python/commit/f8bf9bdddca2c50fb475ea8c06d8d3387b2ebb40))


### Documentation

* link LMNT API reference in README intro ([721854b](https://github.com/lmnt-com/lmnt-python/commit/721854b0acd967cc5217c4815a472665b71330bf))
* refresh speech session descriptions ([3226e7a](https://github.com/lmnt-com/lmnt-python/commit/3226e7ad425aeb00c2289dfb49fe573acef55b7a))
* streamline README and drop examples/ ([2d5b925](https://github.com/lmnt-com/lmnt-python/commit/2d5b925e5814b3fcc2219c749e3730d6d0cf926d))

## [2.5.1](https://github.com/lmnt-com/lmnt-python/compare/v2.5.0...v2.5.1) (2026-04-26)


### Bug Fixes

* extend lmnt.lib path for sibling distributions ([f848612](https://github.com/lmnt-com/lmnt-python/commit/f848612d1c0e9747c053b655fc51eac38635626e))

## [2.5.0](https://github.com/lmnt-com/lmnt-python/compare/v2.4.1...v2.5.0) (2026-04-26)


### Features

* allow lmnt.* subpackages from other distributions ([8efe4fe](https://github.com/lmnt-com/lmnt-python/commit/8efe4feed05ca8aaf86141f657b50c1fcc92e2b4))

## [2.4.1](https://github.com/lmnt-com/lmnt-python/compare/v2.4.0...v2.4.1) (2026-04-26)


### Chores

* drop python 3.8 fallbacks and rye references ([6138efa](https://github.com/lmnt-com/lmnt-python/commit/6138efa6e75e238a370890f5d8877e28c1d50727))
* fix import ordering in generated types ([094c4b9](https://github.com/lmnt-com/lmnt-python/commit/094c4b9f5b55bbd2633f7bb562f3198834ce0b40))
* generate api_resources tests from carbonsteel ([b9262db](https://github.com/lmnt-com/lmnt-python/commit/b9262dbf0edfe3deae4253917588634a1a4d5ec0))
* generate api.md from carbonsteel ([8d72de7](https://github.com/lmnt-com/lmnt-python/commit/8d72de7c0ed5e8acbb6642d48b3136c1237675cf))
* generate websocket types and sessions from asyncapi.yaml ([5150f43](https://github.com/lmnt-com/lmnt-python/commit/5150f436880efa15fe84d78ef6ce36657ef4f763))
* migrate from rye to uv ([a845166](https://github.com/lmnt-com/lmnt-python/commit/a845166a810d411ece2675ff20bf74c88d3f9ad3))
* regenerate from new code generator ([c4bb01b](https://github.com/lmnt-com/lmnt-python/commit/c4bb01b3c2b871f17085605b32d4bcb4f3662080))
* regenerate from new code generator ([cc0b428](https://github.com/lmnt-com/lmnt-python/commit/cc0b42810cbd5d37b5d4821967dc3070774f1638))
* register runtime files in manifest ([e117e4b](https://github.com/lmnt-com/lmnt-python/commit/e117e4be5f79a2384cbf7528fbf73595e6cbc312))
* remove devcontainer config ([c1da477](https://github.com/lmnt-com/lmnt-python/commit/c1da477276c091dae6919f6e029eab81e4b74387))
* remove MIGRATING.md ([9bbb761](https://github.com/lmnt-com/lmnt-python/commit/9bbb76196a3f1b9262001ac56077d12566b621cf))
* remove SECURITY.md ([22341da](https://github.com/lmnt-com/lmnt-python/commit/22341da2983ef4d379a086b2029dcf6de0eb9704))
* remove stainless sync state files ([380b363](https://github.com/lmnt-com/lmnt-python/commit/380b363570c578ca76dc1ec91b63daf0fec10235))

## v2.4.0 (2025-09-30)

Full Changelog: [v2.3.0...v2.4.0](https://github.com/lmnt-com/lmnt-python/compare/v2.3.0...v2.4.0)

- feat(api): api update ([6e0a4dd](https://github.com/lmnt-com/lmnt-python/commit/6e0a4dda62360a40d20a591ec744f2111a53a6e8))
- feat(api): api update ([cc7f909](https://github.com/lmnt-com/lmnt-python/commit/cc7f909d59c7bca2cedfc204704cd31dbb32916c))
- chore(internal): update pydantic dependency ([a4c5af5](https://github.com/lmnt-com/lmnt-python/commit/a4c5af517ea5fe4de75612fb596cb7e643115edb))
- chore(types): change optional parameter type from NotGiven to Omit ([7c03fb8](https://github.com/lmnt-com/lmnt-python/commit/7c03fb8645d067dd9992b98da473df9f02b901fc))
- chore: do not install brew dependencies in ./scripts/bootstrap by default ([75d2397](https://github.com/lmnt-com/lmnt-python/commit/75d23979700a889a7ceae787f8449ce66cc53733))
- chore: improve example values ([5c0919c](https://github.com/lmnt-com/lmnt-python/commit/5c0919cd356a9624a9a1b5d0e4a802d7b107226f))
      

## v2.3.0 (2025-09-03)

Full Changelog: [v2.2.1...v2.3.0](https://github.com/lmnt-com/lmnt-python/compare/v2.2.1...v2.3.0)

- replace ava with leah ([47bb854](https://github.com/lmnt-com/lmnt-python/commit/47bb854e04529deb4b29f5b816bbc20c0abe9a3e))
- avoid newer type syntax ([773b08e](https://github.com/lmnt-com/lmnt-python/commit/773b08ee4f4b1456d21fe17cc09fe99789e663e4))
- chore(internal): update pyright exclude list ([8c1bd1d](https://github.com/lmnt-com/lmnt-python/commit/8c1bd1deda2b735d001b52ca1458938bd10bca77))
- feat(api): api update ([7820c00](https://github.com/lmnt-com/lmnt-python/commit/7820c00ae0e8e9ad867b23f35a16a9e6d51fba4c))
- chore(internal): add Sequence related utils ([f1f239b](https://github.com/lmnt-com/lmnt-python/commit/f1f239b20585a2519c7477dcc84e7a7a4fac4d95))


## v2.2.1 (2025-08-21)

Full Changelog: [v2.2.0...v2.2.1](https://github.com/lmnt-com/lmnt-python/compare/v2.2.0...v2.2.1)

- chore(internal): fix ruff target version ([08c3067](https://github.com/lmnt-com/lmnt-python/commit/08c3067ada19ee943719e77bbbc9f25c3da32eef))
- chore: update @stainless-api/prism-cli to v5.15.0 ([1634751](https://github.com/lmnt-com/lmnt-python/commit/16347518c7eae85d6524e8b35c5203a238b1ef5e))
- chore(internal): update comment in script ([6649334](https://github.com/lmnt-com/lmnt-python/commit/6649334778e2cd8e3a433ca6182c11a44a4ce484))
      

## v2.2.0 (2025-08-05)

Full Changelog: [v2.1.0...v2.2.0](https://github.com/lmnt-com/lmnt-python/compare/v2.1.0...v2.2.0)

- feat: add support for resets in websocket speech sessions

## v2.1.0 (2025-08-05)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/lmnt-com/lmnt-python/compare/v2.0.0...v2.1.0)

- fix(parsing): ignore empty metadata ([2671330](https://github.com/lmnt-com/lmnt-python/commit/267133097ede5f0980c2479f41d2b1627baa9205))
- fix(parsing): parse extra field types ([e652a62](https://github.com/lmnt-com/lmnt-python/commit/e652a624a99ba3c5c198aa00a198b6d0a4f69283))
- chore(project): add settings file for vscode ([9d450b1](https://github.com/lmnt-com/lmnt-python/commit/9d450b1915dbb53698e1aec84b8fee4d485fee86))
- feat(api): api update ([f0ef880](https://github.com/lmnt-com/lmnt-python/commit/f0ef8801046aa0ccad2eb44e67a6a44541d3f09b))
      
July 17, 2025
# 2.0.0
- **BREAKING CHANGES**: The new v2 SDK provides more streaming functionality, a more modern, type-safe interface with better error handling, and improved performance. To migrate from the legacy v1 SDK, please update your code to use the new behavior or pin to a previous version if preferred. More details in the [migration guide](./MIGRATING.md).

# 1.1.0
Jan 3, 2024
- `synthesize_streaming` will now return a `buffer_empty` boolean when extras are requested. This can be used to determine when the server has no more audio to send after the client has sent a `flush` message.
- A bug that caused `create_voice` to fail in Python 3.8 and earlier has been fixed.

# 1.0.1
Nov 18, 2023
- Changes the owner type in `list_voices` from 'lmnt' to 'system' to match the LMNT REST API.

# 1.0.0
Nov 14, 2023
- Uses the stable v1 LMNT REST API.
- **BREAKING CHANGES**: please update your code to use the new behavior or pin to a previous version if preferred.
    - Default audio encoding format in `synthesize` is now `mp3` (previously `wav`). Format can be specified by adding `format='wav'` or `format='mp3'` to the `synthesize` call.
    - `list_voices` now returns a list of voice dictionaries for simplicity of return values and ease of use. Previously it returned a dictionary with key `voices` which contained a dictionary of voice dictionaries keyed by their voice id.
    - `synthesize` no longer returns just the binary audio data. It instead always returns a dictionary with keys `audio`, `durations` (optional), and `seed` (optional).
    - `synthesize_streaming` no longer returns an `aiohttp WSMessage`. It instead returns a dictionary with keys `audio`, `durations` (optional), and `seed` (optional).
- Adds support for creating, updating, and deleting voices as well as getting account details.

# 0.2.1

Oct 12, 2023
- Removes the default seed of synthesize (previously 0). When seed is unspecified, synthesize will now use a random seed.
- The durations dictionary has been updated. Now includes each word itself and changes the units of duration from the number of samples to seconds.

# 0.2.0

Sep 7, 2023
- Add support for durations.

# 0.1.0

Aug 11, 2023
- Initial release
