"""
    Polite Lib
    File Tools
    File Tools
    A collections of tools for working with file systems.

"""
import hashlib
import os

from polite_lib.utils import convert
from polite_lib.utils import mathy


def get_directory_size(directory_path: str) -> int:
    """Get the size of a directory in bytes. Will skip sym linked dirctories.
    Use polite_lib.bytes_to_human to get human readable size.
    :unit-test: TestFileTools::test__get_directory_size()
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def get_filename(file_path: str) -> str:
    """Get the filename from a filepath.
    :unit-test: TestFileTools::test__get_filename()
    """
    if "/" in file_path:
        return file_path[file_path.rfind("/") + 1:]
    else:
        return file_path


def get_extension(file_path: str) -> int:
    """Get the extension of a file based off it's path.
    :unit-test: TestFileTools::test__get_extension()
    """
    if "." not in file_path:
        return None
    dot = file_path.rfind(".")
    if len(file_path) == dot:
        return None
    return file_path[dot + 1:]


def get_hash(file_path: str) -> str:
    """Get the MD5 hash of a given file's contents.
    :unit-test: TestFileTools::test__get_hash()
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("Path does not exist: %s" % file_path)
    open_file = open(file_path, 'rb').read()
    return hashlib.md5(open_file).hexdigest()


def get_disk_info(path_of_partion: str = "/", human: bool = False) -> dict:
    """
    """
    statvfs = os.statvfs(path_of_partion)
    ret = {
        "file_system_size": statvfs.f_frsize * statvfs.f_blocks,
        "file_system_free": statvfs.f_frsize * statvfs.f_bfree,
        "file_system_available": statvfs.f_frsize * statvfs.f_bavail,
    }
    ret["percent_free"] = mathy.percentize(ret["file_system_free"], ret["file_system_size"])
    ret["percent_available"] = mathy.percentize(
        ret["file_system_available"],
        ret["file_system_size"])
    if human:
        ret["file_system_size"] = convert.bytes_to_human(["file_system_size"])
        ret["file_system_free"] = convert.bytes_to_human(["file_system_free"])
        ret["file_system_available"] = convert.bytes_to_human(["file_system_available"])
    return ret


# End File: polite-lib/src/polite-lib/file_tools/file_tools.py
