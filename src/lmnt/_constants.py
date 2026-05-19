# Vendored runtime. See carbonsteel README for provenance.

import httpx

RAW_RESPONSE_HEADER = "X-Lmnt-Raw-Response"
OVERRIDE_CAST_TO_HEADER = "____lmnt_override_cast_to"

# default timeout is 1 minute
DEFAULT_TIMEOUT = httpx.Timeout(timeout=60, connect=5.0)
DEFAULT_MAX_RETRIES = 2
DEFAULT_CONNECTION_LIMITS = httpx.Limits(max_connections=100, max_keepalive_connections=20)

INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0
