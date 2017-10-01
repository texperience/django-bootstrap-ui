# -*- coding: utf-8 -*-
from django.template import TemplateSyntaxError
from django.template.loader import get_template
from django.test import RequestFactory, SimpleTestCase, TestCase
from django.core.urlresolvers import reverse
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

    def setUp(self):
        self.template = get_template('htmltag.html')

    def test_htmltag_is_rendered(self):
        rendered = self.template.render({})
        self.assertInHTML(self.HTMLTAG_START + self.HTMLTAG_END, rendered)

    def test_htmltag_content_is_rendered(self):
        rendered = self.template.render({'content': self.SAMPLE_CONTENT})
        self.assertInHTML(self.HTMLTAG_START + self.SAMPLE_CONTENT + self.HTMLTAG_END, rendered)

    def test_htmltag_content_unicode_is_rendered(self):
        rendered = self.template.render({'content': self.SAMPLE_CONTENT_UNICODE})
        self.assertInHTML(self.HTMLTAG_START + self.SAMPLE_CONTENT_UNICODE + self.HTMLTAG_END, rendered)

    def test_htmltag_css_classes_are_rendered(self):
        rendered = self.template.render({'css': self.SAMPLE_CSS})
        self.assertInHTML(self.HTMLTAG_CSS_CLASSES_START + self.HTMLTAG_END, rendered)

    def test_htmltag_tag_is_rendered(self):
        rendered = self.template.render({'tag': self.SAMPLE_TAG})
        self.assertInHTML(self.HTMLTAG_TAG_START + self.HTMLTAG_TAG_END, rendered)

    def test_htmltag_invalid_tag_raises_exception(self):
        with self.assertRaises(TemplateSyntaxError):
            self.template.render({'tag': self.SAMPLE_INVALID_TAG})


class BootstrapTagsTest(SimpleTestCase):
    HTMLTAG_START = mark_safe('<div class="bs">')
    HTMLTAG_END = mark_safe('</div>')

    def setUp(self):
        self.template = get_template('bootstraptag.html')

    def test_bootstraptag_is_rendered(self):
        rendered = self.template.render({})
        self.assertInHTML(self.HTMLTAG_START + self.HTMLTAG_END, rendered)


