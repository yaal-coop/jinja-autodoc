import datetime
import os
import sys
from importlib import metadata

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../sphinxcontrib"))

extensions = [
    "sphinxcontrib.jinja",
    "sphinxcontrib.autojinja.jinja",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
source_suffix = {".rst": "restructuredtext"}
master_doc = "index"
project = "sphinxcontrib-jinja"
year = datetime.datetime.now().strftime("%Y")
copyright = f"{year}, Jaka Hudoklin"
version = metadata.version(project)
release = metadata.version(project)
language = "en"
exclude_patterns = ["_build"]
pygments_style = "sphinx"
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

# -- Options for HTML output ----------------------------------------------

html_theme = "shibuya"
html_theme_options = {
    "page_layout": "compact",
}
htmlhelp_basename = "sphinxcontrib-jinjadoc"

jinja_template_path = "doc/"
