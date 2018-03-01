# -*- coding: utf-8 -*-
import re
try:
    import urllib2
except ImportError:
    import urllib.parse as urllib2
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


class QuoteURIHashPreprocessor(Preprocessor):

    def run(self, lines):

        HEADER_REGEX = re.compile('\]\(#([^\)]+)\)')  # maybe too much sensitive

        def uriquote(m):
            value = m.groups()[0]
            value = value.encode("utf-8", "ignore")
            value = urllib2.quote(value)
            return '](#%s)' % value

        new_lines = []
        for line in lines:
            if HEADER_REGEX.search(line):
                line = HEADER_REGEX.sub(uriquote, line)
            new_lines.append(line)
        return new_lines


class QuoteURIHashExtension(Extension):
    """ Quote URI Hash Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        """ Add QuoteURIHashPreprocessor """
        md.preprocessors.add(
            "quote_uri_hash", QuoteURIHashPreprocessor(md), "_begin")


def makeExtension(*args, **kwargs):
    return QuoteURIHashExtension(*args, **kwargs)
