"""JSON-stored metadata about the managed media.
"""
import json
import logging
import os

METADATA_FILENAME = 'metadata.json'

logger = logging.getLogger(__name__)


class Metadata(object):
    """Wrapper around a JSON file that holds the media metadata.

    """
    def __init__(self, source_repo_location):
        self.source_repo_location = source_repo_location
        self.filename = os.path.join(self.source_repo_location,
                                     METADATA_FILENAME)
        self.contents = {}

    def read(self):
        """Read the metadata file."""
        if not os.path.exists(self.filename):
            logger.warning(
                "Metadata file {} doesn't exist yet. We'll create it later.",
                self.filename)
            return
        self.contents = json.load(open(self.filename))

    def write(self):
        """Write our contents back to the metadata file."""
        json.dump(self.contents, open(self.filename, 'w'))
