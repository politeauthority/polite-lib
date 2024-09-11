
"""
    Polite Lib
    Test - Xlate
    Tests File: polite-lib/src/polite-lib/utils/xlate.py

"""
from pytest import raises

from polite_lib.utils import xlate


class TestUtilsXlate:

    def test__filter_html_tags(self):
        """
        :method: xlate.filter_html_tags
        """
        test_data = "<h1>heres a bunch of</h1><table><thead><tr><td>yeah</td><td>Not DOne</td><tr>"
        test_data += "</thead>"
        expected = "heres a bunch ofyeahNot DOne"
        result = xlate.filter_html_tags(test_data)
        assert result == expected

    def test__url_decode(self):
        """
        :method: xlate.url_decode
        """
        assert xlate.url_decode("haproxy%3A2.0.12") == "haproxy:2.0.12"

    def test__url_encode(self):
        """
        :method: xlate.url_encode
        """
        assert xlate.url_encode("haproxy:2.0.12") == "haproxy%3A2.0.12"

    def test__convert_any_to_int(self):
        """
        :method: xlate.convert_any_to_int
        """
        assert not xlate.convert_any_to_int(None)
        assert xlate.convert_any_to_int("1") == 1
        assert xlate.convert_any_to_int(5) == 5

    def test__convert_bool_to_int(self):
        """Test that bools are properly converted to ints, even when the input is a string value, to
        the best that we can.
        :method: xlate.convert_bool_to_int
        """
        assert xlate.convert_bool_to_int(True) == 1
        assert xlate.convert_bool_to_int(False) == 0
        assert xlate.convert_bool_to_int("True") == 1
        assert xlate.convert_bool_to_int("False") == 0
        assert not xlate.convert_bool_to_int("Falsy")

    def test__convert_int_to_bool(self):
        """
        :method: xlate.convert_int_to_bool
        """
        assert not xlate.convert_int_to_bool(None)
        assert xlate.convert_int_to_bool(1)
        assert xlate.convert_int_to_bool(0) == False

    def test__convert_list_to_str(self):
        """
        :method: xlate.convert_list_to_str
        """
        assert not xlate.convert_list_to_str([])
        # with raises(AttributeError):
        #     assert xlate.convert_list_to_str("hello")
        assert xlate.convert_list_to_str(["hello"])
        test_list = ["hello", "how", "are", "you"]
        assert xlate.convert_list_to_str(test_list) == "hello,how,are,you"

    def test__convert_str_to_bool(self):
        """
        :method: xlate.convert_str_to_bool
        """
        assert not xlate.convert_str_to_bool(None)
        assert xlate.convert_str_to_bool("true")
        assert xlate.convert_str_to_bool("1")
        assert xlate.convert_str_to_bool(1)
        assert not xlate.convert_str_to_bool("false")
        assert not xlate.convert_str_to_bool("0")
        assert not xlate.convert_str_to_bool(0)
        with raises(AttributeError):
            assert xlate.convert_str_to_bool("hello")

    def test__rest_to_snake_case(self):
        """Test that we can convert rest case to snake case.
        :method: xlate.rest_to_snake_case()
        """
        assert xlate.rest_to_snake_case("module") == "module"
        assert xlate.rest_to_snake_case("my-module-is-great") == "my_module_is_great"

    def test__snake_to_camel_case(self):
        """Test that we can convert snake case to camel case.
        :method: xlate.snake_to_camel_case()
        """
        assert xlate.snake_to_camel_case("module") == "Module"
        assert xlate.snake_to_camel_case("my_module_is_great") == "MyModuleIsGreat"
        assert xlate.snake_to_camel_case("image_build_waiting") == "ImageBuildWaiting"

    def test__base64_decode(self):
        """Test that we can decode base64 properly.
        :method: xlate.base64_decode()
        """
        assert xlate.base64_decode("c29tZXRoaW5nIHRvIGRlY29kZQ==") == "something to decode"

    def test__base64_encode(self):
        """Test that we can encode base64 properly.
        :method: xlate.base64_encode()
        """
        assert xlate.base64_encode("something to encode") == "c29tZXRoaW5nIHRvIGVuY29kZQ=="

    def test__slugify(self):
        """Test that we can turn a butterfly into a slug.
        :method: xlate.slugify()
        """
        assert "hello-world" == xlate.slugify("hello world")
        assert "hello-world" == xlate.slugify("Hello World")
        assert "hello-world" == xlate.slugify("hello-world")
        assert "hello-world" == xlate.slugify("hello/world")


# End File: politeauthority/polite-lib/test/unit/utils/test_xlate.py
