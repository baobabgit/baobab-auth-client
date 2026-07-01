"""Utilitaires anti-fuite de secrets dans les messages d'erreur.

:spec: FEAT-001.4
"""

from __future__ import annotations

import re

_JWT_PATTERN = re.compile(r"eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+")
_BEARER_PATTERN = re.compile(r"Bearer\s+\S+", re.IGNORECASE)


def assert_safe_message(message: str) -> str:
    """Vérifie qu'un message ne contient pas de secret évident.

    :param message: Message candidat.
    :returns: Le message inchangé s'il est sûr.
    :raises ValueError: Si un motif sensible est détecté.
    """
    if _JWT_PATTERN.search(message):
        msg = "Le message d'erreur ne doit pas contenir de token JWT."
        raise ValueError(msg)
    if _BEARER_PATTERN.search(message):
        msg = "Le message d'erreur ne doit pas contenir de token Bearer."
        raise ValueError(msg)
    lowered = message.lower()
    for marker in ("password=", "refresh_token=", "access_token="):
        if marker in lowered:
            msg = "Le message d'erreur ne doit pas contenir de secret."
            raise ValueError(msg)
    return message
