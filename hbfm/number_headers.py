# -*- coding: utf-8 -*-
import re
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension


class NumberHeadersPreprocessor(Preprocessor):

    def run(self, lines):

        HEADER_REGEX = re.compile('^(#+)(.*)')
        NUM_HEADERS = 6
        counter = [0, 0, 0, 0, 0, 0]

        section_number = {}  # key: text, value: text with number

        new_lines = []
        for line in lines:
            m = HEADER_REGEX.match(line)
            if m:
                header_spec = m.groups()[0]
                header_num = len(header_spec)
                header_text = m.groups()[1].lstrip()
                header_num = header_num - 2
                # h1 は除外
                if(header_num < 0):
                    new_lines.append(line)
                else:
                    for i in range(header_num + 1, NUM_HEADERS):
                        counter[i] = 0
                    counter[header_num] += 1

                    section = [str(x) for x in counter if x != 0]
                    # if(len(section) == 1):
                    #     section.append('0')

                    section_text = '.'.join(section)

                    new_line = "%s %s. %s" % (
                        header_spec, section_text, header_text)
                    new_lines.append(new_line)

                    section_number[header_text] = section_text
            else:
                new_lines.append(line)

        CROSS_REFERENCE_REGEX = re.compile("\[([^\]]+)\]\(#([^\)]+)\)")

        def replace(m):
            text = m.groups()[0]
            link = m.groups()[1]
            if text not in section_number.keys():
                print(u"ERROR: Section title {} not found".format(text))
            return "[%s. %s](#%s)" % (section_number[text], text, link)

        renew_lines = []
        for line in new_lines:
            if CROSS_REFERENCE_REGEX.search(line):
                line = CROSS_REFERENCE_REGEX.sub(replace, line)
            renew_lines.append(line)
        return renew_lines


class NumberHeadersExtension(Extension):
    """ Number Headers Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        """ Add Number Headers preprocessor """
        md.preprocessors.add(
            "num_header", NumberHeadersPreprocessor(md), "_begin")


def makeExtension(*args, **kwargs):
    return NumberHeadersExtension(*args, **kwargs)
