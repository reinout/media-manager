import logging
import os
import plistlib

from media_manager import config

ALBUMDATA = 'AlbumData.xml'

logger = logging.getLogger(__name__)


class Photo(object):

    def __init__(self, infodict):
        self.infodict = infodict


class Album(object):

    def __init__(self, infodict):
        self.infodict = infodict


class Event(Album):
    pass


class Iphoto(object):
    """Wrapper around iphoto library."""

    def __init__(self, iphoto_location):
        self.iphoto_location = iphoto_location

    def read(self):
        """Read in the album data."""
        albumdata_filename = os.path.join(self.iphoto_location, ALBUMDATA)
        self.albumdata = plistlib.readPlist(albumdata_filename)
        self._photos = self.albumdata['Master Image List']
        self._albums_and_events = self.albumdata['List of Albums']

    def extract_photos(self):
        """Extract info on photos from the albumdata.

        Filter out the ones we don't want.
        """
        logger.debug("Found %s photos in total.", len(self._photos))
        for infodict in self._photos.values():
            photo = Photo(infodict)

    def extract_albums_and_events(self):
        """Extract info on albums and events from the albumdata.

        Filter out the ones we don't want.
        """
        logger.debug("Found %s albums/events in total.",
                     len(self._albums_and_events))
        for infodict in self._albums_and_events:
            album_type = infodict['Album Type']
            if album_type == 'Regular':
                album = Album(infodict)
            elif album_type == 'Event':
                event = Event(infodict)
            elif album_type == 'Folder':
                event = Event(infodict)
            else:
                # 'Smart'
                logger.debug("Unused album type: %s", album_type)


if __name__ == '__main__':
    iphoto = Iphoto(config.IPHOTO_LOCATION)
    iphoto.read()
    iphoto.extract_albums_and_events()
    iphoto.extract_photos()
