import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bootstrap-ui',
    version='0.1.0b1',
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    license='ISC License (ISCL)',
    description='This aims to be a powerful Django app to ease the integration of the popular Bootstrap UI framework'
                ' (http://getbootstrap.com).',
    long_description=README,
    url='https://github.com/timorieber/django-bootstrap-ui',
    author='Timo Rieber',
    author_email='dev@timorieber.de',
    install_requires=[
        'Django>=1.7,<1.9',
        'django-tag-parser>=2.1,<2.2',
        'dominate>=2.1,<2.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
