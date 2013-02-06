import os


def absolute_expanded_path(path):
    """Return absolute path including expanded ``~``."""
    return os.path.abspath(os.path.expanduser(path))


IPHOTO_LOCATION = absolute_expanded_path('~/Pictures/iPhoto Library')

CATEGORIES = [
    "ligfiets",
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
