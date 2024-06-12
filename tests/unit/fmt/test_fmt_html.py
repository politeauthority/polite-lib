"""
    Polite Lib
    Test Format Html
    Tests File: polite-lib/src/polite-lib/utils/fmt_html.py

"""
from polite_lib.fmt import fmt_html


class TestFmtHtml:

    def test__anchor(self):
        """Tests that we create an html anchor.
        :method: fmt_html.anchor()
        """
        assert fmt_html.anchor("https://google.com", "Google") == '<a href="https://google.com">Google</a>'

    def test__code(self):
        """Tests that we add commas in the correct places.
        :method: fmt_html.code()
        """
        assert fmt_html.code("Wrap this in code") == "<code>Wrap this in code</code>"

    def test__strip_markup(self):
        """Tests that we strip markup properly.
        :method: fmt_html.code()
        """
        assert fmt_html.strip_markup("") == ""
        assert fmt_html.strip_markup("hello<br>") == "hello "

    def test__table_from_dict(self):
        """Tests that create an html table from a dict.
        :method: fmt_html.table_from_dict()
        """
        assert fmt_html.table_from_dict("") == ""
        test_dict = {
            "hello": "value",
            "hello2": "value1"
        }
        expected = "<table><tr><td><b>hello</b></td><td>value</td></tr><tr><td><b>hello2</b></td>"
        expected += "<td>value1</td></tr></table>"
        assert fmt_html.table_from_dict(test_dict) == expected

    def test__unordered_list(self):
        """Tests that create an html table from a dict.
        :method: fmt_html.unordered_list()
        """
        assert fmt_html.unordered_list("") == "<ul></ul>"

        test_list = ["hello", "world"]
        assert fmt_html.unordered_list(test_list) == "<ul><li>hello</li><li>world</li></ul>"

# End File: politeauthority/polite-lib/tests/unit/fmt/test_fmt_html.py
