import sys
import os
sys.path.insert(0, os.path.abspath('../src/main/python/'))

# Project
project = "sql-smith"
author = "Franky Braem"

# Extensions
extensions = ['sphinx.ext.autodoc']

pygments_style = 'sphinx'

html_static_path = ['_static']
html_show_sourcelink = False


def setup(app):
    app.add_css_file('custom.css')
