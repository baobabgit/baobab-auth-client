"""Tests du package public ``baobab_auth_client``."""

from __future__ import annotations

import baobab_auth_client


class TestPackageExports:
    """Vérifie les exports publics du package."""

    def test_FEAT_001_5_package_exports_public_api(self) -> None:
        expected = {
            "ApiError",
            "AuthClientSettings",
            "AuthHealth",
            "AuthenticatedUser",
            "AuthorizationError",
            "BaobabAuthClientError",
            "ConfigurationError",
            "InvalidAlgorithmError",
            "JwksError",
            "PermissionRequiredError",
            "RoleRequiredError",
            "TokenClaims",
            "TokenError",
            "TokenExpiredError",
            "TokenPair",
            "TokenValidationError",
            "__version__",
        }
        assert set(baobab_auth_client.__all__) == expected
        assert baobab_auth_client.__version__ == "0.1.0"

    def test_FEAT_001_5_no_sqlalchemy_dependency(self) -> None:
        import importlib.util

        assert importlib.util.find_spec("sqlalchemy") is None

    def test_FEAT_001_5_no_security_runtime_dependency(self) -> None:
        import importlib.util

        assert importlib.util.find_spec("baobab_auth_security") is None
