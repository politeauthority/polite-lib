"""
    Polite Lib
    Xlate
    A collection of tools to translate common items.

"""
import re


def filter_html_tags(message: str) -> str:
    """Remove all html tags from a message. This is helpful for creating the non fomatted text
    version of a message.
    """
    clean_text = re.sub(r"<[^>]*>", "", message)
    return clean_text


# End File: polite-tools/polite-lib/src/utils/xlate.py