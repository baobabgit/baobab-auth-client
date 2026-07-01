"""Exceptions liées aux tokens JWT.

:spec: FEAT-001.4
"""

from __future__ import annotations

from baobab_auth_client.exceptions.base import BaobabAuthClientError


class TokenError(BaobabAuthClientError):
    """Erreur générique liée à un token."""


class TokenValidationError(TokenError):
    """Token invalide à la vérification."""


class TokenExpiredError(TokenValidationError):
    """Token expiré."""


class TokenSignatureError(TokenValidationError):
    """Signature de token invalide."""


class InvalidAlgorithmError(TokenValidationError):
    """Algorithme JWT non autorisé."""
