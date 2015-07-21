from django.conf.urls import include, url

from .views import render_named_template

urlpatterns = [
    url(r'^render_named_template/(?P<template>.*)/$', render_named_template, name='render_named_template'),
    url(r'^themes/', include("bootstrap_ui.urls")),
]
