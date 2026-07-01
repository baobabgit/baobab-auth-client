"""Tests de ``TokenPair``."""

from __future__ import annotations

from baobab_auth_client.models.token_pair import TokenPair


class TestTokenPair:
    """Masquage des secrets dans la représentation."""

    def test_FEAT_001_3_token_pair_masks_secrets_in_repr(self) -> None:
        pair = TokenPair(
            access_token="secret-access",
            refresh_token="secret-refresh",
            token_type="Bearer",
            expires_in=900,
            refresh_expires_in=1209600,
        )
        representation = repr(pair)
        assert "secret-access" not in representation
        assert "secret-refresh" not in representation
        assert "***" in representation
