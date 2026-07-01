# Cahier des charges — `baobab-auth-client` — version `v0.5.0`

**Projet :** `baobab-auth-client`  
**Version cible :** `v0.5.0`  
**Type de document :** cahier des charges complet et détaillé pour IA de développement  
**Format :** Markdown  
**Statut :** spécification de développement versionnée  
**Périmètre :** librairie Python cliente d’intégration au service `baobab-auth-api`  

---

## 1. Résumé de la version

**Titre :** Outils de test pour APIs consommatrices et contrats d’intégration

Fournir un module `testing` complet pour que les APIs métier puissent tester leurs routes protégées sans serveur auth réel. Cette version doit aussi formaliser les tests de contrat entre client, API, security et core.

---

## 2. Description générale de la librairie

`baobab-auth-client` est la librairie Python d’intégration destinée aux APIs consommatrices du service `baobab-auth-api`.
Elle valide les tokens JWT via JWKS, construit un utilisateur authentifié exploitable par les applications métier,
fournit des dépendances FastAPI et permet de contrôler localement rôles et permissions sans gérer la base de données,
les mots de passe, la génération des tokens ni la rotation des clés.

La librairie est utilisée par une API métier comme dépendance d’intégration. Elle permet à cette API de sécuriser ses routes sans réimplémenter la validation JWT, la récupération JWKS ou les contrôles de rôles et permissions.

Exemple cible :

```python
from fastapi import APIRouter, Depends
from baobab_auth_client.fastapi import require_user, require_permission
from baobab_auth_client.models import AuthenticatedUser

router = APIRouter()

@router.get("/me")
async def me(user: AuthenticatedUser = Depends(require_user)):
    return {"user_id": user.id}

@router.post("/admin/sync")
async def sync(
    user: AuthenticatedUser = Depends(require_permission("auth:session:revoke")),
):
    return {"status": "accepted"}
```

---

## 3. Positionnement dans l’écosystème `baobab-auth`

`baobab-auth-client` est la brique cliente consommée par les APIs métier.

```text
baobab-auth-core
        ↑
        │
baobab-auth-client
        ↑
        │
API métier consommatrice
```

Elle ne remplace pas :

- `baobab-auth-api`, qui expose les routes HTTP d’authentification ;
- `baobab-auth-security`, qui produit et valide techniquement les tokens côté auth ;
- `baobab-auth-database`, qui persiste les utilisateurs, rôles, sessions, clés et audits ;
- `baobab-auth-admin`, qui administre le système ;
- `baobab-auth-service`, qui assemble le service complet.

---

## 4. Versions des dépendances et librairies à valider

### 4.1 Dépendances directes ou optionnelles de cette version

| Librairie | Version à utiliser / valider | Rôle dans cette version |
|---|---:|---|
| `baobab-auth-core` | `>=0.4.0,<0.6.0` | Compatibilité élargie avec le core après stabilisation RBAC. |
| `fastapi` | `>=0.110,<1.0` | Tests d’intégration FastAPI. |
| `pytest` | `>=8,<9` | Extra `testing`. |
| `respx` | `>=0.21,<1.0` | Mock HTTP. |

### 4.2 Librairies `baobab-auth` à valider pour poursuivre les développements

| Librairie | Version à utiliser / valider | Rôle dans cette version |
|---|---:|---|
| `baobab-auth-api` | `0.4.0` | Contrats HTTP documentés et testables par fixtures. |
| `baobab-auth-security` | `0.3.0` | Contrats tokens/JWKS testables par fixtures cryptographiques. |
| `baobab-auth-core` | `0.4.0` | Validation des rôles système et permissions auth dans les fixtures. |
| `API consommatrice pilote` | `0.1.0` | Valider l’intégration dans une API métier exemple sans serveur auth réel. |

### 4.3 Règle de validation inter-briques

La validation de cette version doit produire un retour explicite dans le changelog et dans un fichier de compatibilité, par exemple :

```text
docs/integration-matrix.md
```

Ce fichier doit indiquer :

- la version de `baobab-auth-client` testée ;
- la version de chaque brique validée ;
- le type de validation réalisée : unit, contract, integration, e2e ;
- les endpoints ou contrats couverts ;
- les écarts éventuels ;
- le statut `GO` ou `NO GO`.

