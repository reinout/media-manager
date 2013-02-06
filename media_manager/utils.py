import os


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