class GridTagsTest(SimpleTestCase):
    SAMPLE_CONTENT = 'Lorem ipsum'
    SAMPLE_COLUMN_WIDTH = '7'
    SAMPLE_MD_COLUMN_WIDTH = '10'
    SAMPLE_MD_OFFSET_WIDTH = '1'
    SAMPLE_MD_PUSH_WIDTH = '2'
    SAMPLE_MD_PULL_WIDTH = '8'

    CONTAINER_START = mark_safe('<div class="container">')
    CONTAINER_END = mark_safe('</div>')

    CONTAINER_FLUID_START = mark_safe('<div class="container-fluid">')
    CONTAINER_FLUID_END = CONTAINER_END

    ROW_START = mark_safe('<div class="row">')
    ROW_END = CONTAINER_END

    COLUMN_START = mark_safe('<div class="col-xs-12">')
    COLUMN_END = CONTAINER_END

    COLUMN_CUSTOM_WIDTH_START = mark_safe(
        '<div class="'
        + 'col-xs-' + SAMPLE_COLUMN_WIDTH
        + ' col-sm-' + SAMPLE_COLUMN_WIDTH
        + ' col-md-' + SAMPLE_COLUMN_WIDTH
        + ' col-lg-' + SAMPLE_COLUMN_WIDTH
        + '">'
    )
    COLUMN_CUSTOM_WIDTH_END = CONTAINER_END

    COLUMN_CUSTOM_WIDTH_DEFAULT = '<div class="col-lg-12" />'

    COLUMN_MD_OFFSET_START = mark_safe(
        '<div class="'
        + 'col-xs-' + SAMPLE_COLUMN_WIDTH
        + ' col-md-' + SAMPLE_MD_COLUMN_WIDTH
        + ' col-md-offset-' + SAMPLE_MD_OFFSET_WIDTH
        + '">'
    )
    COLUMN_MD_OFFSET_END = CONTAINER_END

    COLUMN_MD_PUSH_START = mark_safe(
        '<div class="'
        + 'col-md-' + str(12 - int(SAMPLE_MD_PUSH_WIDTH))
        + ' col-md-push-' + SAMPLE_MD_PUSH_WIDTH
        + '">'
    )

    COLUMN_MD_PUSH_END = CONTAINER_END

    COLUMN_MD_PULL_START = mark_safe(
        '<div class="'
        + 'col-md-' + str(12 - int(SAMPLE_MD_PULL_WIDTH))
        + ' col-md-pull-' + SAMPLE_MD_PULL_WIDTH
        + '">'
    )

    COLUMN_MD_PULL_END = CONTAINER_END

    def setUp(self):
        self.template = get_template('gridtags.html')

    def test_container_with_row_column_and_content_is_rendered(self):
        rendered = self.template.render({'content': self.SAMPLE_CONTENT, 'type': 'fluid'})
        self.assertInHTML(
            self.CONTAINER_START + self.ROW_START + self.COLUMN_START + self.SAMPLE_CONTENT + self.COLUMN_END
            + self.ROW_END + self.CONTAINER_END,
            rendered
        )

    def test_container_fluid_is_rendered(self):
        rendered = self.template.render({'type': 'fluid'})
        self.assertInHTML(self.CONTAINER_FLUID_START + self.CONTAINER_FLUID_END, rendered)

    def test_container_invalid_type_raises_exception(self):
        with self.assertRaises(TemplateSyntaxError):
            self.template.render({'type': 'foo'})

    def test_column_custom_grid_is_rendered(self):
        rendered = self.template.render({
            'xs': self.SAMPLE_COLUMN_WIDTH,
            'sm': self.SAMPLE_COLUMN_WIDTH,
            'md': self.SAMPLE_COLUMN_WIDTH,
            'lg': self.SAMPLE_COLUMN_WIDTH
        })
        self.assertInHTML(self.COLUMN_CUSTOM_WIDTH_START + self.COLUMN_CUSTOM_WIDTH_END, rendered)

    def test_column_custom_grid_with_defaults_is_rendered(self):
        rendered = self.template.render({'lg': ''})
        self.assertInHTML(self.COLUMN_CUSTOM_WIDTH_DEFAULT, rendered)

    def test_column_grid_with_offset_is_rendered(self):
        rendered = self.template.render({
            'xs': self.SAMPLE_COLUMN_WIDTH,
            'md': self.SAMPLE_MD_COLUMN_WIDTH,
            'md_offset': self.SAMPLE_MD_OFFSET_WIDTH
        })
        self.assertInHTML(self.COLUMN_MD_OFFSET_START + self.COLUMN_MD_OFFSET_END, rendered)

    def test_column_grid_with_push_is_rendered(self):
        rendered = self.template.render({
            'md': str(12 - int(self.SAMPLE_MD_PUSH_WIDTH)),
            'md_push': self.SAMPLE_MD_PUSH_WIDTH
        })
        self.assertInHTML(self.COLUMN_MD_PUSH_START + self.COLUMN_MD_PUSH_END, rendered)

    def test_column_grid_with_pull_is_rendered(self):
        rendered = self.template.render({
            'md': str(12 - int(self.SAMPLE_MD_PULL_WIDTH)),
            'md_pull': self.SAMPLE_MD_PULL_WIDTH
        })
        self.assertInHTML(self.COLUMN_MD_PULL_START + self.COLUMN_MD_PULL_END, rendered)