Une version de dépendance n’est considérée validée que si les tests associés sont automatisés et reproductibles.

---

## 5. Périmètre fonctionnel inclus dans `v0.5.0`

- Créer `testing/users.py`.
- Créer `testing/tokens.py`.
- Créer `testing/dependencies.py`.
- Créer des factories d’utilisateurs authentifiés.
- Créer des dépendances fake pour FastAPI.
- Créer des fixtures de rôles et permissions.
- Créer des helpers de mock JWKS et mock AuthClient.
- Créer des tests de contrat réutilisables.
- Documenter l’usage pour les APIs métier.

---

## 5.1 Hors périmètre de `v0.5.0`

- Génération de vrais JWT de production.
- Serveur auth embarqué.
- Base de données de test auth.


## 6. Contraintes transverses obligatoires

### 6.1 Contraintes d’architecture

La librairie doit rester une brique cliente.

Elle ne doit pas contenir :

- de modèle SQLAlchemy ;
- de migration Alembic ;
- de connexion PostgreSQL ;
- de hash de mot de passe ;
- de génération JWT ;
- de génération de refresh token ;
- de rotation de clés ;
- de serveur FastAPI complet ;
- de logique métier Riftbound, Altered ou autre application métier ;
- de dépendance directe à `baobab-auth-database` ;
- de dépendance directe à `baobab-auth-security` en production.

Elle peut consommer les contrats HTTP et JWKS exposés par `baobab-auth-api`.

### 6.2 Contraintes de sécurité

La librairie doit :

- refuser un token sans signature valide ;
- refuser un token expiré ;
- refuser un token dont l’algorithme n’est pas explicitement autorisé ;
- refuser un token dont le `kid` ne correspond à aucune clé JWKS valide ;
- rafraîchir le cache JWKS lorsqu’un `kid` inconnu est rencontré ;
- éviter les boucles de refresh JWKS en cas d’attaque par `kid` aléatoire ;
- ne jamais logger un mot de passe ;
- ne jamais logger un refresh token ;
- ne jamais logger un access token complet ;
- ne jamais exposer une clé privée ;
- ne jamais retourner de détail cryptographique sensible dans une exception HTTP.

### 6.3 Contraintes qualité

La librairie doit respecter :

- Python `>=3.11` ;
- packaging en structure `src/` ;
- typage strict ;
- fichier `py.typed` ;
- `ruff` pour lint et format ;
- `mypy` pour typage ;
- `pytest` pour tests ;
- `pytest-asyncio` pour tests async ;
- `pytest-cov` pour couverture ;
- `respx` ou équivalent pour mock `httpx` ;
- couverture minimale `>=90 %` dès les versions d’intégration ;
- documentation Markdown maintenue à chaque version.

### 6.4 Commandes de validation minimales

```bash
python -m pip install -e ".[dev,fastapi,http,jwt,testing]"
ruff check .
ruff format --check .
mypy src
pytest --cov=baobab_auth_client --cov-report=term-missing
```



## 7. Architecture cible du package

L’arborescence doit évoluer progressivement vers :

```text
baobab-auth-client/
├── pyproject.toml
├── README.md
├── CHANGELOG.md
├── LICENSE
├── src/
│   └── baobab_auth_client/
│       ├── __init__.py
│       ├── py.typed
│       ├── config.py
│       ├── exceptions.py
│       ├── models.py
│       ├── claims.py
│       ├── client/
│       │   ├── __init__.py
│       │   ├── async_client.py
│       │   ├── sync_client.py
│       │   ├── schemas.py
│       │   └── errors.py
│       ├── jwks/
│       │   ├── __init__.py
│       │   ├── cache.py
│       │   ├── fetcher.py
│       │   └── models.py
│       ├── tokens/
│       │   ├── __init__.py
│       │   ├── parser.py
│       │   ├── validator.py
│       │   └── algorithms.py
│       ├── permissions/
│       │   ├── __init__.py
│       │   ├── checker.py
│       │   └── policy.py
│       ├── fastapi/
│       │   ├── __init__.py
│       │   ├── dependencies.py
│       │   ├── security.py
│       │   └── errors.py
│       ├── starlette/
│       │   ├── __init__.py
│       │   └── middleware.py
│       ├── testing/
│       │   ├── __init__.py
│       │   ├── users.py
│       │   ├── tokens.py
│       │   └── dependencies.py
│       └── integrations/
│           ├── __init__.py
│           └── contract_tests.py
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── fastapi/
│   └── contract/
└── docs/
    ├── usage.md
    ├── configuration.md
    ├── fastapi.md
    ├── jwt-validation.md
    ├── jwks.md
    ├── testing.md
    ├── middleware.md
    └── integration-matrix.md
```


