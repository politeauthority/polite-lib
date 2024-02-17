"""
    Polite Lib
    Utils
    File Tools
    A collections of tools for working with file systems.

"""
import os


def get_directory_size(directory_path: str) -> int:
    """Get the size of a directory. Will skip sym linked dirctories.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


# End File: polite-lib/src/polite-lib/utils/file_tools.py
