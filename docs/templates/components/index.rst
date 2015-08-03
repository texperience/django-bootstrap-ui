Bootstrap component templates
=============================

Render complete Bootstrap components by including our default implementations.

List group
----------

This template (``listgroup.html``) renders a list group. Two parameters are required:

* type
* items

Basic example
*************

Given a list of strings ``['alpha', 'beta', 'gamma']`` as template variable ``items``:

.. code:: Django

    {% include 'bootstrap_ui/listgroup.html' with type='list' items=items only %}

This renders the following html code:

.. code:: HTML

    <ul class="list-group">
        <li class="list-group-item">
            alpha
        </li>
        <li class="list-group-item">
            beta
        </li>
        <li class="list-group-item">
            gamma
        </li>
    </ul>

Button items
************

Given a list of strings ``['alpha', 'beta', 'gamma']`` as template variable ``items``:

.. code:: Django

    {% include 'bootstrap_ui/listgroup.html' with type='buttonlist' items=items only %}

This renders the following html code:

.. code:: HTML

    <div class="list-group">
        <button class="list-group-item" type="button">
            alpha
        </button>
        <button class="list-group-item" type="button">
            beta
        </button>
        <button class="list-group-item" type="button">
            gamma
        </button>
    </div>

Linked items
************

Given a list of 2-tuples containing ``[('alpha', 'http://example.org'), ('beta', 'local.html'), ('gamma', '#')]`` as template variable ``items``:

.. code:: Django

    {% include 'bootstrap_ui/listgroup.html' with type='linklist' items=items only %}

This renders the following html code:

.. code:: HTML

    <div class="list-group">
        <a class="list-group-item" href="http://example.org">
            alpha
        </a>
        <a class="list-group-item" href="local.html">
            beta
        </a>
        <a class="list-group-item" href="#">
            gamma
        </a>
    </div>
