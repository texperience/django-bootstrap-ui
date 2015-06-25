Templates
=========

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