class ListGroupTagsTest(SimpleTestCase):
    SAMPLE_LINK = 'http://example.org'
    SAMPLE_LABEL = 'Linklabel'
    SAMPLE_LIST = [
        'alpha',
        'beta',
        'gamma',
    ]
    SAMPLE_LINKLIST = [
        ('alpha', SAMPLE_LINK),
        ('beta', SAMPLE_LINK),
        ('gamma', SAMPLE_LINK),
    ]

    LIST_GROUP_START = mark_safe('<ul class="list-group">')
    LIST_GROUP_END = mark_safe('</ul>')

    LIST_GROUP_ITEM_START = mark_safe('<li class="list-group-item">')
    LIST_GROUP_ITEM_END = mark_safe('</li>')

    LIST_GROUP_LINK_START = mark_safe('<div class="list-group">')
    LIST_GROUP_LINK_END = mark_safe('</div>')

    LIST_GROUP_ITEM_LINK_START = mark_safe('<a class="list-group-item" href="' + SAMPLE_LINK + '">')
    LIST_GROUP_ITEM_LINK_END = mark_safe('</a>')

    LIST_GROUP_BUTTON_START = LIST_GROUP_LINK_START
    LIST_GROUP_BUTTON_END = LIST_GROUP_LINK_END

    LIST_GROUP_ITEM_BUTTON_START = mark_safe('<button class="list-group-item" type="button">')
    LIST_GROUP_ITEM_BUTTON_END = mark_safe('</button>')

    def setUp(self):
        self.template = get_template('listgrouptags.html')

    def test_list_group_is_rendered(self):
        rendered = self.template.render({})
        self.assertIn(self.LIST_GROUP_START, rendered)
        self.assertIn(self.LIST_GROUP_END, rendered)

    def test_list_group_item_in_list_group_is_rendered(self):
        rendered = self.template.render({})
        self.assertInHTML(
            self.LIST_GROUP_START + self.LIST_GROUP_ITEM_START + self.LIST_GROUP_ITEM_END + self.LIST_GROUP_END,
            rendered
        )

    def test_list_group_item_default_tag_is_rendered(self):
        rendered = self.template.render({})
        self.assertInHTML(self.LIST_GROUP_ITEM_START + self.LIST_GROUP_ITEM_END, rendered)

    def test_list_group_item_link_is_rendered(self):
        rendered = self.template.render({'use_tag': 'a', 'link': self.SAMPLE_LINK, 'label': self.SAMPLE_LABEL})
        self.assertInHTML(self.LIST_GROUP_ITEM_LINK_START + self.SAMPLE_LABEL + self.LIST_GROUP_ITEM_LINK_END, rendered)

    def test_list_group_item_button_is_rendered(self):
        rendered = self.template.render({'use_tag': 'button', 'label': self.SAMPLE_LABEL})
        self.assertInHTML(self.LIST_GROUP_ITEM_BUTTON_START + self.SAMPLE_LABEL + self.LIST_GROUP_ITEM_BUTTON_END, rendered)

    def test_list_group_item_link_without_destination_raises_exception(self):
        with self.assertRaises(TemplateSyntaxError):
            self.template.render({'use_tag': 'a'})

    def test_listgroup_list_is_rendered(self):
        rendered = self.template.render({'type': 'list', 'items': self.SAMPLE_LIST})
        self.assertInHTML(
            self.LIST_GROUP_START
            + ''.join(self.LIST_GROUP_ITEM_START + item + self.LIST_GROUP_ITEM_END for item in self.SAMPLE_LIST)
            + self.LIST_GROUP_END,
            rendered
        )

    def test_listgroup_without_type_is_empty(self):
        rendered = self.template.render({'items': self.SAMPLE_LIST})
        self.assertHTMLEqual('', rendered)

    def test_listgroup_linklist_is_rendered(self):
        rendered = self.template.render({'type': 'linklist', 'items': self.SAMPLE_LINKLIST})
        self.assertInHTML(
            self.LIST_GROUP_LINK_START
            + ''.join(
                self.LIST_GROUP_ITEM_LINK_START
                + item[0]
                + self.LIST_GROUP_ITEM_LINK_END for item in self.SAMPLE_LINKLIST
            )
            + self.LIST_GROUP_LINK_END,
            rendered
        )

    def test_listgroup_buttonlist_is_rendered(self):
        rendered = self.template.render({'type': 'buttonlist', 'items': self.SAMPLE_LIST})
        self.assertInHTML(
            self.LIST_GROUP_BUTTON_START
            + ''.join(
                self.LIST_GROUP_ITEM_BUTTON_START
                + item
                + self.LIST_GROUP_ITEM_BUTTON_END for item in self.SAMPLE_LIST
            )
            + self.LIST_GROUP_BUTTON_END,
            rendered
        )


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

    def setUp(self):
        self.template = get_template('paneltags.html')

    def test_panel_is_rendered(self):
        rendered = self.template.render({})
        self.assertInHTML(
            self.PANEL_START
            + self.PANEL_HEADING_START + self.PANEL_HEADING_END
            + self.PANEL_BODY_START + self.PANEL_BODY_END
            + self.PANEL_FOOTER_START + self.PANEL_FOOTER_END
            + self.PANEL_END, rendered
        )

    def test_panel_heading_content_is_rendered(self):
        rendered = self.template.render({'heading': self.SAMPLE_HEADING})
        self.assertInHTML(self.PANEL_HEADING_START + self.SAMPLE_HEADING + self.PANEL_HEADING_END, rendered)

    def test_panel_title_content_is_rendered(self):
        rendered = self.template.render({'use_tag': 'h3', 'title': self.SAMPLE_TITLE})
        self.assertInHTML(
            self.PANEL_HEADING_START + self.PANEL_TITLE_START
            + self.SAMPLE_TITLE
            + self.PANEL_TITLE_END + self.PANEL_HEADING_END, rendered
        )

    def test_panel_body_content_is_rendered(self):
        rendered = self.template.render({'body': self.SAMPLE_BODY})
        self.assertInHTML(self.PANEL_BODY_START + self.SAMPLE_BODY + self.PANEL_BODY_END, rendered)

    def test_panel_footer_content_is_rendered(self):
        rendered = self.template.render({'footer': self.SAMPLE_FOOTER})
        self.assertInHTML(self.PANEL_FOOTER_START + self.SAMPLE_FOOTER + self.PANEL_FOOTER_END, rendered)


