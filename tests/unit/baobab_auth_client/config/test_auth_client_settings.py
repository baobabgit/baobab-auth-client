"""Tests de ``AuthClientSettings``."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from baobab_auth_client.config.auth_client_settings import AuthClientSettings
from baobab_auth_client.exceptions.configuration import ConfigurationError


class TestAuthClientSettings:
    """Cas nominaux et erreurs de configuration."""

    def test_FEAT_001_2_settings_valid_minimal(self) -> None:
        settings = AuthClientSettings(auth_base_url="https://auth.example.com")
        assert settings.auth_base_url == "https://auth.example.com"
        assert settings.algorithms == ("RS256",)
        assert settings.strict is True

    def test_FEAT_001_2_settings_builds_default_jwks_url(self) -> None:
        settings = AuthClientSettings(auth_base_url="https://auth.example.com")
        assert settings.jwks_url is None
        assert settings.resolved_jwks_url() == "https://auth.example.com/auth/jwks"

    def test_FEAT_001_2_settings_rejects_empty_base_url(self) -> None:
        with pytest.raises((ConfigurationError, ValidationError)):
            AuthClientSettings()
        with pytest.raises((ConfigurationError, ValidationError)):
            AuthClientSettings(auth_base_url="   ")

    def test_FEAT_001_2_settings_from_env(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv(
            "BAOBAB_AUTH_CLIENT_AUTH_BASE_URL",
            "https://auth.env.example.com",
        )
        settings = AuthClientSettings.from_env()
        assert settings.auth_base_url == "https://auth.env.example.com"

    def test_FEAT_001_2_settings_strips_trailing_slash(self) -> None:
        settings = AuthClientSettings(auth_base_url="https://auth.example.com/")
        assert settings.auth_base_url == "https://auth.example.com"

    def test_FEAT_001_2_settings_parse_algorithms_csv(self) -> None:
        settings = AuthClientSettings(
            auth_base_url="https://auth.example.com",
            algorithms="RS256,ES256",
        )
        assert settings.algorithms == ("RS256", "ES256")

    def test_FEAT_001_2_settings_validate_urls(self) -> None:
        settings = AuthClientSettings(auth_base_url="https://auth.example.com")
        settings.validate_urls()

    def test_FEAT_001_2_settings_invalid_url_raises(self) -> None:
        settings = AuthClientSettings(auth_base_url="not-a-url")
        with pytest.raises(ConfigurationError):
            settings.validate_urls()

    def test_FEAT_001_2_settings_is_immutable(self) -> None:
        settings = AuthClientSettings(auth_base_url="https://auth.example.com")
        with pytest.raises(ValidationError):
            settings.auth_base_url = "https://other.example.com"  # type: ignore[misc]

    def test_FEAT_001_2_settings_custom_jwks_url(self) -> None:
        settings = AuthClientSettings(
            auth_base_url="https://auth.example.com",
            jwks_url="https://auth.example.com/custom/jwks",
        )
        assert settings.jwks_url == "https://auth.example.com/custom/jwks"
