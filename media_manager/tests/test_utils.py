from __future__ import unicode_literals
from __future__ import print_function
import os
import shutil
import tempfile
import unittest

from pkg_resources import resource_filename

from media_manager import utils


class UtilsTest(unittest.TestCase):

    def test_exists1(self):
        self.assertTrue(utils.exists('/', 'usr', 'lib'))

    def test_exists2(self):
        self.assertTrue(utils.exists('/usr/lib'))

    def test_exists3(self):
        self.assertFalse(utils.exists('/reinout/is/great/'))

    def test_absolute_expanded_path(self):
        path = utils.absolute_expanded_path('~/something')
        self.assertTrue(path.startswith('/home/') or
                        path.startswith('/Users/'))
