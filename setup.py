import os

from setuptools import find_namespace_packages, setup

from bootstrap_ui import __version__

# Installation dependencies
install_requires = [
    'django>=2.2,<2.3',
]

# Testing dependencies
testing_extras = [
    'coverage>=5.0,<6.0',
    'flake8>=3.7,<4.0',
    'tox>=3.14,<4.0',
]

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bootstrap-ui',
    version=__version__,
    packages=find_namespace_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    license='ISC License (ISCL)',
    description='This aims to be a powerful Django app to ease the integration of the popular Bootstrap UI framework'
                ' (http://getbootstrap.com).',
    long_description=open('README.rst').read(),
    url='https://gitlab.com/texperience/django-bootstrap-ui',
    author='Timo Rieber',
    author_email='trieber@texperience.de',
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
