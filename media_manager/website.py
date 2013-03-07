"""Generator for http://reinout.vanrees.org/media

Create, initially, files for sphinx. Later on, Django might serve them.

Also copy and convert files. We're not serving /media directly.

"""
from __future__ import unicode_literals
from __future__ import print_function
import json
import logging
import os

from zope import component
from zope import interface

from media_manager import interfaces
from media_manager import utils
from media_manager import metadata


logger = logging.getLogger(__name__)


class VideoTxtFile(object):
    interface.implements(interfaces.ITxtFile)
    component.adapts(interfaces.IVideo)



class Website(object):
    """Wrapper around the website's target directory structure.
    """

    def __init__(self, metadata, website_location):
        """Set up the website object.

        Metadata: a metadata object.

        Website location: the directory where the actual website looks for its
        /media part. Probably we store it ourselves.
        """
        self.metadata = metadata
        self.website_location = website_location

    def write_file_per_item(self):
        """For every photo or video, write an .txt file for sphinx.

        Use zope adapters for this!!!
        """
        pass
