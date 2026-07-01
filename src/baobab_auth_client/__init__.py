"""``baobab-auth-client`` — librairie cliente d'intégration ``baobab-auth``.

Fournit la configuration, les modèles publics et les exceptions pour intégrer
une API métier au service ``baobab-auth-api`` sans réimplémenter la validation
JWT ni la gestion des rôles côté serveur auth.

Le contenu de ``__all__`` constitue le **contrat public** versionné en SemVer.

:spec: FEAT-001.1
"""

from __future__ import annotations

from baobab_auth_client.config import AuthClientSettings
from baobab_auth_client.exceptions import (
    ApiError,
    AuthorizationError,
    BaobabAuthClientError,
    ConfigurationError,
    InvalidAlgorithmError,
    JwksError,
    PermissionRequiredError,
    RoleRequiredError,
    TokenError,
    TokenExpiredError,
    TokenValidationError,
)
from baobab_auth_client.models import (
    AuthenticatedUser,
    AuthHealth,
    TokenClaims,
    TokenPair,
)
from baobab_auth_client.version import __version__

__all__ = [
    "ApiError",
    "AuthClientSettings",
    "AuthHealth",
    "AuthenticatedUser",
    "AuthorizationError",
    "BaobabAuthClientError",
    "ConfigurationError",
    "InvalidAlgorithmError",
    "JwksError",
    "PermissionRequiredError",
    "RoleRequiredError",
    "TokenClaims",
    "TokenError",
    "TokenExpiredError",
    "TokenPair",
    "TokenValidationError",
    "__version__",
]
