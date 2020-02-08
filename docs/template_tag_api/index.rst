Template tag API
================

Some utilities and helper tags to make your and our lifes easier.

get_value_from_session_or_cookie
--------------------------------

Returns a value for a given key from a user's session or cookie with fallback to global settings:

#. Check ``request.session`` for ``key``
#. Check ``request.COOKIES`` for ``key``
#. Check ``settings.py`` for ``key``
#. Fall back to ``''``

This tag is implemented as an assignment tag. Usage:

.. code:: Django

    {% load bootstrap_ui_tags %}

    {% get_value_from_session_or_cookie 'DJANGO_BOOTSTRAP_UI_THEME' as theme %}
    ...