## 8. API publique attendue pour cette version

L’IA de développement doit maintenir une API publique cohérente avec le niveau de maturité de la version.

Exports recommandés lorsque le module correspondant est disponible :

```python
from baobab_auth_client.config import AuthClientSettings
from baobab_auth_client.models import AuthenticatedUser, TokenPair, TokenClaims, AuthHealth
from baobab_auth_client.exceptions import BaobabAuthClientError
```

À partir des versions concernées :

```python
from baobab_auth_client.client import AuthClient
from baobab_auth_client.tokens import TokenValidator
from baobab_auth_client.jwks import JwksCache, JwksFetcher
from baobab_auth_client.fastapi import require_user, require_role, require_permission
```

Règles :

- ne pas exposer d’API expérimentale sans documentation ;
- documenter toute dépréciation ;
- préserver les imports publics entre versions mineures sauf justification explicite ;
- ne jamais exporter de helper de test depuis l’API runtime principale.

---

## 9. Modules à développer ou modifier

### 9.1 `testing/users.py`

- Implémenter `make_authenticated_user`.
- Prévoir profils USER, ADMIN, SERVICE, SUPER_ADMIN.
- Permettre permissions applicatives comme `riftbound:collection:read`.

### 9.2 `testing/dependencies.py`

- Implémenter `fake_require_user`.
- Implémenter `fake_require_permission`.
- Documenter `app.dependency_overrides`.

### 9.3 `testing/tokens.py`

- Créer des claims factices.
- Créer des JWT de test si dépendance `jwt` présente.
- Ne jamais réutiliser ces helpers pour production.

### 9.4 `integrations/contract_tests.py`

- Définir une suite de contrats réutilisable.
- Tester forme JWKS, forme TokenPair, forme AuthenticatedUser.


---

## 10. Contrats fonctionnels détaillés

### 10.1 `AuthenticatedUser`

L’objet utilisateur authentifié représente l’identité validée côté API consommatrice.

Champs recommandés :

```python
@dataclass(frozen=True)
class AuthenticatedUser:
    id: str
    email: str | None
    username: str | None
    roles: tuple[str, ...]
    permissions: tuple[str, ...]
    session_id: str | None
    token_id: str | None
    issuer: str | None
    audience: str | tuple[str, ...] | None
    raw_claims: Mapping[str, Any]
```

Méthodes attendues :

```python
user.has_role("ADMIN")
user.has_any_role("ADMIN", "SUPER_ADMIN")
user.has_permission("auth:user:read")
user.has_any_permission("auth:user:read", "auth:user:write")
user.has_all_permissions("auth:user:read", "auth:user:write")
```

### 10.2 Claims JWT attendues

Les tokens compatibles doivent porter au minimum :

```json
{
  "sub": "auth_sub_xxx",
  "sid": "session_xxx",
  "jti": "token_xxx",
  "roles": ["USER"],
  "permissions": ["auth:user:read"],
  "iat": 1779999000,
  "exp": 1780000000,
  "iss": "baobab-auth",
  "aud": "api-consommatrice",
  "typ": "access"
}
```

Règles :

- `sub` représente l’identité publique stable (`AuthSubject`) ;
- `jti` représente l’identifiant unique du token ;
- `sid` représente la session si disponible ;
- `roles` et `permissions` sont transportés, jamais recalculés par le client ;
- le client ne doit pas coder le mapping rôle → permissions ;
- les permissions applicatives comme `riftbound:collection:read` doivent être acceptées si elles respectent le format.

### 10.3 Endpoint JWKS attendu

```http
GET /auth/jwks
```

Réponse compatible :

