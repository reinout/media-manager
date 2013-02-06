"""Contains the console script entrypoints.
"""
from __future__ import unicode_literals
from __future__ import print_function
import os


DEFAULT_REPO = os.path.abspath(os.path.expanduser('~/media'))
# ^^^ Be careful not to use this in tests, you can overwrite the actual
# metadata and files that way.
