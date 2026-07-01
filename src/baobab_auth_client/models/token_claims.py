"""Claims JWT structurées côté client.

:spec: FEAT-001.3
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class TokenClaims:
    """Claims décodées d'un token compatible ``baobab-auth``.

    :param subject: Sujet d'authentification (``sub``).
    :param session_id: Session associée (``sid``).
    :param token_id: Identifiant du token (``jti``).
    :param roles: Rôles transportés.
    :param permissions: Permissions transportées.
    :param issued_at: Date d'émission (``iat``).
    :param expires_at: Date d'expiration (``exp``).
    :param issuer: Émetteur (``iss``).
    :param audience: Audience (``aud``).
    :param token_type: Type de token (``typ``).
    :param raw_claims: Claims brutes complètes.
    """

    subject: str
    session_id: str | None
    token_id: str | None
    roles: tuple[str, ...]
    permissions: tuple[str, ...]
    issued_at: datetime | None
    expires_at: datetime | None
    issuer: str | None
    audience: str | tuple[str, ...] | None
    token_type: str | None
    raw_claims: Mapping[str, Any]
