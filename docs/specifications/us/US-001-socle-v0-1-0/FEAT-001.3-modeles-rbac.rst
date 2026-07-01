FEAT-001.3 — Modèles publics et RBAC local
===========================================

:Rattachée à: :ref:`us-001`
:Backlog: BL-003

Description
-----------

Implémenter ``AuthenticatedUser``, ``TokenPair``, ``TokenClaims`` et
``AuthHealth`` avec helpers de rôles et permissions.

Critères d'acceptation
----------------------

#. ``AuthenticatedUser`` est immuable.
#. Les méthodes ``has_role``, ``has_permission`` et variantes fonctionnent.
#. ``TokenPair`` masque les tokens dans ``__repr__``.
