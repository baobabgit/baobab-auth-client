FEAT-001.2 — Configuration injectable
======================================

:Rattachée à: :ref:`us-001`
:Backlog: BL-002

Description
-----------

Implémenter ``AuthClientSettings`` immuable via ``pydantic-settings``.

Critères d'acceptation
----------------------

#. Chargement depuis l'environnement via ``from_env()``.
#. Construction automatique de ``jwks_url`` depuis ``auth_base_url``.
#. Rejet d'une ``auth_base_url`` vide.
