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
ROOT_URLCONF = 'tests.urls'
SECRET_KEY = 'test-key'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'tests/templates',
        ],
        'APP_DIRS': True,
    },
]
