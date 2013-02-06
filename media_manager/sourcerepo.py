from __future__ import unicode_literals
from __future__ import print_function
import logging
import os
import shutil

from media_manager.metadata import Metadata
from media_manager import utils


KINDS = ('photos', 'videos')

logger = logging.getLogger(__name__)


class SourceRepo(object):
    """Wrapper around the files and dirs of the media source repository.

    Inside the source repo are directories for photos and videos. Inside
    those are directories for every year. Inside the year directories are the
    actual photo and video files for that year.

    """
    def __init__(self, source_repo_location):
        self.source_repo_location = source_repo_location
        self.metadata = Metadata(self.source_repo_location)

    # def read(self):
    #     """Iterate through the source repo and extract the file info."""
    #     pass

    def ensure_directory(self, kind, year=None):
        """Make sure the directory exists. Return the directory's path.

        The structure is ``SOURCE_REPO/:kind/:year/*.jpg``.
        """
        assert kind in KINDS
        directory = os.path.join(self.source_repo_location, kind)
        if year is not None:
            directory = os.path.join(directory, unicode(year))
        if not os.path.exists(directory):
            logger.info("Created %s", directory)
            os.makedirs(directory)
        return directory

    def add_file(self, filepath, kind, year, title=None):
        """Copy the file to the source repo in a year directory.

        Return the filename relative to the root, we use that as an identifier.

        Detect filetype and also record the source filepath in the metadata.
        """
        assert kind in KINDS
        target_dir = self.ensure_directory(kind, year)
        filename = os.path.basename(filepath)
        filename = utils.nice_filename(filename, title, target_dir)
        target = os.path.join(target_dir, filename)
        logger.debug("Adding file %s as %s.", filepath, target)
        # TODO check duplicate filenames. Or warn.
        shutil.copy(filepath, target)
        return os.path.relpath(target, self.source_repo_location)
