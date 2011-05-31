---
layout: post
title: open komodo is out
date: 2007-11-02T08:22:00.009-07:00
published: true
categories: [komodo, mozilla]
---

<p>The wraps are finally off <a href="http://www.openkomodo.com/">Open Komodo</a>!</p>

<ul>
<li>source: <a href="http://svn.openkomodo.com/openkomodo/browse/openkomodo/trunk">http://svn.openkomodo.com/openkomodo/browse/openkomodo/trunk</a></li>
<li>grok (an alternative to lxr): <a href="http://grok.openkomodo.com/source/search?q=koDirs">http://grok.openkomodo.com/source/search?q=koDirs</a></li>
<li>wiki: <a href="http://wiki.openkomodo.com/index.php/Main_Page">http://wiki.openkomodo.com/index.php/Main_Page</a></li>
<li>mailing lists: <a href="http://lists.openkomodo.com/mailman/listinfo">http://lists.openkomodo.com/mailman/listinfo</a></li>
<li>irc: irc.mozilla.org #komodo</li>
</ul>

<p><strong>Check it out.</strong></p>

<p>Quick build notes:</p>

<pre><code># Get the source
svn co http://svn.openkomodo.com/repos/openkomodo/trunk openkomodo
# Build Mozilla
cd openkomodo/mozilla
python build.py configure -k 1.0 --moz-src=cvs:1.8 --release \
    --no-strip --shared --tools
python build.py distclean all
cd ..
# Build Komodo
export PATH=`pwd`/util/black:$PATH   # Komodo's "bk" build tool
bk configure
bk build
# Run Komodo
bk run
</code></pre>

<p>If you have the <a href="http://svn.openkomodo.com/openkomodo/view/openkomodo/trunk/README.txt">build prerequisites</a> setup, you should be able to cut 'n paste the above. (Windows users, use the Windows-specific quick build steps in the README.txt.)</p>

<p>I have some (longer term) <a href="http://svn.openkomodo.com/openkomodo/browse/mk/trunk">plans</a> to reduce those build steps to:</p>

<pre><code>./configure.py
mk
</code></pre>
