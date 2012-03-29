#!/usr/bin/env python

"""Slap in some inline styles to fight wordpress dropping style blocks.

This is currently only for blog.nodejs.org.
"""

import os
import sys
import re
import codecs

htmlpath = sys.argv[1]
assert htmlpath.endswith(".html")
origContent = codecs.open(htmlpath, 'r', 'utf8').read()
content = origContent

# h1
content = re.sub(r'<h1 ',
    '<h1 style="margin: 48px 0 24px 0;" ',
    content)

# code (but not <pre><code>)
content = re.sub(r'(?<!<pre>)<code>',
    '<code style="color: #999; background-color: #2f2f2f; border: 1px solid #484848; padding: 0.2em 0.4em;">',
    content)

# pre
content = re.sub(r'<pre>',
    '<pre style="overflow: auto; color: #999; background-color: #2f2f2f; border: 1px solid #484848; padding: 5px">',
    content)

if content != origContent:
    codecs.open(htmlpath, 'w', 'utf8').write(content)
    print "Wrote '%s'." % htmlpath
else:
    print "No change in '%s'." % htmlpath
