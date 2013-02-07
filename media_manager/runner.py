"""Contains the console script entrypoints.
"""
from __future__ import unicode_literals
from __future__ import print_function
import os

from media_manager.sourcerepo import SourceRepo

DEFAULT_REPO = os.path.abspath(os.path.expanduser('~/media'))
# ^^^ Be careful not to use this in tests, you can overwrite the actual
# metadata and files that way.


def add_video():
    source_repo = SourceRepo(DEFAULT_REPO)
    kind = 'video'
    filename = sys.argv[1]
    # Ask for year.
    year = 2011
    # Ask for title.
    title = None
    # Ask for album.
    albums = []
    # Well, perhaps construct a Video object and pass that around?
