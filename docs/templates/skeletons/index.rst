Page skeleton templates
=======================

Prepare your page for Bootstrap and provide your content.

HTML5 skeleton
--------------

This is our root template (``html5-skeleton.html``) with a minimalistic and clean HTML5 skeleton. It comes with a well-thought-out block structure as follows, but is not meant to be extended directly. Extend the `Bootstrap skeleton`_ instead.

head-meta
*********

Provide additional meta tags within the ``<head>``. Example:

.. code:: Django

    {% block head-meta %}
        <meta name="keywords" content="wood, furniture, garden, garden-table, etc.">
    {% endblock %}

head-title
**********

Provide your content for ``<title>``. Example:

.. code:: Django

    {% block head-title %}
        Your title
    {% endblock %}

head-css
********

Provide additional ``<link>`` tags with css references. Example:

.. code:: Django

    {% block head-css %}
        <link href="css/your-theme.css" media="screen" rel="stylesheet" type="text/css">
    {% endblock %}

head-javascript
***************

Provide additional ``<script>`` tags with javascript source references or inline code. Example:

.. code:: Django

    {% block head-javascript %}
        <script src="js/your-script.js" type="text/javascript"></script>
    {% endblock %}

head-extension
**************

Provide other content within the ``<head>``. Example:

.. code:: Django

    {% block head-extension %}
        Whatever content you need at the end of the head.
    {% endblock %}

body-content
************

All your page content in ``<body>``. Example:

.. code:: Django

    {% block body-content %}
        <h1>Hello, django-bootstrap-ui!</h1>
    {% endblock %}

body-javascript
***************

Provide additional ``<script>`` tags with javascript source references or inline code just before ``<body>`` ends. Example:

.. code:: Django

    {% block body-javascript %}
        <script src="js/your-lately-embedded-script.js" type="text/javascript"></script>
    {% endblock %}

Bootstrap skeleton
------------------

This template (``bootstrap-skeleton.html``) extends our `HTML5 skeleton`_ and provides Bootstrap support. Extend this to get a working, bootstraped page layout.

.. code:: Django

    {% extends "bootstrap_ui/bootstrap-skeleton.html" %}

There are no additional blocks besides the above, the following ones are sensibly used by this template:

* head-meta
* head-css
* head-javascript
* body-javascript

Be careful when you are going to use these blocks with your own stuff. Remember to apply ``{{ block.super }}`` so you won't overwrite existing and necessary Bootstrap resources. Example:

.. code:: Django

    {% block head-meta %}
        {{ block.super }}

        <!-- Page description -->
        <meta name="description" content="This is your page description." />
    {% endblock %}

Apply themes
************

By default the standard, plain Bootstrap style is applied. But in addition, this template is ready to include Bootstrap and Bootswatch themes. You can change this behavior in two ways, they may be used together:

#. Set ``DJANGO_BOOTSTRAP_UI_THEME`` to a valid identifier in your ``settings.py`` for a project-wide default theme:

    .. code:: python

        # django-bootstrap-ui settings
        DJANGO_BOOTSTRAP_UI_THEME = 'bootswatch-paper'

#. Set ``DJANGO_BOOTSTRAP_UI_THEME`` to a valid identifier in your user's session or cookie using the :doc:`set_theme <../../views/index>` view.

The following table lists currently available themes:

=============  ====================  ===========
Name           Identifier            Provided by
=============  ====================  ===========
Example theme  bootstrap             Bootstrap
Cerulean       bootswatch-cerulean   Bootswatch
Cosmo          bootswatch-cosmo      Bootswatch
Cyborg         bootswatch-cyborg     Bootswatch
Darkly         bootswatch-darkly     Bootswatch
Flatly         bootswatch-flatly     Bootswatch
Journal        bootswatch-journal    Bootswatch
Lumen          bootswatch-lumen      Bootswatch
Paper          bootswatch-paper      Bootswatch
Readable       bootswatch-readable   Bootswatch
Sandstone      bootswatch-sandstone  Bootswatch
Simplex        bootswatch-simplex    Bootswatch
Slate          bootswatch-slate      Bootswatch
Spacelab       bootswatch-spacelab   Bootswatch
Superhero      bootswatch-superhero  Bootswatch
United         bootswatch-united     Bootswatch
Yeti           bootswatch-yeti       Bootswatch

All other values will be ignored and default to the standard, plain Bootstrap style.
