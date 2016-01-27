#!/usr/bin/env python

import sys
import re
import codecs
import itertools

def _lintpost(path):
    content = codecs.open(path, 'r', 'utf-8').read()
    header_idx = content.find('\n---')
    header_lines = content[:header_idx].splitlines(False)[1:]
    body = content[header_idx+4:].lstrip()

    # Note all Liquid tags and escapes, if necessary: possible these are
    # *django* template tags that should be shown literally.
    for hit in re.finditer(r"""(?<!['"]){{(?!['"])\s*(.*?)\s*}}""", body):
        s = hit.group(0)
        if '"' in s and "'" in s:
            escaped = None
        elif "'" in s:
            escaped = '{{"%s"}}}}' % s[:-2]
        else:
            escaped = "{{'%s'}}}}" % s[:-2]
        if escaped:
            yield "Liquid tag: %s  (use `%s` if need to escape it)" % (
                hit.group(0), escaped)
        else:
            yield "Liquid tag: %s  (**don't know how to escape this!**)" % s
    for hit in re.finditer(r"{%\s*(.*?)\s*%}", body):
        s = hit.group(0)
        if '"' in s and "'" in s:
            escaped = None
        elif "'" in s:
            escaped = '{{"%s"}}}' % s[:-1]
        else:
            escaped = "{{'%s'}}}" % s[:-1]
        if escaped:
            yield "Liquid tag: %s  (use `%s` if need to escape it)" % (
                hit.group(0), escaped)
        else:
            yield "Liquid tag: %s  (**don't know how to escape this!**)" % s

    _setext_h_re = re.compile(r'^(.+)[ \t]*\n(=+|-+)[ \t]*\n+', re.M)
    _atx_h_re = re.compile(r'''
        ^(\#{1,6})  # \1 = string of #'s
        [ \t]*
        (.+?)       # \2 = Header text
        [ \t]*
        (?<!\\)     # ensure not an escaped trailing '#'
        \#*         # optional closing #'s (not counted)
        \n+
        ''', re.X | re.M)
    for hit in itertools.chain(
            _setext_h_re.finditer(body),
            _atx_h_re.finditer(body)
            ):
        s = hit.group(0).strip()
        if "'" in s:
            yield "Header with single-quotes (might want smartquotes: `&#8216;` and `&#8217;`): %s" % s
        if '"' in s:
            yield "Header with double-quotes (might want smartquotes: `&#8220;` and `&#8221;`): %s" % s


#---- mainline

if __name__ == "__main__":
    for post in sys.argv[1:]:
        for issue in _lintpost(post):
            print '%s: %s' % (post, issue)
