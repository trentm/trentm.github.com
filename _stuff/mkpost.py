#!/usr/bin/env python

import sys
import os
from os.path import join, dirname, normpath, abspath, exists, basename, expanduser
import codecs
import re
from pprint import pprint
import datetime


#---- globals

TOP = dirname(dirname(__file__))


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




#---- mainline

title = query("Title")
slug = query("Slug", _slugify(title))
# TODO: would be nice to emit current categories in use before
categories = [c.strip()
    for c in re.split(r'\s*[,\s]\s*', query("Categories", ""))]

now = datetime.datetime.now()
path = join(TOP, now.strftime("_posts/%Y-%m-%d-") + slug + ".markdown")
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
print("Wrote '%s'" % path)
os.system("git add %s" % path)
os.system("open -a 'Komodo IDE 8.app' %s" % path)