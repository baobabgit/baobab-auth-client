"""État de santé du service d'authentification.

:spec: FEAT-001.3
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthHealth:
    """Résultat d'un contrôle de disponibilité du service auth.

    :param status: Statut global (ex. ``ok``, ``degraded``).
    :param auth_service_reachable: Indique si le service répond.
    :param jwks_available: Indique si le endpoint JWKS est disponible.
    :param version: Version du service si connue.
    """

    status: str
    auth_service_reachable: bool
    jwks_available: bool
    version: str | None = None
