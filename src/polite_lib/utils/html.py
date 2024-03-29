"""
    Polite Lib
    Html
    Tools for writing html

"""

from . import xlate


def anchor(url: str, title: str = None) -> str:
    """Create an anchor link in html with a given anchor and title string to use."""
    if not title:
        title = url
    return '<a href="%s">%s</a>' % (url, title)


def strip_markup(original: str) -> str:
    stripped = original
    if "<br>" in original:
        stripped = original.replace("<br>", " ")
    if "<br/>" in original:
        stripped = original.replace("<br>", " ")
    stripped = xlate.filter_html_tags(stripped)
    return stripped


def table_from_dict(the_dict: dict, t_format=["bold_key"]) -> str:
    """Create a vertical html table from a dictonary."""
    if not the_dict:
        return ""
    table = "<table>"
    for key, value in the_dict.items():
        key_print = key
        if "bold_key" in t_format:
            key_print = "<b>%s</b>" % key_print
        table += "<tr><td>%s</td><td>%s</td></tr>" % (key_print, str(value))
    table += "</table>"
    return table

# End File: polite-lib/src/polite-lib/utils/html.py
