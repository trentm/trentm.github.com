---
layout: post
title: eol.py 0.7.4 -- Python 3 support
published: true
categories: [python, programming]
---

<h3>Where?</h3>

<ul>
<li>Project Page: <a href="http://github.com/trentm/eol">http://github.com/trentm/eol</a></li>
<li>PyPI: <a href="http://pypi.python.org/pypi/eol/">http://pypi.python.org/pypi/eol/</a></li>
</ul>

<h3>What's new?</h3>

<ul>
<li>Python 3 support (not heavily tested yet)</li>
<li>Starter test suite</li>
</ul>

<p>Full changelog: <a href="http://github.com/trentm/eol/tree/master/CHANGES.md#files">http://github.com/trentm/eol/tree/master/CHANGES.md#files</a></p>

<h3>What is &#8216;eol&#8217;?</h3>

<p><code>eol</code> is both a command-line script <code>eol</code> and a Python module <code>eol</code> for working
with end-of-line chars in text files.</p>

<h4>Command line usage</h4>

<pre><code># list EOL-style of files
$ eol *
configure: Unix (LF)
build.bat: Windows (CRLF)
snafu.txt: Mixed, predominantly Unix (LF)

# find files with a given EOL-style
$ eol -f CRLF -x .svn -r ~/src/python
/Users/trentm/src/python/Doc/make.bat
/Users/trentm/src/python/Lib/email/test/data/msg_26.txt
/Users/trentm/src/python/Lib/encodings/cp720.py
...

# convert EOL-style of files
$ eol -c LF foo.c 
converted `foo.c' to LF EOLs
</code></pre>

<h4>Module usage</h4>

<pre><code>&gt;&gt;&gt; import eol
&gt;&gt;&gt; eol.eol_info_from_path("configure")
('\n', '\n')         # (&lt;detected-eols&gt;, &lt;suggested-eols&gt;)
&gt;&gt;&gt; eol.eol_info_from_path("build.bat")
('\r\n', '\r\n')
&gt;&gt;&gt; eol.eol_info_from_path("snafu.txt")
(&lt;class 'eol.MIXED'&gt;, '\n')
</code></pre>

<p>See the <a href="http://github.com/trentm/eol#readme">README</a> for full usage
information.</p>
