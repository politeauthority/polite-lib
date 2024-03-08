"""
    Polite Lib
    Utils
    File Tools
    A collections of tools for working with file systems.

"""
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


# End File: polite-lib/src/polite-lib/utils/file_tools.py
