SECRET_KEY = 'test-key'
INSTALLED_APPS = [
    'bootstrap_ui',
]
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    'tests/templates',
)
