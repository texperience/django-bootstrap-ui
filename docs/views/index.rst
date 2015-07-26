Views
=====

django-bootstrap-ui comes with predefined views and corresponding urls that get you right on the track.

Setting the bootstrap theme
---------------------------

The ``set_theme`` view
**********************

Use the ``set_theme`` view to change the style of the page on a per-user basis. ``set_theme``

#. determines the page to redirect to after execution in the following manner:
    #. checks the ``next`` parameter from ``request.POST`` for a valid url
    #. checks the ``next`` parameter from ``request.GET`` for a valid url
    #. checks the ``HTTP_REFERER`` value in ``request.META`` for a valid url
    #. falls back to ``/``

#. sets the theme using the ``theme`` parameter from ``request.POST`` as ``DJANGO_BOOTSTRAP_UI_THEME`` in:
    #. the user's session if available
    #. the user's cookie

#. redirects to the evaluated page

Since this view changes how the user will see the rest of the site, it must only be accessed as a ``POST`` request. If called as a ``GET`` request, it will redirect to the page in the request (the ``next`` parameter) without changing any state.

The ``set_theme`` url
*********************

A named url ``set_theme`` to the above view is available within our ``urls.py``, so you may easily include this route in your project like this:

.. code:: python

    from django.conf.urls import patterns, include, url

    urlpatterns = patterns("",
        ...
        url(r"^bootstrap_ui/", include("bootstrap_ui.urls")),
        ...
    )

Then use this url to provide the ``action`` attribute for your form:

.. code:: Django

    <form method="post" action="{% url 'set_theme' %}">
        {% csrf_token %}
        <input type="text" name="next" value="/redirect-to-this-page"/>
        <input type="text" name="theme" value="bootstrap"/>
        <button type="submit">Go!</button>
    </form>

See :doc:`Apply themes <../templates/skeletons/index>` for valid theme identifiers.
