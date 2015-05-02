===================
django-bootstrap-ui
===================

This aims to be a powerful Django app to ease the integration of the
popular Bootstrap UI framework (http://getbootstrap.com).

.. image:: https://img.shields.io/travis/timorieber/django-bootstrap-ui.svg
    :target: https://travis-ci.org/timorieber/django-bootstrap-ui

.. image:: https://img.shields.io/coveralls/timorieber/django-bootstrap-ui/master.svg
    :target: https://coveralls.io/r/timorieber/django-bootstrap-ui?branch=master

.. image:: https://img.shields.io/pypi/v/django-bootstrap-ui.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-ui

.. image:: https://img.shields.io/pypi/l/django-bootstrap-ui.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-ui

Quick start
-----------

1. Add ``bootstrap_ui`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'bootstrap_ui',
        ...
    )

2. Load ``bootstrap_ui_tags`` in your template::

    {% load bootstrap_ui_tags %}

3. Use bootstrap components through intuitive template tags::

    {% listgroup %}
        {% listgroupitem %}
            Your raw text.
        {% endlistgroupitem %}
        {% listgroupitem %}
            You may also use a {{ context_variable }}.
        {% endlistgroupitem %}
    {% endlistgroup %}

4. Some bootstrap components support different html tags, to change the default add a parameter::

    {% listgroup use_tag="div" %}
        ...
        Your list group content goes here.
        ...
    {% endlistgroup %}

Supported bootstrap components
------------------------------

* List group (http://getbootstrap.com/components/#list-group)