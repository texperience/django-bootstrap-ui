# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join('..', 'bootstrap_ui', 'templatetags')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'bootstrap_ui.tests.settings'

# -- Project information -----------------------------------------------------

project = 'django-bootstrap-ui'
copyright = '2020, Timo Rieber'
author = 'Timo Rieber'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc']

# Autodoc options
autodoc_default_options = {
    'members': None,  # Include all members (methods).
    'special-members': '__init__',
    'exclude-members': '__dict__,__weakref__',  # Exclude "standard" methods.
    'member-order': 'bysource',    'show-inheritance': True,
}


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
