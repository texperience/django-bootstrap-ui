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

Bootstrap template
******************

Prepare your page for Bootstrap and provide your content:

#. Extend ``bootstrap-skeleton.html`` in your base template:

    .. code:: Django

        {% extends "bootstrap_ui/bootstrap-skeleton.html" %}

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

See :doc:`../templates/skeletons/index` for more details.

Bootstrap component templates
*****************************

Render complete Bootstrap components by including our default implementations. Example:

#. Provide a list of strings ``['alpha', 'beta', 'gamma']`` as template variable ``items``

#. Include ``listgroup.html`` parameterized with ``type='list'`` and ``items=items``:

    .. code:: Django

        {% include 'bootstrap_ui/listgroup.html' with type='list' items=items only %}

Template tag API
****************

Generate your own, customized Bootstrap elements using our template tags. Example:

#. Load ``bootstrap_ui_tags`` in your template:

    .. code:: Django

        {% load bootstrap_ui_tags %}

#. Use Bootstrap components through intuitive template tags:

    .. code:: Django

        {% listgroup %}
            {% listgroupitem %}
                Your raw text.
            {% endlistgroupitem %}
            {% listgroupitem %}
                You may also use a {{ context_variable }}.
            {% endlistgroupitem %}
        {% endlistgroup %}

#. Some Bootstrap components support different html tags, to change the default add a parameter:

    .. code:: Django

        {% listgroup use_tag="div" %}
            ...
            Your list group content goes here.
            ...
        {% endlistgroup %}
