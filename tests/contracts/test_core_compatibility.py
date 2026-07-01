"""Tests de compatibilité avec ``baobab-auth-core``."""

from __future__ import annotations

from baobab_auth_core.application.results.authenticated_user import (
    AuthenticatedUser as CoreAuthenticatedUser,
)
from baobab_auth_core.application.results.token_claims import (
    TokenClaims as CoreTokenClaims,
)
from baobab_auth_core.application.results.token_pair import TokenPair as CoreTokenPair
from baobab_auth_core.domain.value_objects.auth_subject import AuthSubject
from baobab_auth_core.domain.value_objects.permission_name import PermissionName
from baobab_auth_core.domain.value_objects.role_name import RoleName


class TestCoreCompatibility:
    """Valide l'import des concepts stabilisés du core 0.4.x."""

    def test_FEAT_001_5_core_auth_subject_importable(self) -> None:
        subject = AuthSubject("auth_sub_xxx")
        assert str(subject) == "auth_sub_xxx"

    def test_FEAT_001_5_core_role_and_permission_names(self) -> None:
        role = RoleName("USER")
        permission = PermissionName("auth:user:read")
        assert str(role) == "USER"
        assert str(permission) == "auth:user:read"

    def test_FEAT_001_5_core_dtos_importable(self) -> None:
        assert CoreAuthenticatedUser is not None
        assert CoreTokenClaims is not None
        assert CoreTokenPair is not None
