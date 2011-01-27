
# This is a Makefile for the `mk` tool. (Limited) details for that here:
# <http://github.com/ActiveState/mk>

import sys
import os
from os.path import join, dirname, normpath, abspath, exists, basename, expanduser
import codecs
import re
import difflib
from pprint import pprint
import itertools
from glob import glob

import mklib
assert mklib.__version_info__ >= (0,7,2)  # for `mklib.mk`
from mklib.common import MkError
from mklib import Task, mk
from mklib import sh


class feeds(Task):
    """diff feed"""
    def make(self):
        print "http://feeds.feedburner.com/trentmick"
        print "http://localhost:4000/atom.xml"
        print "http://www.blogger.com/feeds/1552913144533093368/posts/default"

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

class lint2(Task):
    def make(self):
        for issue in _lintpost('/Users/trentm/tm/trentm.github.com/_posts/2010-06-14-django-markdown-deux-django-app.markdown'):
            print issue

class pull(Task):
    def make(self):
        ns = "{http://www.w3.org/2005/Atom}"
        from xml.etree import ElementTree as ET
        tree = ET.parse(glob(join(self.dir, "d/*.xml"))[0]).getroot()
        marker = "python-markdown2"
        for entry in tree:
            title = entry.find('{http://www.w3.org/2005/Atom}title')
            if title is not None and marker in title.text:
                break
        else:
            return
        
        post = _post_from_blogger_entry(entry)
        pprint(post)
        path = join(self.dir, "_posts", post["path"])
        codecs.open(path, 'w', 'utf-8').write("%(header)s\n%(content)s" % post)
        print "'%s' written" % path


#---- internal support stuff

def _post_from_blogger_entry(entry):
    ns = "{http://www.w3.org/2005/Atom}"
    post = {}
    post["title"] = entry.find(ns+"title").text
    post["slug"] = _slugify(post["title"])
    post["pub_date"] = entry.find(ns+"published").text.split("T",1)[0] 
    post["content"] = entry.find(ns+"content").text
    post["tags"] = []
    for cat in entry.findall(ns+"category"):
        if cat.get("scheme") == "http://www.blogger.com/atom/ns#":
            post["tags"].append(cat.get("term"))
    post["path"] = "%(pub_date)s-%(slug)s.markdown" % post
    post["header"] = """---
layout: post
title: %s
published: true
categories: [%s]
---
""" % (post["title"], ', '.join(post["tags"]))
    return post
    

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
    
