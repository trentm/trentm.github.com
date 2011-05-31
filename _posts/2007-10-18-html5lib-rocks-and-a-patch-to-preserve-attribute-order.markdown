---
layout: post
title: html5lib rocks (and a patch to preserve attribute order)
date: 2007-10-18T08:08:00.009-07:00
published: true
categories: [python, komodo, programming]
---

<p>I've been playing with the Python <a href="http://code.google.com/p/html5lib/">html5lib package</a> -- having come across it reading <a href="http://intertwingly.net/blog/">Sam Ruby's blog</a>. What a fantastically useful library!</p>

<p>Originally my interest in it was with the discussion surrounding <a href="http://wiki.whatwg.org/wiki/Sanitization_rules">santization</a>, and I expect to use it for that later, but today I've been playing with some general parse/filter/serialize code to support some preprocessing of HTML documentation for <a href="http://www.activestate.com/openkomodo/">Open Komodo</a>.</p>

<p>My code looks like this:</p>

<pre><code>import sys
from html5lib import treebuilders, treewalkers
from html5lib.serializer.xhtmlserializer import XHTMLSerializer

def filter_play(path):
    p = html5lib.XHTMLParser(tree=treebuilders.getTreeBuilder("simpletree"))
    f = open(path)
    dom = p.parse(f)

    walker = treewalkers.getTreeWalker("simpletree")
    stream = walker(dom)
    #stream = MyPreprocessingFilter()

    s = XHTMLSerializer()
    outputter = s.serialize(stream)

    for item in outputter:
        sys.stdout.write(item)

filter_play(sys.argv[1])
</code></pre>

<p>One thing that bugged me a little with the output generated with this is that attributes on HTML elements get sorted, i.e. their order is not preserved. While totally cool for correctness, this reduces the utility of using <code>diff</code> or similar for comparing input with output. As well, I work on the <a href="http://www.activestate.com/Products/komodo_ide/">Komodo</a> IDE/editor and would like to consider using <code>html5lib</code> for an HTML reflow/beautifier feature at some point. Preserving attribute order for this will be important.</p>

<p>To that end, here is <a href="http://dl.getdropbox.com/u/1301040/blog/2007/10/html5lib_preserve_attr_order.patch">a small patch that adds the ability to preserve attribute order</a> in serialized output.  To use it:</p>

<ol>
<li>You need <a href="http://pypi.python.org/pypi/Ordered%20Dictionary/">odict.py</a>.</li>
<li><p>You need to change the above code to:</p>

<pre><code>...
s = XHTMLSerializer(preserve_attr_order=True)
...
</code></pre></li>
</ol>

<p>Obviously this isn't something that would be ready to check-in to <code>html5lib</code>. Reasons why:</p>

<ul>
<li>It only works for the "simpletree" treebuilder/treewalker. I'm not sure if it is feasible/practical to get it to work with some of the others (e.g. dom).</li>
<li>It unconditionally requires an external non-standard module (<code>odict.py</code>).</li>
<li>It should be optional on the parser because (a) using <code>OrderedDict</code> instead of <code>dict</code> would presumably have an undesired perf impact and (b) the attribute order normalization could be <em>desirable</em> for many users.</li>
</ul>

<p>Maybe a better solution would be a custom "roundtriptree" tree type? Anyway, just throwing this up here to perhaps come back to later. I have to dig into the <code>html5lib</code> discussion list to see if this has come up before.</p>
