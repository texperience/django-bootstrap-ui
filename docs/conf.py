# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import datetime

from bootstrap_ui import __version__

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
#
# sys.path.insert(0, os.path.abspath(os.path.join('..', 'bootstrap_ui')))

# -- Project information -----------------------------------------------------

# General information about the project
project = 'django-bootstrap-ui'
copyright = '{year:d}, texperience'.format(year=datetime.now().year)
author = 'Timo Rieber'

# The short X.Y version
versiontuple = __version__.split('.')
version = __version__
release = '{}.{}'.format(versiontuple[0], versiontuple[1])


# -- General configuration ---------------------------------------------------

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

# The master toctree document
master_doc = 'index'

# The suffix of source filenames
source_suffix = '.rst'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use
pygments_style = 'sphinx'
