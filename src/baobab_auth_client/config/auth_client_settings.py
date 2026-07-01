"""Paramètres de configuration du client d'authentification.

:spec: FEAT-001.2, ADR-0001
"""

from __future__ import annotations

from pydantic import Field, HttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from baobab_auth_client.exceptions.configuration import ConfigurationError


class AuthClientSettings(BaseSettings):
    """Configuration immuable chargée depuis l'environnement.

    Préfixe d'environnement : ``BAOBAB_AUTH_CLIENT_`` (ex.
    ``BAOBAB_AUTH_CLIENT_AUTH_BASE_URL``). Aucun secret n'est stocké ici.

    :param auth_base_url: URL de base du service ``baobab-auth-api``.
    :param jwks_url: URL du endpoint JWKS (dérivée si absente).
    :param issuer: Émetteur attendu des tokens JWT.
    :param audience: Audience attendue des tokens JWT.
    :param algorithms: Algorithmes JWT autorisés.
    :param request_timeout_seconds: Délai maximal des requêtes HTTP.
    :param jwks_cache_ttl_seconds: Durée de vie du cache JWKS.
    :param leeway_seconds: Tolérance sur l'expiration des tokens.
    :param strict: Active les contrôles stricts de configuration.
    """

    model_config = SettingsConfigDict(
        env_prefix="BAOBAB_AUTH_CLIENT_",
        frozen=True,
        extra="ignore",
    )

    auth_base_url: str = ""
    jwks_url: str | None = None
    issuer: str | None = None
    audience: str | None = None
    algorithms: tuple[str, ...] = ("RS256",)
    request_timeout_seconds: float = Field(default=10.0, gt=0)
    jwks_cache_ttl_seconds: int = Field(default=3600, gt=0)
    leeway_seconds: int = Field(default=0, ge=0)
    strict: bool = True

    @field_validator("auth_base_url")
    @classmethod
    def validate_auth_base_url(cls, value: str) -> str:
        """Valide que l'URL de base n'est pas vide.

        :param value: URL de base fournie.
        :returns: URL normalisée sans slash final.
        :raises ConfigurationError: Si l'URL est vide.
        """
        stripped = value.strip()
        if not stripped:
            msg = "auth_base_url ne peut pas être vide."
            raise ConfigurationError(msg)
        return stripped.rstrip("/")

    @field_validator("algorithms", mode="before")
    @classmethod
    def parse_algorithms(cls, value: object) -> tuple[str, ...]:
        """Parse les algorithmes depuis une chaîne ou une séquence.

        :param value: Valeur brute (chaîne CSV ou séquence).
        :returns: Tuple d'algorithmes normalisés.
        """
        if isinstance(value, str):
            parts = [part.strip() for part in value.split(",") if part.strip()]
            return tuple(parts)
        if isinstance(value, (list, tuple)):
            return tuple(str(item).strip() for item in value if str(item).strip())
        return ("RS256",)

    @classmethod
    def from_env(cls) -> AuthClientSettings:
        """Charge la configuration depuis les variables d'environnement.

        :returns: Paramètres validés.
        """
        return cls()

    def resolved_jwks_url(self) -> str:
        """Retourne l'URL JWKS effective.

        :returns: URL JWKS explicite ou dérivée de ``auth_base_url``.
        """
        if self.jwks_url:
            return self.jwks_url
        return f"{self.auth_base_url}/auth/jwks"

    def validate_urls(self) -> None:
        """Valide le format des URLs de configuration.

        :raises ConfigurationError: Si une URL est invalide.
        """
        for name, value in (
            ("auth_base_url", self.auth_base_url),
            ("jwks_url", self.resolved_jwks_url()),
        ):
            try:
                HttpUrl(value)
            except ValueError as exc:
                msg = f"{name} invalide : {exc}"
                raise ConfigurationError(msg) from exc
