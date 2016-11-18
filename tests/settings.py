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
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            'tests/templates',
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ]
        },
    },
]
