from zope import interface


class IPhoto(interface.Interface):
    """A photo (and its metadata)"""


class IVideo(interface.Interface):
    """A video (and its metadata)"""


class ITxtFile(interface.Interface):
    """A sphinx ``.txt`` file"""
    # .write() method?
