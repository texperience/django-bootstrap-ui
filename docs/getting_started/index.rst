Getting started
===============

Installation
------------

#. First install the package using ``pip`` with the ``--pre`` option as long as this is a pre-release::

    pip install --pre django-bootstrap-ui

#. Add ``bootstrap_ui`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'bootstrap_ui',
        ...
    )

Usage
-----

#. Load ``bootstrap_ui_tags`` in your template::

    {% load bootstrap_ui_tags %}

#. Use bootstrap components through intuitive template tags::

    {% listgroup %}
        {% listgroupitem %}
            Your raw text.
        {% endlistgroupitem %}
        {% listgroupitem %}
            You may also use a {{ context_variable }}.
        {% endlistgroupitem %}
    {% endlistgroup %}

#. Some bootstrap components support different html tags, to change the default add a parameter::

    {% listgroup use_tag="div" %}
        ...
        Your list group content goes here.
        ...
    {% endlistgroup %}
