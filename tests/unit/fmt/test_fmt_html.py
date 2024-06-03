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

# End File: politeauthority/polite-lib/tests/unit/fmt/test_fmt_html.py
