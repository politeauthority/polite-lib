"""

"""

from polite_lib.utils import dict_tools


class TestUtilsDictUtils:

    def test__key_exists(self):
        """
        :method: dict_utils.key_exists()
        """
        data = {
            "some": "shit",
            "more": {
                "complicated": {
                    "details": 1
                }
            }
        }
        assert dict_tools.key_exists(data, "some")
        assert dict_tools.key_exists(data, "more.complicated")
        assert not dict_tools.key_exists(data, "nonexistant")

    def test__key_with_value(self):
        """
        :method: dict_utils.key_with_value()
        """
        data = {
            "some": "shit",
            "more": {
                "complicated": {
                    "details": 1,
                    "empty": None
                }
            }
        }
        assert "shit" == dict_tools.key_with_value(data, "some")
        assert {"details": 1, "empty": None} == dict_tools.key_with_value(data, "more.complicated")
        assert not dict_tools.key_with_value(data, "more.complicated.empty")
        assert not dict_tools.key_exists(data, "nonexistant")

    def test__drop_keys(self):
        """
        :method: dict_utils.test__drop_keys()
        """
        data = {
            "some": "shit",
            "more": {
                "complicated": {
                    "details": 1,
                    "empty": None
                }
            }
        }
        assert "more" not in dict_tools.drop_keys(data, ["more"])

# End File: polite-lib/test/unit/utils/test_dict_utils.py
