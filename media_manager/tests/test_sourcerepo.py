import os
import shutil
import tempfile
import unittest

from media_manager import sourcerepo


def exists(*path_elements):
    return os.path.exists(os.path.join(*path_elements))


class SourceRepoTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.source_repo = sourcerepo.SourceRepo(self.tempdir)

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_ensure_directory1(self):
        self.source_repo.ensure_directory('photos')
        self.assertTrue(exists(self.tempdir, 'photos'))

    def test_ensure_directory2(self):
        self.source_repo.ensure_directory('photos', 1972)
        self.assertTrue(exists(self.tempdir, 'photos', '1972'))

    def test_ensure_directory3(self):
        self.source_repo.ensure_directory('photos', '1972')
        self.assertTrue(exists(self.tempdir, 'photos', '1972'))

    def test_ensure_directory4(self):
        self.assertRaises(AssertionError,
                          self.source_repo.ensure_directory,
                          'something_else')
