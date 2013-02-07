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

    def test_addable_to_metadata1(self):
        # We need an ID before the metadata can accept us.
        item = metadata.MetadataItem()
        self.assertFalse(item.addable_to_metadata)

    def test_addable_to_metadata2(self):
        # We need an ID before the metadata can accept us.
        item = metadata.MetadataItem(id='abc')
        self.assertTrue(item.addable_to_metadata)

    def test_addable_to_source_repo1(self):
        item = metadata.Photo()
        self.assertFalse(item.addable_to_source_repo)

    def test_addable_to_source_repo2(self):
        # We use Photo because that accepts original_filepath.
        item = metadata.Photo(original_filepath='/a/b/c')
        self.assertTrue(item.addable_to_source_repo)


class MetadataTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.metadata = metadata.Metadata(self.tempdir)

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_smoke(self):
        self.assertTrue(self.metadata.filename.endswith('metadata.json'))

    def test_read_nonexisting(self):
        # No existing file? The basic is already in place in-memory.
        self.metadata.read()
        self.assertTrue('videos' in self.metadata.contents)

    def test_write_read_empty(self):
        self.metadata.read()
        self.metadata.write()
        self.assertTrue(os.path.exists(os.path.join(
                    self.tempdir, 'metadata.json')))

    def test_write_read_non_empty(self):
        self.metadata.read()
        self.metadata.contents['reinout'] = 'fantastic'
        self.metadata.write()
        # Grab a new copy.
        new = metadata.Metadata(self.tempdir)
        new.read()
        self.assertEquals(new.contents['reinout'], 'fantastic')
