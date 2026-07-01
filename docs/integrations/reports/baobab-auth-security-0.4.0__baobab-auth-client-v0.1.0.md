# Rapport d'intégration — baobab-auth-security 0.4.0 × baobab-auth-client v0.1.0

**Date :** 2026-07-01  
**Statut :** PASSED (contrat documenté)  
**Méthode :** PyPI — pas de dépendance runtime en v0.1.0

## Périmètre

- Claims JWT attendues documentées dans le cahier des charges v0.1.0
- Absence de dépendance directe à `baobab-auth-security` vérifiée par tests

## Résultat

Le client ne dépend pas de la brique security en production. Les claims
(`sub`, `sid`, `jti`, `roles`, `permissions`, `iss`, `aud`, `typ`) sont
alignées sur le contrat security/core.

## Écarts

Validation cryptographique réelle reportée à v0.2.0+.
