"""Exception racine du client ``baobab-auth-client``.

:spec: FEAT-001.4
"""

from __future__ import annotations

from baobab_auth_client.exceptions.message_guard import assert_safe_message


class BaobabAuthClientError(Exception):
    """Racine de toutes les erreurs de ``baobab-auth-client``."""

    def __init__(self, message: str) -> None:
        """Initialise l'exception avec un message sûr.

        :param message: Description de l'erreur sans secret.
        """
        super().__init__(assert_safe_message(message))
