FEAT-001.4 — Exceptions et anti-secret
=======================================

:Rattachée à: :ref:`us-001`
:Backlog: BL-004

Description
-----------

Créer la hiérarchie d'exceptions sans dépendance FastAPI ni fuite de secret.

Critères d'acceptation
----------------------

#. ``BaobabAuthClientError`` est la racine.
#. Exceptions spécialisées : configuration, API, token, JWKS, autorisation.
#. Aucun message d'exception ne contient de token complet.
