import logging
import os
import shutil

from media_manager.metadata import Metadata


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

    def read(self):
        """Iterate through the source repo and extract the file info."""
        pass

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

    def add_file(self, filepath):
        """Copy the file to the source repo in a year directory.

        Detect filetype and also record the source filepath in the metadata.
        """
        kind = 'photos'
        year = 2011
        target_dir = self.ensure_directory(kind, year)
        filename = os.path.basename(filepath).lower()
        target = os.path.join(target_dir, filename)
        logger.debug("Adding file %s as %s.", filepath, target)
        # TODO check duplicate filenames. Or warn.
        # TODO lowercase filename.
        shutil.copy(filepath, target)
