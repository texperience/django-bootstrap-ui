Bootstrap components API
========================

Generate your own, customized Bootstrap elements using these template tags.

Grid system
-----------

See http://getbootstrap.com/css/#grid.

Container
*********

Use the ``container`` tag to house a fixed-width bootstrap grid system:

.. code:: Django

    {% container %}
        ...
    {% endcontainer %}

This renders the following html code:

.. code:: HTML

    <div class="container">
        ...
    </div>

Provide ``type="fluid"`` as parameter for a full-width container housing your grid:

.. code:: Django

    {% container type="fluid" %}
        ...
    {% endcontainer %}

This renders the following html code:

.. code:: HTML

    <div class="container-fluid">
        ...
    </div>

Row
***

Use ``row`` to create horizontal groups of columns within containers:

.. code:: Django

    {% row %}
        ...
    {% endrow %}

This renders the following html code:

.. code:: HTML

    <div class="row">
        ...
    </div>

Remember that according to the bootstrap rules only columns may be immediate children of rows.

Column
******

Basic example
+++++++++++++

Place ``column`` within rows to span a certain width of your row:

.. code:: Django

    {% column %}
        Lorem ipsum. Your content goes here!
    {% endcolumn %}

This renders the following html code:

.. code:: HTML

    <div class="col-xs-12">
        Lorem ipsum. Your content goes here!
    </div>

As bootstrap is a mobile first framework grid classes are applied to devices with screen widths greater than or equal to the breakpoint sizes. Therefore ``column`` used without parameters applies a ``col-xs-12`` css class.

Custom column width and larger devices
++++++++++++++++++++++++++++++++++++++

Provide ``xs``, ``sm``, ``md`` and/or ``lg`` parameters to change the column span and address larger viewports:

.. code:: Django

    {% column xs="8" sm="6" md="4" lg="3" %}
        Lorem ipsum. Your content goes here!
    {% endcolumn %}

This renders the following html code:

.. code:: HTML

    <div class="col-xs-8 col-sm-6 col-md-4 col-lg-3">
        Lorem ipsum. Your content goes here!
    </div>

Every individual parameter may be omitted, you can use any combination of them.

List group
----------

See http://getbootstrap.com/components/#list-group.

Basic example
*************

Use the ``listgroup`` tag with nested ``listgroupitem`` tags:

.. code:: Django

    {% listgroup %}
        {% listgroupitem %}
            Your raw text.
        {% endlistgroupitem %}
        {% listgroupitem %}
            You may also use a {{ context_variable }}.
        {% endlistgroupitem %}
    {% endlistgroup %}

This renders the following html code:

.. code:: HTML

    <ul class="list-group">
        <li class="list-group-item">
            Your raw text.
        </li>
        <li class="list-group-item">
            You may also use a context variable.
        </li>
    </ul>

Linked items
************

Provide ``use_tag`` and ``link`` parameters to get linked items:

.. code:: Django

    {% listgroup use_tag="div" %}
        {% listgroupitem use_tag="a" link="http://example.org" %}
            External link to {{ ext_page_title }}.
        {% endlistgroupitem %}
        {% listgroupitem use_tag="a" link=local_reference %}
            Internal link to {{ your_page_title }}. Note how the link is provided as a context variable.
        {% endlistgroupitem %}
    {% endlistgroup %}

This renders the following html code:

.. code:: HTML

    <div class="list-group">
        <a class="list-group-item" href="http://example.org">
            External link to Example.
        </a>
        <a class="list-group-item" href="your_local_link">
            Internal link to awesame internal page. Note how the link is provided as a context variable.
        </a>
    </div>

Disabled items
**************

Provide ``add_css_classes`` parameter for ``listgroupitem``:

.. code:: Django

    {% listgroup use_tag="div" %}
        {% listgroupitem use_tag="a" link="http://example.org" add_css_classes="disabled" %}
            External link to {{ ext_page_title }}, but in disabled state.
        {% endlistgroupitem %}
        {% listgroupitem use_tag="a" link=local_reference %}
            Internal link to {{ your_page_title }}. This one is enabled.
        {% endlistgroupitem %}
    {% endlistgroup %}

This renders the following html code:

.. code:: HTML

    <div class="list-group">
        <a class="list-group-item disabled" href="http://example.org">
            External link to Example, but in disabled state.
        </a>
        <a class="list-group-item" href="your_local_link">
            Internal link to awesame internal page.  This one is enabled.
        </a>
    </div>

Contextual classes
******************

Provide valid bootstrap class names to ``add_css_classes`` parameter for ``listgroupitem``:

.. code:: Django

    {% listgroup %}
        {% listgroupitem add_css_classes="list-group-item-success" %}
            Your success text.
        {% endlistgroupitem %}
        {% listgroupitem add_css_classes="list-group-item-info" %}
            Your info text.
        {% endlistgroupitem %}
        {% listgroupitem add_css_classes="list-group-item-warning" %}
            Your warning text.
        {% endlistgroupitem %}
        {% listgroupitem add_css_classes="list-group-item-danger" %}
            Your danger text.
        {% endlistgroupitem %}
    {% endlistgroup %}

