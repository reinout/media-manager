"""JSON-stored metadata about the managed media.
"""
from __future__ import unicode_literals
from __future__ import print_function
import json
import logging
import os

from media_manager import utils

METADATA_FILENAME = 'metadata.json'
GENERIC_FIELDS = [
    'kind',
    'id',
    ]
FILE_FIELDS = GENERIC_FIELDS + [
    'original_filepath',
    'year',
    'title',
    ]
PHOTO_FIELDS = FILE_FIELDS + []
VIDEO_FIELDS = FILE_FIELDS + []

logger = logging.getLogger(__name__)


class MetadataItem(object):
    fields = GENERIC_FIELDS

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            if kwarg not in self.fields:
                raise ValueError("Unknown kwarg: {}".format(kwarg))
            setattr(self, kwarg, kwargs[kwarg])

    def as_dict(self):
        """Return ourselves as a dictionary."""
        result = {}
        for field in self.fields:
            value = getattr(self, field, None)
            if value:
                result[field] = value
        return result

    @property
    def addable_to_metadata(self):
        """Return whether we have an ID.

        For the metadata we need an ID so that others can point at us.
        """
        return hasattr(self, 'id')

    @property
    def addable_to_source_repo(self):
        """Return whether we're actually a file."""
        if not hasattr(self, 'original_filepath'):
            return False
        if not hasattr(self, 'year'):
            return False
        if not self.kind in ('photos', 'videos'):
            return False
        return True

    def determine_filename_and_set_id(self, target_directory):
        """Return nice filename and set our ID

        Try and come up with a SEO-fiendly nice name based on the title. But
        should not overlap with an existing file in the target directory.
        """
        current_filename = os.path.basename(self.original_filepath).lower()
        base, ext = os.path.splitext(current_filename)
        if hasattr(self, 'title'):
            base = utils.slugify(self.title)
        while (base + ext) in os.listdir(target_directory):
            base += '_'
        filename = base + ext
        self.id = os.path.join(self.kind, unicode(self.year), filename)
        return filename


class Photo(MetadataItem):
    kind = 'photos'
    fields = PHOTO_FIELDS


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
                "Metadata file %s doesn't exist yet. We'll create it later.",
                self.filename)
        else:
            self.contents = json.load(open(self.filename))
        self.update_content_structure()

    def write(self):
        """Write our contents back to the metadata file."""
        json.dump(self.contents, open(self.filename, 'w'))

    def update_content_structure(self):
        """Fix up the content dict, if needed."""
        if not 'albums' in self.contents:
            self.contents['albums'] = {}
        for album_name in utils.ALBUMS:
            if album_name not in self.contents['albums']:
                self.contents['albums'][album_name] = []
        if not 'photos' in self.contents:
            self.contents['photos'] = {}
        if not 'videos' in self.contents:
            self.contents['videos'] = {}

    def add(self, item):
        assert item.addable_to_metadata
        if item.id in self.contents[item.kind]:
            logger.debug("Overwriting existing {id} in {kind}.".format(
                    id=item.id, kind=item.kind))
        # Check *_link(s) attributes. Add auto-references.
        # albums_links = [album1_id, album2_id]
        # Add our (if we're kind=videos) link to those two albums in their
        # videos_links attr.
        self.contents[item.kind][item.id] = item
