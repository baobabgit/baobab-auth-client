"""Exceptions d'autorisation locale (rôles et permissions).

:spec: FEAT-001.4
"""

from __future__ import annotations

from baobab_auth_client.exceptions.base import BaobabAuthClientError


class AuthorizationError(BaobabAuthClientError):
    """Accès refusé pour rôle ou permission insuffisante."""


class RoleRequiredError(AuthorizationError):
    """Rôle requis manquant."""


class PermissionRequiredError(AuthorizationError):
    """Permission requise manquante."""