This renders the following html code:

.. code:: HTML

    <ul class="list-group">
        <li class="list-group-item list-group-item-success">
            Your success text.
        </li>
        <li class="list-group-item list-group-item-info">
            Your info text.
        </li>
        <li class="list-group-item list-group-item-warning">
            Your warning text.
        </li>
        <li class="list-group-item list-group-item-danger">
            Your danger text.
        </li>
    </ul>

Custom content
**************

You may also render custom html content within your ``list-group-item``:

.. code:: Django

    {% listgroup use_tag="div" %}
        {% listgroupitem use_tag="div" %}
            <h2>A custom title</h2>
            <p>With a custom paragraph.</p>
        {% endlistgroupitem %}
    {% endlistgroup %}

This renders the following html code:

.. code:: HTML

    <div class="list-group">
        <div class="list-group-item">
            <h2>A custom title</h2>
            <p>With a custom paragraph.</p>
        </div>
    </div>

Panels
------

See http://getbootstrap.com/components/#panels.

Basic example
*************

Use the ``panel`` in a simple way:

.. code:: Django

    {% panel %}
        {% panelbody %}
            Lorem ipsum.
        {% endpanelbody %}
    {% endpanel %}

This renders the following html code:

.. code:: HTML

    <div class="panel panel-default">
        <div class="panel-body">
            Lorem ipsum.
        </div>
    </div>

Panel with heading
******************

Add a nested ``panel-heading``:

.. code:: Django

    {% panel %}
        {% panelheading %}
            Your panel heading
        {% endpanelheading %}
        {% panelbody %}
            Lorem ipsum.
        {% endpanelbody %}
    {% endpanel %}

This renders the following html code:

.. code:: HTML

    <div class="panel panel-default">
        <div class="panel-heading">
            Your panel heading
        </div>
        <div class="panel-body">
            Lorem ipsum.
        </div>
    </div>

In addition you may specify a ``panel-title`` within ``panel-heading`` using ``h1`` to ``h6``:

.. code:: Django

    {% panel %}
        {% panelheading %}
            {% paneltitle use_tag="h1" %}
                Your panel heading
            {% panelheading %}
        {% endpanelheading %}
        {% panelbody %}
            Lorem ipsum.
        {% endpanelbody %}
    {% endpanel %}

This renders the following html code:

.. code:: HTML

    <div class="panel panel-default">
        <div class="panel-heading">
            Your panel heading
        </div>
        <div class="panel-body">
            Lorem ipsum.
        </div>
    </div>

Panel with footer
*****************

Add a nested ``panel-footer``:

.. code:: Django

    {% panel %}
        {% panelbody %}
            Lorem ipsum.
        {% endpanelbody %}
        {% panelfooter %}
            Your panel footer
        {% endpanelfooter %}
    {% endpanel %}

This renders the following html code:

.. code:: HTML

    <div class="panel panel-default">
        <div class="panel-body">
            Lorem ipsum.
        </div>
        <div class="panel-footer">
            Your panel footer
        </div>
    </div>

Contextual alternatives
***********************

Provide valid bootstrap class names to ``add_css_classes`` parameter for ``panel``:

.. code:: Django

    {% panel add_css_classes="panel-primary" %}
        {% panelbody %}
            Your primary panel.
        {% endpanelbody %}
    {% endpanel %}

This renders the following html code:

.. code:: HTML

    <div class="panel panel-default panel-primary">
        <div class="panel-body">
            Your primary panel.
        </div>
    </div>

Other valid css classes are ``panel-success``, ``panel-info``, ``panel-warning`` and ``panel-danger``.

With list groups
****************

As mentioned in the bootstrap docs you may use a list group inside your panel, even in addition to default panel contents:

.. code:: Django

    {% panel %}
        {% panelheading %}
            Panel heading
        {% endpanelheading %}
        {% panelbody %}
            <p>...</p>
        {% endpanelbody %}

        {% listgroup %}
            {% listgroupitem %}
                Cras justo odio
            {% endlistgroupitem %}
            {% listgroupitem %}
                Dapibus ac facilisis in
            {% endlistgroupitem %}
            {% listgroupitem %}
                Morbi leo risus
            {% endlistgroupitem %}
            {% listgroupitem %}
                Porta ac consectetur ac
            {% endlistgroupitem %}
            {% listgroupitem %}
                Vestibulum at eros
            {% endlistgroupitem %}
        {% endlistgroup %}
    {% endpanel %}

This renders the following html code:

.. code:: HTML

    <div class="panel panel-default">
        <div class="panel-heading">
            Panel heading
        </div>
        <div class="panel-body">
            <p>...</p>
        </div>

        <ul class="list-group">
            <li class="list-group-item">Cras justo odio</li>
            <li class="list-group-item">Dapibus ac facilisis in</li>
            <li class="list-group-item">Morbi leo risus</li>
            <li class="list-group-item">Porta ac consectetur ac</li>
            <li class="list-group-item">Vestibulum at eros</li>
        </ul>
    </div>