```json
{
  "keys": [
    {
      "kty": "RSA",
      "kid": "key-id",
      "use": "sig",
      "alg": "RS256",
      "n": "...",
      "e": "..."
    }
  ]
}
```

### 10.4 Endpoints API auth attendus

Selon le niveau de version :

```http
POST /auth/login
POST /auth/logout
POST /auth/refresh
GET  /auth/me
GET  /auth/jwks
GET  /health
```

Endpoints optionnels :

```http
POST /auth/register
GET  /auth/roles
POST /auth/introspect
```

Le client doit rester robuste lorsqu’un endpoint optionnel n’est pas disponible, à condition que la fonctionnalité correspondante soit explicitement désactivée.

---

## 11. Tests obligatoires

### 11.1 Tests spécifiques de cette version

- `test_make_authenticated_user_default_user`
- `test_make_admin_user`
- `test_fake_require_user_dependency_override`
- `test_fake_require_permission_success`
- `test_fake_require_permission_forbidden`
- `test_mock_jwks_contract`
- `test_contract_token_pair_shape`
- `test_contract_authenticated_user_shape`

### 11.2 Tests transverses

À chaque version, conserver ou ajouter :

- tests d’import public ;
- tests d’absence de dépendance SQLAlchemy/PostgreSQL ;
- tests anti-secret dans exceptions ;
- tests anti-secret dans logs ;
- tests de typage ;
- tests de documentation minimale si exemples exécutables ;
- tests de compatibilité avec la version de `baobab-auth-core` indiquée.

### 11.3 Couverture

Objectifs :

```text
v0.1.0 à v0.4.0 : coverage >= 90 %
v0.5.0 à v0.9.0 : coverage >= 92 %
v1.0.0          : coverage >= 95 % recommandé
```

---

## 12. Documentation attendue

La version doit mettre à jour :

```text
README.md
CHANGELOG.md
docs/usage.md
docs/configuration.md
docs/integration-matrix.md
```

Selon le périmètre de la version, compléter aussi :

```text
docs/fastapi.md
docs/jwt-validation.md
docs/jwks.md
docs/testing.md
docs/middleware.md
docs/security.md
```

Le changelog doit contenir :

- version ;
- date ;
- fonctionnalités ajoutées ;
- corrections ;
- changements de compatibilité ;
- versions des briques validées ;
- statut d’intégration.

---

## 13. Backlog détaillé

### BL-C-021 — Créer module testing utilisateurs.

**Objectif :** implémenter ce lot en conservant une librairie typée, testée et documentée.

**Actions minimales :**

- créer ou modifier les modules nécessaires ;
- ajouter ou adapter les tests unitaires ;
- vérifier `ruff`, `mypy`, `pytest` ;
- mettre à jour la documentation et le changelog ;
- ne pas introduire de dépendance hors périmètre.

**Critères d’acceptation :**

- le comportement attendu est couvert par tests ;
- aucune fuite de secret n’est possible dans logs, exceptions ou représentations ;
- la compatibilité inter-briques indiquée dans ce cahier des charges est validée.

### BL-C-022 — Créer module testing dépendances FastAPI.

**Objectif :** implémenter ce lot en conservant une librairie typée, testée et documentée.

**Actions minimales :**

- créer ou modifier les modules nécessaires ;
- ajouter ou adapter les tests unitaires ;
- vérifier `ruff`, `mypy`, `pytest` ;
- mettre à jour la documentation et le changelog ;
- ne pas introduire de dépendance hors périmètre.

**Critères d’acceptation :**

- le comportement attendu est couvert par tests ;
- aucune fuite de secret n’est possible dans logs, exceptions ou représentations ;
- la compatibilité inter-briques indiquée dans ce cahier des charges est validée.

### BL-C-023 — Créer fixtures JWKS/tokens de test.

**Objectif :** implémenter ce lot en conservant une librairie typée, testée et documentée.

**Actions minimales :**

- créer ou modifier les modules nécessaires ;
- ajouter ou adapter les tests unitaires ;
- vérifier `ruff`, `mypy`, `pytest` ;
- mettre à jour la documentation et le changelog ;
- ne pas introduire de dépendance hors périmètre.

**Critères d’acceptation :**

