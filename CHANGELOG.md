# Changelog

## [2.5.2](https://github.com/lmnt-com/lmnt-python/compare/v2.5.1...v2.5.2) (2026-04-28)


### Chores

* bump nox and use session.run_install for uv sync ([74c4425](https://github.com/lmnt-com/lmnt-python/commit/74c4425f6a1c3ebc9c0c835cb04890889c650f44))
* regenerate sdk ([8004007](https://github.com/lmnt-com/lmnt-python/commit/80040072ee6b3999123a8dbf07fb0713f63bc62f))


### Documentation

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
