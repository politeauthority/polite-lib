"""
    Polite Lib - Tests
    Fike Tools

"""
import os

import pytest

from polite_lib.file_tools import file_tools

TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "../../data/"
)


class TestFileTools:

    def test__get_directory_size(self):
        """Test can get a diretory's size in bytes.
        :method: file_tools.get_directory_size()
        """
        directory_to_size = TEST_DATA_DIR
        x = file_tools.get_directory_size(directory_to_size)
        import ipdb; ipdb.set_trace()

        assert 10 == file_tools.get_directory_size(directory_to_size)

    def test__get_filename(self):
        """Test can get a the filename from a file path.
        :method: file_tools.get_filename()
        """
        filename = "/a/full/file_path/test_file_tools.py"
        assert "test_file_tools.py" == file_tools.get_filename(filename)

    def test__get_extension(self):
        """Test can get a file's extension.
        :method: file_tools.get_extension()
        """
        filename = "test_file_tools.py"
        assert "py" == file_tools.get_extension(filename)

    def test__get_hash(self):
        """Test that we convert a file's contents to a hash.
        :method: file_tools.get_hash()
        """
        with pytest.raises(FileNotFoundError):
            assert file_tools.get_hash("/does-not-exist")
        file_to_hash = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "../../data/file_tools_hash.txt")
        assert "0c8263ef81be7da66923df494a259053" == file_tools.get_hash(file_to_hash)


# End File: polite-lib/test/unit/file_tools/test_file_tools.py
