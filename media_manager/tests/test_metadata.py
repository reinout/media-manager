import os
import shutil
import tempfile
import unittest

from media_manager import metadata


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
