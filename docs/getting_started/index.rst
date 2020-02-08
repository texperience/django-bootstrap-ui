Getting started
===============

Installation
------------

#. First install the package using ``pip``:

    .. code:: bash

        pip install django-bootstrap-ui

#. Add ``bootstrap_ui`` to your ``INSTALLED_APPS`` setting:

    .. code:: python

        INSTALLED_APPS = (
            ...
            'bootstrap_ui',
            ...
        )

Usage
-----

Bootstrap 3 template
********************

Prepare your page for Bootstrap 3 and provide your content:

#. Extend ``bootstrap3-skeleton.html`` in your base template:

    .. code:: Django

        {% extends "bootstrap_ui/bootstrap3-skeleton.html" %}

#. Fill predefined blocks with your content:

    .. code:: Django

        {% block body-content %}
            <h1>Hello, I'm using django-bootstrap-ui!</h1>
        {% endblock %}

Themes
******

You can style your page with Bootstrap or Bootswatch themes. Set ``DJANGO_BOOTSTRAP_UI_THEME`` to a valid identifier in your ``settings.py`` for a project-wide default theme:

.. code:: python

    # django-bootstrap-ui settings
    DJANGO_BOOTSTRAP_UI_THEME = 'bootswatch-paper'

See :doc:`../templates/index` for more details.
