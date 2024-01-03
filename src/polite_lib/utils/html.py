"""
    Polite Lib
    Dict Tools
    Helpers for handling dicts

"""

from . import xlate


def anchor(url: str, title: str = None) -> str:
    """Create an anchor link in html with a given anchor and title string to use."""
    if not title:
        title = anchor
    return '<a href="%s">%s</a>' % (url, title)


def strip_markup(original: str) -> str:
    stripped = original
    if "<br>" in original:
        stripped = original.replace("<br>", " ")
    if "<br/>" in original:
        stripped = original.replace("<br>", " ")
    stripped = xlate.filter_html_tags(stripped)
    return stripped


# End File: polite-lib/src/polite-lib/utils/html.py
