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
