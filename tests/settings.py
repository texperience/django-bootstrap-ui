DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}
INSTALLED_APPS = [
    'django.contrib.sessions',
    'bootstrap_ui',
]
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
)
ROOT_URLCONF = 'tests.urls'
SECRET_KEY = 'test-key'
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)
TEMPLATE_DIRS = (
    'tests/templates',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
