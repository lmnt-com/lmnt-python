# Changelog

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
