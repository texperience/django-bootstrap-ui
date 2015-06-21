# -*- coding: utf-8 -*-
from django.template import Context, Template, TemplateSyntaxError
from django.test import SimpleTestCase
from django.utils.safestring import mark_safe


class HtmlTagNodeTest(SimpleTestCase):
    SAMPLE_CONTENT = 'Lorem ipsum'
    SAMPLE_CONTENT_UNICODE = 'Lörém ípsüm'
    SAMPLE_CSS = 'simple sample'
    SAMPLE_TAG = 'span'
    SAMPLE_INVALID_TAG = 'foo'

    HTMLTAG_START = mark_safe('<div>')
    HTMLTAG_CSS_CLASSES_START = mark_safe('<div class="' + SAMPLE_CSS + '">')
    HTMLTAG_END = mark_safe('</div>')

    HTMLTAG_TAG_START = mark_safe('<' + SAMPLE_TAG + '>')
    HTMLTAG_TAG_END = mark_safe('</' + SAMPLE_TAG + '>')

    TEMPLATE_SIMPLE = Template(
        '{% load bootstrap_ui_tags %}'
        '{% htmltag %}'
        '{% endhtmltag %}'
    )
    TEMPLATE_CONTENT = Template(
        '{% load bootstrap_ui_tags %}'
        '{% htmltag %}'
        '{{ content }}'
        '{% endhtmltag %}'
    )
    TEMPLATE_CSS = Template(
        '{% load bootstrap_ui_tags %}'
        '{% htmltag add_css_classes=css %}'
        '{% endhtmltag %}'
    )
    TEMPLATE_TAG = Template(
        '{% load bootstrap_ui_tags %}'
        '{% htmltag use_tag=tag %}'
        '{% endhtmltag %}'
    )

    def setUp(self):
        pass

    def test_htmltag_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({}))
        self.assertInHTML(self.HTMLTAG_START + self.HTMLTAG_END, rendered)

    def test_htmltag_content_is_rendered(self):
        rendered = self.TEMPLATE_CONTENT.render(Context({'content': self.SAMPLE_CONTENT}))
        self.assertInHTML(self.HTMLTAG_START + self.SAMPLE_CONTENT + self.HTMLTAG_END, rendered)

    def test_htmltag_content_unicode_is_rendered(self):
        rendered = self.TEMPLATE_CONTENT.render(Context({'content': self.SAMPLE_CONTENT_UNICODE}))
        self.assertInHTML(self.HTMLTAG_START + self.SAMPLE_CONTENT_UNICODE + self.HTMLTAG_END, rendered)

    def test_htmltag_css_classes_are_rendered(self):
        rendered = self.TEMPLATE_CSS.render(Context({'css': self.SAMPLE_CSS}))
        self.assertInHTML(self.HTMLTAG_CSS_CLASSES_START + self.HTMLTAG_END, rendered)

    def test_htmltag_tag_is_rendered(self):
        rendered = self.TEMPLATE_TAG.render(Context({'tag': self.SAMPLE_TAG}))
        self.assertInHTML(self.HTMLTAG_TAG_START + self.HTMLTAG_TAG_END, rendered)

    def test_htmltag_invalid_tag_raises_exception(self):
        with self.assertRaises(TemplateSyntaxError):
            self.TEMPLATE_TAG.render(Context({'tag': self.SAMPLE_INVALID_TAG}))


class BootstrapTagsTest(SimpleTestCase):
    HTMLTAG_START = mark_safe('<div class="bs">')
    HTMLTAG_END = mark_safe('</div>')

    TEMPLATE_SIMPLE = Template(
        '{% load bootstrap_ui_tags %}'
        '{% bootstraptag %}'
        '{% endbootstraptag %}'
    )

    def setUp(self):
        pass

    def test_bootstraptag_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({}))
        self.assertInHTML(self.HTMLTAG_START + self.HTMLTAG_END, rendered)


