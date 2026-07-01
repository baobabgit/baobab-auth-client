"""Utilisateur authentifié côté API consommatrice.

:spec: FEAT-001.3, ADR-0001
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class AuthenticatedUser:
    """Projection immuable d'un utilisateur validé via JWT.

    Ne contient jamais de token brut. Les rôles et permissions sont transportés
    depuis les claims, jamais recalculés localement.

    :param id: Identifiant stable du sujet (``sub``).
    :param email: Adresse email si disponible.
    :param username: Nom d'utilisateur si disponible.
    :param roles: Rôles portés par le token.
    :param permissions: Permissions portées par le token.
    :param session_id: Identifiant de session (``sid``).
    :param token_id: Identifiant du token (``jti``).
    :param issuer: Émetteur du token (``iss``).
    :param audience: Audience du token (``aud``).
    :param raw_claims: Claims brutes pour extension contrôlée.
    """

    id: str
    email: str | None
    username: str | None
    roles: tuple[str, ...]
    permissions: tuple[str, ...]
    session_id: str | None
    token_id: str | None
    issuer: str | None
    audience: str | tuple[str, ...] | None
    raw_claims: Mapping[str, Any]

    def has_role(self, role: str) -> bool:
        """Indique si l'utilisateur possède le rôle donné.

        :param role: Nom du rôle recherché.
        :returns: ``True`` si le rôle est présent.
        """
        return role in self.roles

    def has_any_role(self, *roles: str) -> bool:
        """Indique si l'utilisateur possède au moins un des rôles.

        :param roles: Rôles candidats.
        :returns: ``True`` si au moins un rôle correspond.
        """
        return any(role in self.roles for role in roles)

    def has_permission(self, permission: str) -> bool:
        """Indique si l'utilisateur possède la permission donnée.

        :param permission: Permission recherchée.
        :returns: ``True`` si la permission est présente.
        """
        return permission in self.permissions

    def has_any_permission(self, *permissions: str) -> bool:
        """Indique si l'utilisateur possède au moins une permission.

        :param permissions: Permissions candidates.
        :returns: ``True`` si au moins une permission correspond.
        """
        return any(permission in self.permissions for permission in permissions)

    def has_all_permissions(self, *permissions: str) -> bool:
        """Indique si l'utilisateur possède toutes les permissions.

        :param permissions: Permissions requises.
        :returns: ``True`` si toutes les permissions sont présentes.
        """
        return all(permission in self.permissions for permission in permissions)
