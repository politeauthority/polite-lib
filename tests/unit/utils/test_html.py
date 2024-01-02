
"""
    Polite Lib
    Test Unit
    Utils
    html
    Tests File: polite-lib/src/polite-lib/utils/html.py

"""
from polite_lib.utils import html


class TestUtilsHtml:

    def test__anchor(self):
        """
        :method: html.anchor
        """
        expected = '<a href="https://google.com">https://google.com</a>'
        assert expected == html.anchor("https://google.com")
        expected = '<a href="https://google.com">Google</a>'
        assert expected == html.anchor("https://google.com", "Google")

    def test_strip_markup(self):
        """
        :method: html.strip_markup
        """
        markup = "<h1>Hello World</h1> We have something<br> to <i>say</i>"
        expected = "Hello World We have something  to say"
        assert expected == html.strip_markup(markup)

# End File: polite-lib/test/unit/utils/html.py