class GridTagsTest(SimpleTestCase):
    SAMPLE_CONTENT = 'Lorem ipsum'
    SAMPLE_COLUMN_WIDTH = '7'

    CONTAINER_START = mark_safe('<div class="container">')
    CONTAINER_END = mark_safe('</div>')

    CONTAINER_FLUID_START = mark_safe('<div class="container-fluid">')
    CONTAINER_FLUID_END = mark_safe('</div>')

    ROW_START = mark_safe('<div class="row">')
    ROW_END = mark_safe('</div>')

    COLUMN_START = mark_safe('<div class="col-xs-12">')
    COLUMN_END = mark_safe('</div>')

    COLUMN_CUSTOM_WIDTH_START = mark_safe(
        '<div class="'
        + 'col-xs-' + SAMPLE_COLUMN_WIDTH
        + ' col-sm-' + SAMPLE_COLUMN_WIDTH
        + ' col-md-' + SAMPLE_COLUMN_WIDTH
        + ' col-lg-' + SAMPLE_COLUMN_WIDTH
        + '">'
    )
    COLUMN_CUSTOM_WIDTH_END = mark_safe('</div>')

    COLUMN_CUSTOM_WIDTH_DEFAULT = '<div class="col-lg-12" />'

    TEMPLATE_SIMPLE = Template(
        '{% load bootstrap_ui_tags %}'
        '{% container %}'
        '{% row %}'
        '{% column %}'
        '{{ content }}'
        '{% endcolumn %}'
        '{% endrow %}'
        '{% endcontainer %}'
        '{% container type=type %}'
        '{% endcontainer %}'
    )

    TEMPLATE_CUSTOM_COLUMN = Template(
        '{% load bootstrap_ui_tags %}'
        '{% column xs=xs sm=sm md=md lg=lg %}'
        '{% endcolumn %}'
    )

    TEMPLATE_CUSTOM_COLUMN_DEFAULT = Template(
        '{% load bootstrap_ui_tags %}'
        '{% column lg=lg %}'
        '{% endcolumn %}'
    )

    def setUp(self):
        pass

    def test_container_with_row_column_and_content_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({'content': self.SAMPLE_CONTENT, 'type': 'fluid'}))
        self.assertInHTML(
            self.CONTAINER_START + self.ROW_START + self.COLUMN_START + self.SAMPLE_CONTENT + self.COLUMN_END
            + self.ROW_END + self.CONTAINER_END,
            rendered
        )

    def test_container_fluid_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({'type': 'fluid'}))
        self.assertInHTML(self.CONTAINER_FLUID_START + self.CONTAINER_FLUID_END, rendered)

    def test_container_invalid_type_raises_exception(self):
        with self.assertRaises(TemplateSyntaxError):
            self.TEMPLATE_SIMPLE.render(Context({'type': 'foo'}))

    def test_column_custom_grid_is_rendered(self):
        rendered = self.TEMPLATE_CUSTOM_COLUMN.render(Context({
            'xs': self.SAMPLE_COLUMN_WIDTH,
            'sm': self.SAMPLE_COLUMN_WIDTH,
            'md': self.SAMPLE_COLUMN_WIDTH,
            'lg': self.SAMPLE_COLUMN_WIDTH
        }))
        self.assertInHTML(self.COLUMN_CUSTOM_WIDTH_START + self.COLUMN_CUSTOM_WIDTH_END, rendered)

    def test_column_custom_grid_with_defaults_is_rendered(self):
        rendered = self.TEMPLATE_CUSTOM_COLUMN_DEFAULT.render(Context({'lg': ''}))
        self.assertInHTML(self.COLUMN_CUSTOM_WIDTH_DEFAULT, rendered)


class ListGroupTagsTest(SimpleTestCase):
    SAMPLE_LINK = 'http://example.org'
    SAMPLE_LABEL = 'Linklabel'

    LIST_GROUP_START = mark_safe('<ul class="list-group">')
    LIST_GROUP_END = mark_safe('</ul>')

    LIST_GROUP_ITEM_START = mark_safe('<li class="list-group-item">')
    LIST_GROUP_ITEM_END = mark_safe('</li>')

    LIST_GROUP_ITEM_LINK_START = mark_safe('<a class="list-group-item" href="' + SAMPLE_LINK + '">')
    LIST_GROUP_ITEM_LINK_END = mark_safe('</a>')

    TEMPLATE_SIMPLE = Template(
        '{% load bootstrap_ui_tags %}'
        '{% listgroup %}'
        '{% listgroupitem %}'
        '{{ sample_content }}'
        '{% endlistgroupitem %}'
        '{% endlistgroup %}'
    )

    TEMPLATE_LINK = Template(
        '{% load bootstrap_ui_tags %}'
        '{% listgroupitem use_tag="a" link=sample_link %}'
        '{{ sample_label }}'
        '{% endlistgroupitem %}'
    )

    def setUp(self):
        pass

    def test_list_group_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({}))
        self.assertIn(self.LIST_GROUP_START, rendered)
        self.assertIn(self.LIST_GROUP_END, rendered)

    def test_list_group_item_in_list_group_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({}))
        self.assertInHTML(
            self.LIST_GROUP_START + self.LIST_GROUP_ITEM_START + self.LIST_GROUP_ITEM_END + self.LIST_GROUP_END,
            rendered
        )

    def test_list_group_item_default_tag_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({}))
        self.assertInHTML(self.LIST_GROUP_ITEM_START + self.LIST_GROUP_ITEM_END, rendered)

    def test_list_group_item_link_is_rendered(self):
        rendered = self.TEMPLATE_LINK.render(
            Context({'sample_link': self.SAMPLE_LINK, 'sample_label': self.SAMPLE_LABEL})
        )
        self.assertInHTML(self.LIST_GROUP_ITEM_LINK_START + self.SAMPLE_LABEL + self.LIST_GROUP_ITEM_LINK_END, rendered)

    def test_list_group_item_link_without_destination_raises_exception(self):
        with self.assertRaises(TemplateSyntaxError):
            self.TEMPLATE_LINK.render(Context({}))


