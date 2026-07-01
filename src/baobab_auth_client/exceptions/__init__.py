"""Hiérarchie d'exceptions de ``baobab-auth-client``.

:spec: FEAT-001.4
"""

from baobab_auth_client.exceptions.api import (
    ApiError,
    ApiResponseError,
    ApiUnavailableError,
)
from baobab_auth_client.exceptions.authorization import (
    AuthorizationError,
    PermissionRequiredError,
    RoleRequiredError,
)
from baobab_auth_client.exceptions.base import BaobabAuthClientError
from baobab_auth_client.exceptions.configuration import ConfigurationError
from baobab_auth_client.exceptions.jwks import (
    JwksError,
    JwksFetchError,
    JwksKeyNotFoundError,
)
from baobab_auth_client.exceptions.token import (
    InvalidAlgorithmError,
    TokenError,
    TokenExpiredError,
    TokenSignatureError,
    TokenValidationError,
)

__all__ = [
    "ApiError",
    "ApiResponseError",
    "ApiUnavailableError",
    "AuthorizationError",
    "BaobabAuthClientError",
    "ConfigurationError",
    "InvalidAlgorithmError",
    "JwksError",
    "JwksFetchError",
    "JwksKeyNotFoundError",
    "PermissionRequiredError",
    "RoleRequiredError",
    "TokenError",
    "TokenExpiredError",
    "TokenSignatureError",
    "TokenValidationError",
]
