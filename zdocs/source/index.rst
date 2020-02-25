.. islelib documentation master file, created by
   sphinx-quickstart on Mon Oct  1 00:18:03 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

IsleService Objects
===================

Template for creating models, schemas and errors for services, then installed for use in
client apps and companion services.

This template is built off of `islelib`_ and shares it's same tool suite.

Development Guide
=================

Each objects package for a service should contain the following sub-packages:

   * *models*: Dataclass models for schema generation through `grahamcracker`_
   * schemas*: Any schemas which require custom implementation. Should always inherit
     from ``grahamcracker.DataSchema`` and be generated using the
     ``grahamcracker.schema_for`` decorator to tie it to a dataclass model
   * *fields*: ``marshmallow.fields.Field`` implementations required by the schemas.
   * *errors*: All errors should inherit from ``spanreed.APIError``

A few development notes:

   * The purpose of having a separate package for these objects is that they can be
     shared between the service itself and other client applications / services. In some
     cases it may make sense to have one objects module contain the models / errors /
     schemas for a group of microservices.

   * The default pipeline is set up to test on Mac, Windows, and PC -- unlike
     `isleservice`_, which by default only tests on Linux.

Models
======

.. automodule:: isleservice_objects.models
   :members:

Schemas
=======

.. automodule:: isleservice_objects.schemas
   :members:

Exceptions
==========

.. automodule:: isleservice_objects.errors
   :members:


.. _islelib: https://illuscio-islelib-py.readthedocs-hosted.com/en/latest/
