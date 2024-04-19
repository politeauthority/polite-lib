"""
    Polite Lib
    File Tools
    File Tools
    A collections of tools for working with file systems.

"""
import hashlib
import os


def get_directory_size(directory_path: str) -> int:
    """Get the size of a directory in bytes. Will skip sym linked dirctories.
    Use polite_lib.bytes_to_human to get human readable size.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def get_extension(file_path: str) -> int:
    """Get the extension of a file based off it's path."""
    if "." not in file_path:
        return None
    dot = file_path.rfind(".")
    if len(file_path) == dot:
        return None
    return file_path[dot + 1:]


def md5_file(file_path: str) -> str:
    """Get the MD5 hash of a given file's contents.
    :unit-test: TestHash::test__md5_file()
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("Path does not exist: %s" % file_path)
    open_file = open(file_path, 'rb').read()
    return hashlib.md5(open_file).hexdigest()


# End File: polite-lib/src/polite-lib/file_tools/file_tools.py
