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
    'albums',
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
        """Return whether we're actually a file that can be added."""
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


class Video(MetadataItem):
    kind = 'videos'
    fields = VIDEO_FIELDS


class Metadata(object):
    """Wrapper around a JSON file that holds the media metadata.

    """
    def __init__(self, source_repo_location):
        self.source_repo_location = source_repo_location
        self.filename = os.path.join(self.source_repo_location,
                                     METADATA_FILENAME)
        self.albums = {}
        for album_name in utils.ALBUMS:
            self.albums[album_name] = []
        self.photos = {}
        self.videos = {}

    def read(self):
        """Read the metadata file."""
        if not os.path.exists(self.filename):
            logger.warning(
                "Metadata file %s doesn't exist yet. We'll create it later.",
                self.filename)
        else:
            self.contents = json.load(open(self.filename))

    def write(self):
        """Write our contents back to the metadata file."""
        json.dump(self.contents, open(self.filename, 'w'), indent=4)

    def _get_contents(self):
        """Return nice dict, collected from our attributes."""
        result = {}
        result['albums'] = {}
        for key, values in self.albums.items():
            result['albums'][key] = list(set(values))
        result['photos'] = {}
        for id, photo in self.photos.items():
            result['photos'][id] = photo.as_dict()
        result['videos'] = {}
        for id, video in self.videos.items():
            result['videos'][id] = video.as_dict()
        return result

    def _set_contents(self, contents_dict):
        """Sync contents dict we're getting from JSON to our attributes."""
        self.albums = contents_dict['albums']
        for photo_info in contents_dict['photos'].values():
            photo = Photo(**photo_info)
            self.add(photo)
        for video_info in contents_dict['videos'].values():
            video = Video(**video_info)
            self.add(video)

    contents = property(_get_contents, _set_contents)

    def add(self, item):
        """Add photo or video."""
        assert item.addable_to_metadata
        items = getattr(self, item.kind)
        if item.id in items:
            logger.debug("Overwriting existing {id} in {kind}.".format(
                    id=item.id, kind=item.kind))
        # Check *_link(s) attributes. Add auto-references.
        # albums_links = [album1_id, album2_id]
        # Add our (if we're kind=videos) link to those two albums in their
        # videos_links attr.
        items[item.id] = item
        for album_name in getattr(item, 'albums', []):
            assert album_name in utils.ALBUMS
            self.albums[album_name].append(item.id)
