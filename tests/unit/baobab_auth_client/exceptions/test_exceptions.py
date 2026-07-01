"""Tests des exceptions et garde anti-secret."""

from __future__ import annotations

import pytest

from baobab_auth_client.exceptions.api import ApiError
from baobab_auth_client.exceptions.authorization import PermissionRequiredError
from baobab_auth_client.exceptions.base import BaobabAuthClientError
from baobab_auth_client.exceptions.configuration import ConfigurationError
from baobab_auth_client.exceptions.jwks import JwksKeyNotFoundError
from baobab_auth_client.exceptions.message_guard import assert_safe_message
from baobab_auth_client.exceptions.token import TokenExpiredError


class TestExceptions:
    """Hiérarchie et absence de dépendance FastAPI."""

    def test_FEAT_001_4_exceptions_do_not_depend_on_fastapi(self) -> None:
        import importlib.util

        assert importlib.util.find_spec("fastapi") is None
        error = ConfigurationError("paramètre invalide")
        assert isinstance(error, BaobabAuthClientError)

    def test_FEAT_001_4_exception_hierarchy(self) -> None:
        assert issubclass(TokenExpiredError, BaobabAuthClientError)
        assert issubclass(JwksKeyNotFoundError, BaobabAuthClientError)
        assert issubclass(PermissionRequiredError, BaobabAuthClientError)
        assert issubclass(ApiError, BaobabAuthClientError)

    def test_FEAT_001_4_safe_message_accepts_plain_text(self) -> None:
        assert assert_safe_message("configuration invalide") == "configuration invalide"

    def test_FEAT_001_4_safe_message_rejects_jwt(self) -> None:
        jwt = (
            "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0."
            "dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U"
        )
        with pytest.raises(ValueError, match="JWT"):
            assert_safe_message(f"token invalide : {jwt}")

    def test_FEAT_001_4_safe_message_rejects_bearer(self) -> None:
        with pytest.raises(ValueError, match="Bearer"):
            assert_safe_message("Authorization: Bearer abc.def.ghi")

    def test_FEAT_001_4_safe_message_rejects_password_marker(self) -> None:
        with pytest.raises(ValueError, match="secret"):
            assert_safe_message("password=super-secret")

    def test_FEAT_001_4_exception_rejects_unsafe_message(self) -> None:
        jwt = (
            "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0."
            "dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U"
        )
        with pytest.raises(ValueError):
            ConfigurationError(f"erreur : {jwt}")
