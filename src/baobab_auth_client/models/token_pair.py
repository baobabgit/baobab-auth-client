"""Paire de tokens d'accès et de rafraîchissement.

:spec: FEAT-001.3
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TokenPair:
    """Paire de tokens sans fuite accidentelle dans les logs.

    :param access_token: Token d'accès sérialisé.
    :param refresh_token: Token de rafraîchissement sérialisé.
    :param token_type: Type de token (ex. ``Bearer``).
    :param expires_in: Durée de vie de l'access token en secondes.
    :param refresh_expires_in: Durée de vie du refresh token en secondes.
    """

    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    refresh_expires_in: int

    def __repr__(self) -> str:
        """Représentation masquant les valeurs sensibles.

        :returns: Représentation sans token brut.
        """
        return (
            "TokenPair(access_token='***', refresh_token='***', "
            f"token_type={self.token_type!r}, expires_in={self.expires_in}, "
            f"refresh_expires_in={self.refresh_expires_in})"
        )
