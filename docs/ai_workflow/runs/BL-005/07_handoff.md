# Handoff — BL-001 à BL-005 (v0.1.0)

## État

Tous les backlogs v0.1.0 (BL-001 à BL-005) sont implémentés sur `version/v0.1.0`.

## Réalisé

- Package `baobab_auth_client` installable (pyproject, py.typed, exports publics)
- `AuthClientSettings` avec `from_env()` et dérivation JWKS
- Modèles : `AuthenticatedUser`, `TokenPair`, `TokenClaims`, `AuthHealth`
- Exceptions avec garde anti-secret
- 30 tests, couverture ~98 %
- Matrice de compatibilité : core 0.4.1 GO, security/database contrat GO
- ADR-0001, US-001, FEAT-001.1 à 001.5

## Qualité locale

- black, ruff, mypy, bandit, pytest ≥ 95 % : OK
- traceability : OK
- build : OK

## Prochaine action

1. Pousser `version/v0.1.0` et ouvrir PR vers `main`
2. Attendre CI verte puis merge (Release manager)
3. Passer `version.yaml` à `INTEGRATION_PENDING` si validation git-ref requise
4. Démarrer v0.2.0 (client HTTP, validation JWT)