class TemplatesTest(TestCase):
    def setUp(self):
        # Mock get request
        self.request = RequestFactory().get('/')

        # Provide template paths
        self.template_html5_skeleton = get_template('bootstrap_ui/html5-skeleton.html')
        self.template_bootstrap_skeleton = get_template('bootstrap_ui/bootstrap-skeleton.html')

    def test_html5_skeleton_is_rendered(self):
        rendered = self.template_html5_skeleton.render({})
        self.assertInHTML(
            '<html lang="en"><head><meta charset="utf-8"><title>django-bootstrap-ui template</title></head>'
            '<body><h1>Hello, django-bootstrap-ui!</h1></body></html>', rendered)

    def test_bootstrap_skeleton_is_rendered(self):
        rendered = self.template_bootstrap_skeleton.render({'request': self.request})
        self.assertInHTML('<meta http-equiv="X-UA-Compatible" content="IE=edge">', rendered)
        self.assertInHTML('<meta name="viewport" content="width=device-width, initial-scale=1">', rendered)
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertInHTML('<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>', rendered)
        self.assertInHTML('<script src="//ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>', rendered)
        self.assertNotIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css">', rendered)

    def test_bootstrap_skeleton_bootstrap_theme_is_rendered(self):
        self.request.session = {'DJANGO_BOOTSTRAP_UI_THEME': 'bootstrap'}
        rendered = self.template_bootstrap_skeleton.render({'request': self.request})
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css">', rendered)

    def test_bootstrap_skeleton_bootswatch_theme_is_rendered(self):
        self.request.session = {'DJANGO_BOOTSTRAP_UI_THEME': 'bootswatch-paper'}
        rendered = self.template_bootstrap_skeleton.render({'request': self.request})
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/bootswatch/3.3.7/paper/bootstrap.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertNotIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertNotIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css">', rendered)


class ThemingTest(TestCase):
    def setUp(self):
        # Mock get request
        self.request = RequestFactory().get('/')

        # Provide template paths
        self.template_assignment_tags = get_template('assignmenttags.html')
        self.url_set_theme_view = reverse('set_theme')

    def test_theme_in_session_is_set(self):
        with self.settings(MIDDLEWARE_CLASSES=('django.contrib.sessions.middleware.SessionMiddleware',)):
            self.client.post(self.url_set_theme_view, {'theme': 'bootstrap-theme-in-session'})
            self.assertEqual(self.client.session['DJANGO_BOOTSTRAP_UI_THEME'], 'bootstrap-theme-in-session')

    def test_theme_in_cookie_is_set(self):
        self.client.post(self.url_set_theme_view, {'theme': 'bootstrap-theme-in-cookies'})
        self.assertEqual(self.client.cookies['DJANGO_BOOTSTRAP_UI_THEME'].value, 'bootstrap-theme-in-cookies')

    def test_set_theme_is_redirected(self):
        # We are redirecting to non-existent urls/views and therefore expecting 404 codes in the end
        response = self.client.get(self.url_set_theme_view)
        self.assertRedirects(response, '/', 302, 404)
        response = self.client.post(self.url_set_theme_view)
        self.assertRedirects(response, '/', 302, 404)
        response = self.client.get(self.url_set_theme_view, {'next': '/foo'})
        self.assertRedirects(response, '/foo', 302, 404)
        response = self.client.get(self.url_set_theme_view, {'next': '/foo/?bar=yes'})
        self.assertRedirects(response, '/foo/?bar=yes', 302, 404)

    def test_get_value_from_session_is_ok(self):
        self.request.session = {'DJANGO_BOOTSTRAP_UI_THEME': 'bootstrap-theme-in-session'}
        rendered = self.template_assignment_tags.render({'request': self.request})
        self.assertIn('Theme|bootstrap-theme-in-session', rendered)

    def test_get_value_from_cookie_is_ok(self):
        self.request.COOKIES = {'DJANGO_BOOTSTRAP_UI_THEME': 'bootstrap-theme-in-cookies'}
        rendered = self.template_assignment_tags.render({'request': self.request})
        self.assertIn('Theme|bootstrap-theme-in-cookies', rendered)

    def test_get_value_from_settings_is_ok(self):
        with self.settings(DJANGO_BOOTSTRAP_UI_THEME='bootstrap-theme-in-settings'):
            rendered = self.template_assignment_tags.render({'request': self.request})
            self.assertIn('Theme|bootstrap-theme-in-settings', rendered)

    def test_get_value_default_is_ok(self):
        rendered = self.template_assignment_tags.render({'request': self.request})
        self.assertIn('Theme|bootstrap-theme-default', rendered)
