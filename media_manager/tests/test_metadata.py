from __future__ import unicode_literals
from __future__ import print_function
import os
import shutil
import tempfile
import unittest

from media_manager import metadata


class MetadataItemTest(unittest.TestCase):

    def test_kwarg_setting(self):
        item = metadata.MetadataItem(id='abc')
        self.assertEquals(item.id, 'abc')

    def test_only_allowed_kwarg_setting(self):
        self.assertRaises(ValueError, metadata.MetadataItem, reinout='abc')

    def test_as_dict1(self):
        item = metadata.MetadataItem()
        self.assertEquals(item.as_dict(), {})

    def test_as_dict2(self):
        item = metadata.MetadataItem(id='abc')
        self.assertEquals(item.as_dict(), {'id': 'abc'})


class MetadataTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.metadata = metadata.Metadata(self.tempdir)

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_smoke(self):
        self.assertTrue(self.metadata.filename.endswith('metadata.json'))

    def test_read_nonexisting(self):
        self.metadata.read()
        self.assertEquals(self.metadata.contents, {})

    def test_write_read_empty(self):
        self.metadata = metadata.Metadata(self.tempdir)
        self.metadata.write()
        self.metadata.read()
        self.assertTrue(os.path.exists(os.path.join(
                    self.tempdir, 'metadata.json')))
