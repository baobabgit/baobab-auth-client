# ADR-0001 — Socle client v0.1.0

## Statut

Accepté

## Contexte

``baobab-auth-client`` doit fournir une brique cliente réutilisable par les APIs
métier. La version ``v0.1.0`` pose le socle sans validation JWT réelle ni
dépendances FastAPI.

## Décision

1. **Modèles client dédiés** : ``AuthenticatedUser``, ``TokenClaims`` et
   ``TokenPair`` sont définis dans le client avec des types primitifs
   (``str``, ``tuple``) adaptés aux claims JWT, distincts des DTO du core
   (``UserId``, ``AuthSubject``, etc.).
2. **Dépendance unique** : ``baobab-auth-core>=0.4.0,<0.5.0`` pour valider les
   concepts métier ; pas de dépendance à ``baobab-auth-security`` en production.
3. **Configuration injectée** : ``AuthClientSettings`` via ``pydantic-settings``,
   préfixe ``BAOBAB_AUTH_CLIENT_``, sans état global.
4. **1 classe = 1 fichier** : modèles et configuration dans des modules dédiés ;
   exceptions regroupées par catégorie dans ``exceptions/``.

## Conséquences

- Les versions ultérieures mapperont les claims JWT vers les modèles client.
- La compatibilité avec le core est validée par des tests d'import contractuels.
- Aucune rupture du contrat public prévu avant ``v0.2.0``.
