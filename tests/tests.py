# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.test import RequestFactory, TestCase
from django.urls import reverse


class TemplatesTest(TestCase):
    def setUp(self):
        # Mock get request
        self.request = RequestFactory().get('/')

        # Provide template paths
        self.template_html5_skeleton = get_template('bootstrap_ui/html5-skeleton.html')
        self.template_bootstrap3_skeleton = get_template('bootstrap_ui/bootstrap3-skeleton.html')

    def test_html5_skeleton_is_rendered(self):
        rendered = self.template_html5_skeleton.render({})
        self.assertInHTML(
            '<html lang="en"><head><meta charset="utf-8"><title>django-bootstrap-ui template</title></head>'
            '<body><h1>Hello, django-bootstrap-ui!</h1></body></html>', rendered)

    def test_bootstrap3_skeleton_is_rendered(self):
        rendered = self.template_bootstrap3_skeleton.render({'request': self.request})
        self.assertInHTML('<meta http-equiv="X-UA-Compatible" content="IE=edge">', rendered)
        self.assertInHTML('<meta name="viewport" content="width=device-width, initial-scale=1">', rendered)
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertInHTML('<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>', rendered)
        self.assertInHTML('<script src="//ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>', rendered)
        self.assertNotIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css">', rendered)

    def test_bootstrap3_skeleton_bootstrap_theme_is_rendered(self):
        self.request.session = {'DJANGO_BOOTSTRAP_UI_THEME': 'bootstrap'}
        rendered = self.template_bootstrap3_skeleton.render({'request': self.request})
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css">', rendered)

    def test_bootstrap3_skeleton_bootswatch_theme_is_rendered(self):
        self.request.session = {'DJANGO_BOOTSTRAP_UI_THEME': 'bootswatch-paper'}
        rendered = self.template_bootstrap3_skeleton.render({'request': self.request})
        self.assertInHTML('<link href="//maxcdn.bootstrapcdn.com/bootswatch/3.3.7/paper/bootstrap.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertNotIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">', rendered)
        self.assertNotIn('<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css">', rendered)


class ThemingTest(TestCase):
    def setUp(self):
        # Mock get request
        self.request = RequestFactory().get('/')

        # Provide template paths
        self.template_helper_tags = get_template('helpertags.html')
        self.url_set_theme_view = reverse('set_theme')

    def test_theme_in_session_is_set(self):
        with self.settings(MIDDLEWARE=('django.contrib.sessions.middleware.SessionMiddleware',)):
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
        rendered = self.template_helper_tags.render({'request': self.request})
        self.assertIn('Theme|bootstrap-theme-in-session', rendered)

    def test_get_value_from_cookie_is_ok(self):
        self.request.COOKIES = {'DJANGO_BOOTSTRAP_UI_THEME': 'bootstrap-theme-in-cookies'}
        rendered = self.template_helper_tags.render({'request': self.request})
        self.assertIn('Theme|bootstrap-theme-in-cookies', rendered)

    def test_get_value_from_settings_is_ok(self):
        with self.settings(DJANGO_BOOTSTRAP_UI_THEME='bootstrap-theme-in-settings'):
            rendered = self.template_helper_tags.render({'request': self.request})
            self.assertIn('Theme|bootstrap-theme-in-settings', rendered)

    def test_get_value_default_is_ok(self):
        rendered = self.template_helper_tags.render({'request': self.request})
        self.assertIn('Theme|bootstrap-theme-default', rendered)
