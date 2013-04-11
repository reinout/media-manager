from __future__ import unicode_literals
from __future__ import print_function
import logging

from jinja2 import Environment
from jinja2 import PackageLoader

from media_manager import metadata

logger = logging.getLogger(__name__)
jinja_env = Environment(loader=PackageLoader('media_manager', 'templates'))


class Page(object):
    template = 'layout.html'

    def __init__(self, context, path):
        self.context = context
        self.path = path

    def write(self):
        render_with_template = jinja_env.get_template(self.template).render
        render_with_template(pathto=self.path, **self.context)
