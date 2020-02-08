Welcome to django-bootstrap-ui
==============================

.. image:: https://img.shields.io/travis/texperience/django-bootstrap-ui.svg?branch=master
    :target: https://travis-ci.org/texperience/django-bootstrap-ui

.. image:: https://img.shields.io/coveralls/texperience/django-bootstrap-ui/master.svg
    :target: https://coveralls.io/r/texperience/django-bootstrap-ui?branch=master

.. image:: https://img.shields.io/pypi/v/django-bootstrap-ui.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-ui

.. image:: https://img.shields.io/pypi/l/django-bootstrap-ui.svg
    :target: http://en.wikipedia.org/wiki/ISC_license

.. image:: https://readthedocs.org/projects/django-bootstrap-ui/badge/?version=stable
    :target: http://django-bootstrap-ui.readthedocs.org/stable/

django-bootstrap-ui aims to be a powerful Django app to ease the integration of the popular `Bootstrap UI framework`_. It is written in `Python`_ and built on the `Django web framework <https://www.djangoproject.com/>`_.

.. _Bootstrap UI framework: http://getbootstrap.com/
.. _Python: https://www.python.org/
.. _Django web framework: https://www.djangoproject.com/

Features
--------

* Basic HTML5 template (3.3.7)
* Full-featured Bootstrap 3 template (3.3.7)
* Latest Font Awesome integration (4.7.0)
* Built-in Bootstrap and `Bootswatch`_ themes (3.3.7)
* Extensive and up-to-date documentation
* Mainstream Python (3.6, 3.7, 3.8) and Django (2.2) support
* Outstanding test coverage
* Continuously integrated codebase

.. _Bootswatch: https://bootswatch.com/

Technical requirements
----------------------

Below is the list of currently supported combinations of Django and Python:

+---+--------+---------------+
| # | Django | Python        |
+===+========+===============+
| 1 | 2.2    | 3.6, 3.7, 3.8 |
+---+--------+---------------+

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

Continue reading in our `detailed documentation <https://django-bootstrap-ui.readthedocs.org>`_ at readthedocs.org.

Code and contribution
---------------------

The code is open source and released under the `ISC License (ISCL)`_. It is available on `GitHub`_ and follows the guidelines about `Semantic Versioning`_ for transparency within the release cycle and backward compatibility whenever possible.

All contributions are welcome, whether bug reports, code contributions and reviews, documentation or feature requests.

.. _ISC License (ISCL): http://en.wikipedia.org/wiki/ISC_license
.. _Semantic Versioning: http://semver.org/
.. _GitHub: https://github.com/texperience/django-bootstrap-ui