class PanelTagsTest(SimpleTestCase):
    SAMPLE_HEADING = 'Lorem ipsum heading'
    SAMPLE_TITLE = 'Lorem ipsum title'
    SAMPLE_BODY = 'Lorem ipsum body'
    SAMPLE_FOOTER = 'Lorem ipsum footer'

    PANEL_START = mark_safe('<div class="panel panel-default">')
    PANEL_END = mark_safe('</div>')

    PANEL_HEADING_START = mark_safe('<div class="panel-heading">')
    PANEL_HEADING_END = mark_safe('</div>')

    PANEL_TITLE_START = mark_safe('<h3 class="panel-title">')
    PANEL_TITLE_END = mark_safe('</h3>')

    PANEL_BODY_START = mark_safe('<div class="panel-body">')
    PANEL_BODY_END = mark_safe('</div>')

    PANEL_FOOTER_START = mark_safe('<div class="panel-footer">')
    PANEL_FOOTER_END = mark_safe('</div>')

    TEMPLATE_SIMPLE = Template(
        '{% load bootstrap_ui_tags %}'
        '{% panel %}'
        '{% panelheading %}'
        '{{ sample_heading }}'
        '{% endpanelheading %}'
        '{% panelbody %}'
        '{{ sample_body }}'
        '{% endpanelbody %}'
        '{% panelfooter %}'
        '{{ sample_footer }}'
        '{% endpanelfooter %}'
        '{% endpanel %}'
    )

    TEMPLATE_TITLE = Template(
        '{% load bootstrap_ui_tags %}'
        '{% panel %}'
        '{% panelheading %}'
        '{% paneltitle use_tag="h3" %}'
        '{{ sample_title }}'
        '{% endpaneltitle %}'
        '{% endpanelheading %}'
        '{% endpanel %}'
    )

    def setUp(self):
        pass

    def test_panel_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({}))
        self.assertInHTML(
            self.PANEL_START
            + self.PANEL_HEADING_START + self.PANEL_HEADING_END
            + self.PANEL_BODY_START + self.PANEL_BODY_END
            + self.PANEL_FOOTER_START + self.PANEL_FOOTER_END
            + self.PANEL_END, rendered
        )

    def test_panel_heading_content_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({'sample_heading': self.SAMPLE_HEADING}))
        self.assertInHTML(self.PANEL_HEADING_START + self.SAMPLE_HEADING + self.PANEL_HEADING_END, rendered)

    def test_panel_title_content_is_rendered(self):
        rendered = self.TEMPLATE_TITLE.render(Context({'sample_title': self.SAMPLE_TITLE}))
        self.assertInHTML(
            self.PANEL_START
            + self.PANEL_HEADING_START + self.PANEL_TITLE_START
            + self.SAMPLE_TITLE
            + self.PANEL_TITLE_END + self.PANEL_HEADING_END
            + self.PANEL_END, rendered
        )

    def test_panel_body_content_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({'sample_body': self.SAMPLE_BODY}))
        self.assertInHTML(self.PANEL_BODY_START + self.SAMPLE_BODY + self.PANEL_BODY_END, rendered)

    def test_panel_footer_content_is_rendered(self):
        rendered = self.TEMPLATE_SIMPLE.render(Context({'sample_footer': self.SAMPLE_FOOTER}))
        self.assertInHTML(self.PANEL_FOOTER_START + self.SAMPLE_FOOTER + self.PANEL_FOOTER_END, rendered)
