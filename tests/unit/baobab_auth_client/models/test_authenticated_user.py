"""Tests de ``AuthenticatedUser``."""

from __future__ import annotations

import dataclasses

import pytest

from baobab_auth_client.models.authenticated_user import AuthenticatedUser


def _sample_user() -> AuthenticatedUser:
    return AuthenticatedUser(
        id="auth_sub_xxx",
        email="user@example.com",
        username="demo",
        roles=("USER", "ADMIN"),
        permissions=("auth:user:read", "auth:user:write"),
        session_id="session_xxx",
        token_id="token_xxx",
        issuer="baobab-auth",
        audience="api-consommatrice",
        raw_claims={"sub": "auth_sub_xxx"},
    )


class TestAuthenticatedUser:
    """Helpers RBAC et immutabilité."""

    def test_FEAT_001_3_authenticated_user_has_role(self) -> None:
        user = _sample_user()
        assert user.has_role("ADMIN") is True
        assert user.has_role("SUPER_ADMIN") is False

    def test_FEAT_001_3_authenticated_user_has_any_role(self) -> None:
        user = _sample_user()
        assert user.has_any_role("SUPER_ADMIN", "ADMIN") is True

    def test_FEAT_001_3_authenticated_user_has_permissions(self) -> None:
        user = _sample_user()
        assert user.has_permission("auth:user:read") is True
        assert user.has_any_permission("auth:user:read", "other:perm") is True
        assert user.has_all_permissions("auth:user:read", "auth:user:write") is True
        assert user.has_all_permissions("auth:user:read", "missing") is False

    def test_FEAT_001_3_authenticated_user_is_immutable(self) -> None:
        user = _sample_user()
        with pytest.raises(dataclasses.FrozenInstanceError):
            user.id = "other"  # type: ignore[misc]
