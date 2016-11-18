import os

from setuptools import find_packages, setup

from bootstrap_ui import __version__

# Installation dependencies
install_requires = [
    'django>=1.8,<1.11',
    'django-tag-parser>=2.1,<2.2',
    'dominate>=2.1,<2.2',
]

# Testing dependencies
testing_extras = [
    'coverage>=4.0.3',
    'flake8>=2.4.1',
    'isort>=4.2.0',
]

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bootstrap-ui',
    version=__version__,
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    license='ISC License (ISCL)',
    description='This aims to be a powerful Django app to ease the integration of the popular Bootstrap UI framework'
                ' (http://getbootstrap.com).',
    long_description=open('README.rst').read(),
    url='https://github.com/texperience/django-bootstrap-ui',
    author='Timo Rieber',
    author_email='trieber@texperience.de',
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
