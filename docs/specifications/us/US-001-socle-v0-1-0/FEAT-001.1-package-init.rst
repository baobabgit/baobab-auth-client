FEAT-001.1 — Initialiser le package
====================================

:Rattachée à: :ref:`us-001`
:Backlog: BL-001

Description
-----------

Créer le package ``baobab_auth_client`` installable avec métadonnées,
``py.typed`` et exports publics de base.

Critères d'acceptation
----------------------

#. ``pyproject.toml`` référence ``baobab-auth-client`` en version ``0.1.0``.
#. Le package expose ``__version__``.
#. Aucune dépendance interdite (SQLAlchemy, PostgreSQL, baobab-auth-security).
