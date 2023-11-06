# 1.0.0
Nov 10, 2023
- Uses the stable v1 LMNT REST API.
- (BREAKING) Default audio encoding format is now mp3 (previously wav). Please pin to a previous version if needed.
- (BREAKING) Synthesize will no longer return just the binary audio data. It will instead always return a dictionary with keys `audio`, `durations` (optional), and `seed` (optional). Please pin to a previous version if needed.
- (BREAKING) Synthesize streaming will no longer return an aiohttp WSMessage. It will instead return a dictionary with keys `audio`, `durations` (optional), and `seed` (optional). Please pin to a previous version if needed.
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
