# Configuration — baobab-auth-client

## AuthClientSettings

| Paramètre | Variable d'environnement | Défaut |
|---|---|---|
| `auth_base_url` | `BAOBAB_AUTH_CLIENT_AUTH_BASE_URL` | requis |
| `jwks_url` | `BAOBAB_AUTH_CLIENT_JWKS_URL` | `{auth_base_url}/auth/jwks` |
| `issuer` | `BAOBAB_AUTH_CLIENT_ISSUER` | `None` |
| `audience` | `BAOBAB_AUTH_CLIENT_AUDIENCE` | `None` |
| `algorithms` | `BAOBAB_AUTH_CLIENT_ALGORITHMS` | `RS256` |
| `request_timeout_seconds` | `BAOBAB_AUTH_CLIENT_REQUEST_TIMEOUT_SECONDS` | `10.0` |
| `jwks_cache_ttl_seconds` | `BAOBAB_AUTH_CLIENT_JWKS_CACHE_TTL_SECONDS` | `3600` |
| `leeway_seconds` | `BAOBAB_AUTH_CLIENT_LEEWAY_SECONDS` | `0` |
| `strict` | `BAOBAB_AUTH_CLIENT_STRICT` | `true` |

Les algorithmes peuvent être fournis en CSV : `RS256,ES256`.
