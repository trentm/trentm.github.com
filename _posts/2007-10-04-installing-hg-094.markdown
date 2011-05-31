---
layout: post
title: installing hg 0.9.4
date: 2007-10-04T03:20:00.009-07:00
published: true
categories: [mercurial]
---

<p>Cleaning out some notes of mine, it seemed a shame to just throw out notes on installing hg. I'm happy to update this with sections for other platforms and other Linux distros if people send them my way.</p>

<h2>Installation on Ubuntu (&lt; Gutsy)</h2>

<p>Note: only Ubuntu Gutsy has hg 0.9.4, and my Ubuntu isn't yet Gutsy.</p>

<pre><code>sudo apt-get install python2.4 python2.4-dev
wget http://www.selenic.com/mercurial/release/mercurial-0.9.4.tar.gz
tar xzf mercurial-0.9.4.tar.gz
cd mercurial-0.9.4
sudo make install
which hg    # should be /usr/local/bin/hg
hg debuginstall
</code></pre>

<h2>Installation on Linux (with no package mgmt support):</h2>

<p>Presumably this works just as well on other Unix-y platforms.</p>

<pre><code># You must have a Python &gt;=2.4 installation and first on your PATH.
cd tmp
wget http://www.selenic.com/mercurial/release/mercurial-0.9.4.tar.gz
tar xzf mercurial-0.9.4.tar.gz
cd mercurial-0.9.4
python setup.py install
hg debuginstall
</code></pre>

<h2>Installation on Mac OS X (using MacPorts):</h2>

<pre><code>sudo port selfupdate
sudo port search mercurial
# ensure this is version &gt;= 0.9.4
sudo port install mercurial
</code></pre>

<h3>Troubleshooting : install fails with "Another version of this port (mercurial @0.9.1_0) is already active."</h3>

<pre><code>sudo port uninstall mercurial @0.9.1_0   # the old one
sudo port uninstall mercurial @0.9.4_0   # the broken new one
sudo port install mercurial
</code></pre>

<h2>Installation on other platforms (Windows, Solaris, FreeBSD, ...)</h2>

<p>Look for <a href="http://www.selenic.com/mercurial/wiki/index.cgi/BinaryPackages">an available binary package</a>.</p>