- le comportement attendu est couvert par tests ;
- aucune fuite de secret n’est possible dans logs, exceptions ou représentations ;
- la compatibilité inter-briques indiquée dans ce cahier des charges est validée.

### BL-C-024 — Créer tests de contrat inter-briques.

**Objectif :** implémenter ce lot en conservant une librairie typée, testée et documentée.

**Actions minimales :**

- créer ou modifier les modules nécessaires ;
- ajouter ou adapter les tests unitaires ;
- vérifier `ruff`, `mypy`, `pytest` ;
- mettre à jour la documentation et le changelog ;
- ne pas introduire de dépendance hors périmètre.

**Critères d’acceptation :**

- le comportement attendu est couvert par tests ;
- aucune fuite de secret n’est possible dans logs, exceptions ou représentations ;
- la compatibilité inter-briques indiquée dans ce cahier des charges est validée.

### BL-C-025 — Documenter intégration dans une API métier pilote.

**Objectif :** implémenter ce lot en conservant une librairie typée, testée et documentée.

**Actions minimales :**

- créer ou modifier les modules nécessaires ;
- ajouter ou adapter les tests unitaires ;
- vérifier `ruff`, `mypy`, `pytest` ;
- mettre à jour la documentation et le changelog ;
- ne pas introduire de dépendance hors périmètre.

**Critères d’acceptation :**

- le comportement attendu est couvert par tests ;
- aucune fuite de secret n’est possible dans logs, exceptions ou représentations ;
- la compatibilité inter-briques indiquée dans ce cahier des charges est validée.


---

## 14. Critères d’acceptation de la version `v0.5.0`

La version est validée si :

- le package s’installe avec `pip install -e ".[dev]"` ;
- les extras concernés s’installent correctement ;
- les imports publics documentés fonctionnent ;
- les modules prévus dans ce cahier des charges sont implémentés ;
- les tests spécifiques de cette version passent ;
- les tests de non-régression des versions précédentes passent ;
- la couverture minimale est atteinte ;
- `ruff check .` passe ;
- `ruff format --check .` passe ;
- `mypy src` passe ;
- aucune dépendance interdite n’est ajoutée ;
- aucune fuite de secret n’est détectée dans logs, exceptions ou représentations ;
- la documentation de la version est à jour ;
- `docs/integration-matrix.md` indique les versions validées ;
- le changelog indique clairement le statut `GO` ou `NO GO`.

---

## 15. Validation d’intégration et poursuite des autres librairies

Après validation de `v0.5.0`, les projets consommateurs peuvent tester leurs routes protégées sans attendre un déploiement complet. Les contrats `baobab-auth-api v0.4.0` et `baobab-auth-security v0.3.0` sont figés pour les tests d’intégration.

L’IA de développement doit produire en fin de version un résumé d’intégration au format :

```markdown
## Résultat d’intégration v0.5.0

| Librairie | Version testée | Statut | Commentaire |
|---|---:|---|---|
| baobab-auth-core | ... | GO/NO GO | ... |
| baobab-auth-api | ... | GO/NO GO | ... |
| baobab-auth-security | ... | GO/NO GO | ... |
```

Si le statut est `NO GO`, l’IA doit ouvrir ou documenter un backlog correctif dans la librairie responsable.

---

## 16. Définition de terminé

La version `v0.5.0` est terminée lorsque :

1. tous les backlogs de ce fichier sont implémentés ;
2. tous les tests sont automatisés ;
3. les versions dépendantes indiquées sont validées ;
4. les écarts sont documentés ;
5. le changelog est prêt ;
6. la documentation est complète ;
7. un tag Git `v0.5.0` peut être créé ;
8. la publication PyPI peut être préparée si la stratégie de release le prévoit.

---

## 17. Recommandation finale pour l’IA de développement

Traiter ce cahier des charges comme contractuel pour `baobab-auth-client v0.5.0`.

Priorité d’implémentation :

```text
1. garantir la compatibilité avec les versions dépendantes indiquées ;
2. maintenir la sécurité par défaut ;
3. couvrir le comportement par tests ;
4. documenter l’usage pour les APIs consommatrices ;
5. préserver l’API publique existante ;
6. signaler tout écart bloquant par un statut NO GO.
```
