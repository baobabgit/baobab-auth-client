US-001 — Socle du package v0.1.0
=================================

.. _us-001:

**ID :** US-001
**Version cible :** v0.1.0
**Priorité :** P0

Description
-----------

Poser le socle technique et contractuel de ``baobab-auth-client`` : configuration,
modèles publics, exceptions, documentation minimale et tests unitaires.

Critères d'acceptation
----------------------

#. Le package ``baobab_auth_client`` s'installe via ``pip install -e ".[dev]"``.
#. Les imports publics documentés fonctionnent.
#. La couverture de tests est ≥ 95 %.
#. La compatibilité avec ``baobab-auth-core`` 0.4.x est validée.

Features
--------

.. toctree::
   :maxdepth: 1

   FEAT-001.1-package-init
   FEAT-001.2-configuration
   FEAT-001.3-modeles-rbac
   FEAT-001.4-exceptions
   FEAT-001.5-documentation-tests
