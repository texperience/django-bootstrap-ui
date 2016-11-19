from django.conf.urls import include, url

urlpatterns = [
    url(r'^themes/', include("bootstrap_ui.urls")),
]
