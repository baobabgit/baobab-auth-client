"""Exceptions liées au JWKS.

:spec: FEAT-001.4
"""

from __future__ import annotations

from baobab_auth_client.exceptions.base import BaobabAuthClientError


class JwksError(BaobabAuthClientError):
    """Erreur générique liée au JWKS."""


class JwksFetchError(JwksError):
    """Échec de récupération du JWKS."""


class JwksKeyNotFoundError(JwksError):
    """Aucune clé ne correspond au ``kid`` demandé."""
