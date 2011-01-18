
# This is a Makefile for the `mk` tool. (Limited) details for that here:
# <http://github.com/ActiveState/mk>

import sys
import os
from os.path import join, dirname, normpath, abspath, exists, basename, expanduser
import re
import difflib
from pprint import pprint

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


#---- internal support stuff

def _get(url):
    import urllib
    return urllib.urlopen(url).read()
    
