# -*- coding: utf-8 -*-
import re
from markdown import Markdown
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


class InlineListPreprocessor(Preprocessor):

    def run(self, lines):
        HEADER_REGEX = re.compile('\{\{inline\(list\)::\n(.*?)\n\}\}', re.DOTALL)  # maybe too much sensitive

        def replace(m):
            text = m.groups()[0]
            md = Markdown()
            table = md.convert(text).replace("\n", "")
            return table

        new_lines = HEADER_REGEX.sub(replace, "\n".join(lines))
        return new_lines.split("\n")


class InlineListExtension(Extension):
    """ InlineList Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        """ Add InlineListPreprocessor """
        md.preprocessors.add(
            "inline_list", InlineListPreprocessor(md), "_begin")


def makeExtension(*args, **kwargs):
    return InlineListExtension(*args, **kwargs)
