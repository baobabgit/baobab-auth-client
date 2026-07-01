"""Exceptions de configuration.

:spec: FEAT-001.4
"""

from __future__ import annotations

from baobab_auth_client.exceptions.base import BaobabAuthClientError


class ConfigurationError(BaobabAuthClientError):
    """Configuration invalide ou incohérente."""
