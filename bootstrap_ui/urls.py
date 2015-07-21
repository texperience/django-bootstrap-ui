from django.conf.urls import url

from bootstrap_ui.views import set_theme

urlpatterns = [
    url(r'^set_theme/$', set_theme, name='set_theme'),
]
