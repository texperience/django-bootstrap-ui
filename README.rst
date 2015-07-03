Welcome to django-bootstrap-ui
==============================

.. image:: https://img.shields.io/travis/timorieber/django-bootstrap-ui.svg
    :target: https://travis-ci.org/timorieber/django-bootstrap-ui

.. image:: https://img.shields.io/coveralls/timorieber/django-bootstrap-ui/master.svg
    :target: https://coveralls.io/r/timorieber/django-bootstrap-ui?branch=master

.. image:: https://img.shields.io/pypi/v/django-bootstrap-ui.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-ui

.. image:: https://img.shields.io/pypi/l/django-bootstrap-ui.svg
    :target: http://en.wikipedia.org/wiki/ISC_license

.. image:: https://readthedocs.org/projects/django-bootstrap-ui/badge/
    :target: https://django-bootstrap-ui.readthedocs.org

django-bootstrap-ui aims to be a powerful Django app to ease the integration of the popular `Bootstrap UI framework`_. It is written in `Python`_ and built on the `Django web framework <https://www.djangoproject.com/>`_.

The code is open source and released under the `ISC License (ISCL)`_. It is available on `GitHub`_ and follows the guidelines about `Semantic Versioning`_ for transparency within the release cycle and backward compatibility whenever possible.

.. _Bootstrap UI framework: http://getbootstrap.com/
.. _Python: https://www.python.org/
.. _Django web framework: https://www.djangoproject.com/
.. _ISC License (ISCL): http://en.wikipedia.org/wiki/ISC_license
.. _Semantic Versioning: http://semver.org/
.. _GitHub: https://github.com/timorieber/django-bootstrap-ui

Features
--------

* Full-featured Bootstrap 3 template (3.3.5)
* Latest Font Awesome integration (4.3.0)
* Ready-to-use Bootstrap component templates
* Intuitive template tag API for generating valid Bootstrap markup
* Extensive and up-to-date documentation
* Mainstream Python (2.7, 3.3, 3.4) and Django (1.7, 1.8) support
* Outstanding `test coverage <https://coveralls.io/r/timorieber/django-bootstrap-ui?branch=master>`_
* Continuously integrated codebase

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

Continue reading in our `detailed documentation <https://django-bootstrap-ui.readthedocs.org>`_ at readthedocs.org.
