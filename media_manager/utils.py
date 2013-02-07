from __future__ import unicode_literals
from __future__ import print_function
from unicodedata import normalize
import os
import re

PUNCT_RE = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

ALBUMS = [
    "cycling",
    "familie",
    "construction",
    "trains",
    "modeltrains",
    "historicaltrains",
    "work",
    "csrdelft",
    "kerk",
    "school",
    ]


def absolute_expanded_path(path):
    """Return absolute path including expanded ``~``."""
    return os.path.abspath(os.path.expanduser(path))


def exists(*path_elements):
    """Handy variant on os.path.exists(), easier for tests."""
    return os.path.exists(os.path.join(*path_elements))


def slugify(text):
    """Return a slug from a string.

    Copied from http://flask.pocoo.org/snippets/5/.
    """
    result = []
    for word in PUNCT_RE.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode('-'.join(result)[:100])


def nice_filename(file_item, directory):
    """Return nice non-duplicate filename."""
    current = os.path.basename(file_item.original_filepath)
    title = getattr(file_item, 'title', None)
    filename = current.lower()
    base, ext = os.path.splitext(filename)
    if title:
        base = slugify(title)
    while (base + ext) in os.listdir(directory):
        base += '_'
    return base + ext
