# Rapport d'intégration — baobab-auth-core 0.4.1 × baobab-auth-client v0.1.0

**Date :** 2026-07-01  
**Statut :** PASSED  
**Méthode :** PyPI (`baobab-auth-core>=0.4.0,<0.5.0`)

## Périmètre

- Import de `AuthSubject`, `RoleName`, `PermissionName`
- Import des DTO `AuthenticatedUser`, `TokenClaims`, `TokenPair` du core
- Tests contractuels : `tests/contracts/test_core_compatibility.py`

## Résultat

Tous les imports et instanciations de base passent. Les modèles client restent
distincts (types primitifs) conformément à ADR-0001.

## Écarts

Aucun écart bloquant.
