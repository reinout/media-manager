import unittest
import shutil
import tempfile

from media_manager import metadata
from media_manager import config


class MetadataTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.config = {}
        self.config.update(config.DEFAULT_CONFIG)
        self.config['source_repo_location'] = self.tempdir

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_smoke(self):
        md = metadata.Metadata()
        self.assertTrue(md.filename.endswith('media/metadata.json'))
