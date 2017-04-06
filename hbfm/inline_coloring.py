# -*- coding: utf-8 -*-
import re
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


class InlineColoringPreprocessor(Preprocessor):

    def run(self, lines):

        HEADER_REGEX = re.compile('\{\{color\(([^:]+)\)::([^\}]+)\}\}')  # maybe too much sensitive

        def replace(m):
            color = m.groups()[0]
            text = m.groups()[1]
            return u'<font color="%s">%s</font>' % (color, text)

        new_lines = []
        for line in lines:
            if HEADER_REGEX.search(line):
                line = HEADER_REGEX.sub(replace, line)
            new_lines.append(line)
        return new_lines


class InlineColoringExtension(Extension):
    """ Inilne Coloring Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        """ Add InlineColoringPreprocessor """
        md.preprocessors.add(
            "inline_coloring", InlineColoringPreprocessor(md), "_begin")


def makeExtension(*args, **kwargs):
    return InlineColoringExtension(*args, **kwargs)
