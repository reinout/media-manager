import os


def absolute_expanded_path(path):
    """Return absolute path including expanded ``~``."""
    return os.path.abspath(os.path.expanduser(path))


DEFAULT_CONFIG = {
    'source_repo_location': absolute_expanded_path('~/media')
    }
