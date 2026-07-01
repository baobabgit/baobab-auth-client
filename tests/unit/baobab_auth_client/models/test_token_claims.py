"""Tests de ``TokenClaims`` et ``AuthHealth``."""

from __future__ import annotations

from datetime import UTC, datetime

from baobab_auth_client.models.auth_health import AuthHealth
from baobab_auth_client.models.token_claims import TokenClaims


class TestTokenClaims:
    """Construction des claims structurées."""

    def test_FEAT_001_3_token_claims_fields(self) -> None:
        now = datetime(2026, 1, 1, tzinfo=UTC)
        claims = TokenClaims(
            subject="auth_sub_xxx",
            session_id="session_xxx",
            token_id="token_xxx",
            roles=("USER",),
            permissions=("auth:user:read",),
            issued_at=now,
            expires_at=now,
            issuer="baobab-auth",
            audience="api-consommatrice",
            token_type="access",
            raw_claims={"sub": "auth_sub_xxx"},
        )
        assert claims.subject == "auth_sub_xxx"
        assert claims.token_type == "access"


class TestAuthHealth:
    """Modèle de santé du service auth."""

    def test_FEAT_001_3_auth_health_ok(self) -> None:
        health = AuthHealth(
            status="ok",
            auth_service_reachable=True,
            jwks_available=True,
            version="0.1.0",
        )
        assert health.status == "ok"
        assert health.jwks_available is True
