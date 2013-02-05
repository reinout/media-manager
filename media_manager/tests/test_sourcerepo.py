import os
import shutil
import tempfile
import unittest

from media_manager import sourcerepo


def exists(*path_elements):
    return os.path.exists(os.path.join(*path_elements))


class ChdirContext(object):
    """Context manager for a 'with' loop."""
    def __init__(self, target):
        self._original = os.getcwd()
        self._target = target

    def __enter__(self):
        os.chdir(self._target)
        return self

    def __exit__(self, *args):
        os.chdir(self._original)
        return self


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


class SourceRepoWithAnnexTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        with ChdirContext(self.tempdir):
            os.system("git init")
            os.system("git annex init tempdir")
        self.source_repo = sourcerepo.SourceRepo(self.tempdir)
