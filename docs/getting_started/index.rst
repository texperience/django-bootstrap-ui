Getting started
===============

Installation
------------

#. First install the package using ``pip`` with the ``--pre`` option as long as this is a pre-release:

    .. code:: bash

        pip install --pre django-bootstrap-ui

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
