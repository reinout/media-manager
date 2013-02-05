import logging
import os


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

    def read(self):
        """Iterate through the source repo and extract the file info."""
        pass

    def ensure_directory(self, kind, year=None):
        """Make sure the directory exists.

        The structure is ``SOURCE_REPO/:kind/:year/*.jpg``.
        """
        assert kind in KINDS
        directory = os.path.join(self.source_repo_location, kind)
        if year is not None:
            directory = os.path.join(directory, unicode(year))
        if not os.path.exists(directory):
            logger.info("Created {}", directory)
            os.makedirs(directory)
