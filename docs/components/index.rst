Available bootstrap components
==============================

List group
----------

See http://getbootstrap.com/components/#list-group.

Basic example
*************

Use the ``listgroup`` tag with nested ``listgroupitem`` tags::

    {% listgroup %}
        {% listgroupitem %}
            Your raw text.
        {% endlistgroupitem %}
        {% listgroupitem %}
            You may also use a {{ context_variable }}.
        {% endlistgroupitem %}
    {% endlistgroup %}

This renders the following html code::

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

Provide ``use_tag`` and ``link`` parameters to get linked items::

    {% listgroup use_tag="div" %}
        {% listgroupitem use_tag="a" link="http://example.org" %}
            External link to {{ ext_page_title }}.
        {% endlistgroupitem %}
        {% listgroupitem use_tag="a" link=local_reference %}
            Internal link to {{ your_page_title }}. Note how the link is provided as a context variable.
        {% endlistgroupitem %}
    {% endlistgroup %}

This renders the following html code::

    <div class="list-group">
        <a class="list-group-item" href="http://example.org">
            External link to Example.
        </a>
        <a class="list-group-item" href="your_local_link">
            Internal link to awesame internal page. Note how the link is provided as a context variable.
        </a>
    </div>

Custom content
**************

You may also render custom html content within your ``list-group-item``::

    {% listgroup use_tag="div" %}
        {% listgroupitem use_tag="div" %}
            <h2>A custom title</h2>
            <p>With a custom paragraph.</p>
        {% endlistgroupitem %}
    {% endlistgroup %}

This renders the following html code::

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

Use the ``panel`` in a simple way::

    {% panel %}
        {% panelbody %}
            Lorem ipsum.
        {% endpanelbody %}
    {% endpanel %}

This renders the following html code::

    <div class="panel panel-default">
        <div class="panel-body">
            Lorem ipsum.
        </div>
    </div>

Panel with heading
******************

Add a nested ``panel-heading``::

    {% panel %}
        {% panelheading %}
            Your panel heading
        {% endpanelheading %}
        {% panelbody %}
            Lorem ipsum.
        {% endpanelbody %}
    {% endpanel %}

This renders the following html code::

    <div class="panel panel-default">
        <div class="panel-heading">
            Your panel heading
        </div>
        <div class="panel-body">
            Lorem ipsum.
        </div>
    </div>

In addition you may specify a ``panel-title`` within ``panel-heading`` using ``h1`` to ``h6``::

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

This renders the following html code::

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

Add a nested ``panel-footer``::

    {% panel %}
        {% panelbody %}
            Lorem ipsum.
        {% endpanelbody %}
        {% panelfooter %}
            Your panel footer
        {% endpanelfooter %}
    {% endpanel %}

This renders the following html code::

    <div class="panel panel-default">
        <div class="panel-body">
            Lorem ipsum.
        </div>
        <div class="panel-footer">
            Your panel footer
        </div>
    </div>

With list groups
****************

As mentioned in the bootstrap docs you may use a list group inside your panel, even in addition to default panel contents::

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

This renders the following html code::

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
