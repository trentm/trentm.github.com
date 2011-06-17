
# This is a Makefile for the `mk` tool. (Limited) details for that here:
# <http://github.com/ActiveState/mk>

import sys
import os
from os.path import join, dirname, normpath, abspath, exists, basename, expanduser
import codecs
import re
import difflib
from pprint import pprint
import json
import itertools
from glob import glob
import datetime

import mklib
assert mklib.__version_info__ >= (0,7,2)  # for `mklib.mk`
from mklib.common import MkError
from mklib import Task, mk, Alias
from mklib import sh


class run(Task):
    """run local Jekyll devserver"""
    def make(self):
        os.system("_stuff/devserver")

class post(Task):
    """start a new post"""
    def make(self):
        title = query("Title")
        slug = query("Slug", _slugify(title))
        categories = [c.strip()
            for c in re.split(r'\s*[,\s]\s*', query("Categories"))]
        
        now = datetime.datetime.now()
        path = join(self.dir,
            now.strftime("_posts/%Y-%m-%d-") + slug + ".markdown")
        title_esc = title
        if ':' in title_esc or '"' in title_esc:
            title_esc = '"%s"' % title_esc.replace('"', '\\"')
        template = [
            "---",
            "layout: post",
            "title: %s" % title_esc,
            "published: true",
            "date: %s" % now.isoformat(),
        ]
        if categories:
            template.append("categories: [%s]" % ", ".join(categories))
        template += [
            "---",
            ""
        ]
        codecs.open(path, 'w', 'utf-8').write('\n'.join(template))
        self.log.info("Wrote '%s'.", path)
        os.system("git add %s" % path)
        os.system("open -a 'Komodo IDE.app' %s" % path)

class lint(Task):
    """Lint the latest post (or path in POST envvar)."""
    def make(self):
        if "POST" in os.environ:
            path = os.environ["POST"]
        else:
            paths = glob(join(self.dir, "_posts", "????-??-??-*.markdown"))
            paths.sort()
            path = paths[-1]
        print "# lint", path
        for issue in _lintpost(path):
            print issue

class lintall(Task):
    """Lint all posts."""
    def make(self):
        paths = glob(join(self.dir, "_posts", "????-??-??-*.markdown"))
        for path in paths:
            print "# lint %s" % path
            for issue in _lintpost(path):
                print issue


#---- internal support stuff

## {{{ http://code.activestate.com/recipes/577099/ (r1)
def query(question, default=None):
    s = question
    if default:
        s += " [%s]" % default
    s += ": "
    answer = raw_input(s)
    answer = answer.strip()
    if not answer:
        return default
    return answer
## end of http://code.activestate.com/recipes/577099/ }}}

## {{{ http://code.activestate.com/recipes/577257/ (r1)
_slugify_strip_re = re.compile(r'[^\w\s-]')
_slugify_hyphenate_re = re.compile(r'[-\s]+')
def _slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.

    From Django's "django/template/defaultfilters.py".
    """
    import unicodedata
    if not isinstance(value, unicode):
        value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(_slugify_strip_re.sub('', value).strip().lower())
    return _slugify_hyphenate_re.sub('-', value)
## end of http://code.activestate.com/recipes/577257/ }}}

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
            print "Header with single-quotes (might want `&#8216;` and `&#8217;`): %s" % s
        if '"' in s:
            print "Header with double-quotes (might want `&#8220;` and `&#8221;`): %s" % s

def _get(url):
    import urllib
    return urllib.urlopen(url).read()
