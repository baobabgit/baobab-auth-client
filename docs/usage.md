# Usage — baobab-auth-client v0.1.0

## Installation

```bash
uv sync
# ou
pip install -e ".[dev]"
```

## Configuration minimale

```python
from baobab_auth_client import AuthClientSettings

settings = AuthClientSettings(auth_base_url="https://auth.example.com")
# ou depuis l'environnement (préfixe BAOBAB_AUTH_CLIENT_)
settings = AuthClientSettings.from_env()
```

Variables d'environnement courantes :

- `BAOBAB_AUTH_CLIENT_AUTH_BASE_URL`
- `BAOBAB_AUTH_CLIENT_ISSUER`
- `BAOBAB_AUTH_CLIENT_AUDIENCE`

## Utilisateur authentifié (RBAC local)

```python
from baobab_auth_client import AuthenticatedUser

user = AuthenticatedUser(
    id="auth_sub_xxx",
    email="user@example.com",
    username=None,
    roles=("USER",),
    permissions=("auth:user:read",),
    session_id="session_xxx",
    token_id="token_xxx",
    issuer="baobab-auth",
    audience="api-consommatrice",
    raw_claims={},
)

if user.has_permission("auth:user:read"):
    ...
```

La validation JWT réelle et les dépendances FastAPI arrivent dans les versions
ultérieures (v0.2.0+).
