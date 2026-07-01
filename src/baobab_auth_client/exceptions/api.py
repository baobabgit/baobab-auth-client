"""Exceptions liées aux appels API auth.

:spec: FEAT-001.4
"""

from __future__ import annotations

from baobab_auth_client.exceptions.base import BaobabAuthClientError


class ApiError(BaobabAuthClientError):
    """Erreur générique lors d'un appel au service auth."""


class ApiUnavailableError(ApiError):
    """Le service auth est indisponible."""


class ApiResponseError(ApiError):
    """Réponse HTTP inattendue du service auth."""
