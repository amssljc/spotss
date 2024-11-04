# Configuration file for the Sphinx documentation builder.

# -- Project information
from recommonmark.parser import CommonMarkParser

project = 'Spotscope'
copyright = '2024, Jiacheng Leng'
author = 'Jiacheng Leng'

release = '1.0.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'recommonmark',
    'nbsphinx'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']


def setup(app):
    app.add_css_file('custom.css')


html_static_path = ['_static']

html_logo = 'docs\source\logo.jpg'  # 替换为你的 logo 路径
