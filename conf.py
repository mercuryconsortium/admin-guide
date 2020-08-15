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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

project = "Mercury HPC Administrator's Guide"
copyright = '2020, Tuguldur T. Odabdrakh'
author = 'Tuguldur T. Odbadrakh'
release = '0.1.1'

needs_sphinx = '1.0'
extensions = ['recommonmark','sphinxcontrib.fulltoc']
templates_path = ['_templates']
import astropy_sphinx_theme
html_theme_path = astropy_sphinx_theme.get_html_theme_path()
html_theme = 'bootstrap-astropy'
html_theme_options = {
    'sticky_navigation': True,
    'astropy_project_menubar': True
}
html_css_files = ['style.css']
html_static_path = ['_static']
pygments_style = 'sphinx'
