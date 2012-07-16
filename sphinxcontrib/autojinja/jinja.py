"""
    sphinxcontrib.autojinja
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2012 by Jaka Hudoklin
    :license: BSD, see LICENSE for details.

"""

import re
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

from docutils import nodes
from docutils.statemachine import ViewList

from sphinx.util import force_decode
from sphinx.util.compat import Directive
from sphinx.util.nodes import nested_parse_with_titles
from sphinx.util.docstrings import prepare_docstring
from sphinx.pycode import ModuleAnalyzer

from sphinxcontrib import jinjadomain


def jinja_directive(path, content):
    if isinstance(content, basestring):
        content = content.splitlines()
    yield ''
    yield '.. jinja:template:: {path}'.format(**locals())
    yield ''
    for line in content:
        yield '   ' + line
    yield ''

def parse_jinja_comment(path):
    """
    Parses jinja comment

    :param path: Path to jinja template
    :type path: str

    :returns: Jinja comment docstring
    :rtype: str
    """

    import pdb; pdb.set_trace()

    f= open(path, 'r')
    contents= f.read()
    res=re.match(r"\{\#(.+?)\#\}", contents, flags=re.MULTILINE|re.DOTALL)
    if res:
        return res.group(1)

    return None

class AutojinjaDirective(Directive):

    has_content = True
    required_arguments = 1
    option_spec = {}

    @property
    def endpoints(self):
        try:
            endpoints = re.split(r'\s*,\s*', self.options['endpoints'])
        except KeyError:
            # means 'endpoints' option was missing
            return None
        return frozenset(endpoints)

    @property
    def undoc_endpoints(self):
        try:
            endpoints = re.split(r'\s*,\s*', self.options['undoc-endpoints'])
        except KeyError:
            return frozenset()
        return frozenset(endpoints)

    def make_rst(self):
        path = self.arguments[0]
        docstring=parse_jinja_comment(path)
        docstring = prepare_docstring(docstring)
        for line in jinja_directive(path, docstring):
            yield line

    def run(self):
        node = nodes.section()
        node.document = self.state.document
        result = ViewList()
        for line in self.make_rst():
            result.append(line, '<autojinja>')
        nested_parse_with_titles(self.state, result, node)
        return node.children


def setup(app):
    if 'jinja' not in app.domains:
        jinjadomain.setup(app)
    app.add_directive('autojinja', AutojinjaDirective)

