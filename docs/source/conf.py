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


# {% extends "!layout.html" %}
# {% block footer %}
# {{ super() }}
# <link rel="stylesheet" href="_static/custom.css" type="text/css">
# <div id="custom-footer-content">
#     <!-- 这里放置从 RevolverMaps 获取的 HTML/JavaScript 代码 -->
#     <script type="text/javascript" src="//rf.revolvermaps.com/0/0/6.js?i=5msw68d5wrj&amp;m=7&amp;c=e63100&amp;cr1=ffffff&amp;f=arial&amp;l=0&amp;bv=90&amp;lx=-420&amp;ly=420&amp;hi=20&amp;he=7&amp;hc=a8ddff&amp;rs=80" async="async"></script>
# </div>
# {% endblock %}
