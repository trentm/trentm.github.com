---
layout: post
title: How to install MySQL-python 1.2.3c1 on Mac OS X
published: true
categories: [install, python, activestate]
---

<h2>Introduction</h2><p>Just a quick note on getting MySQL-python (aka <code>import MySQLdb</code>) 1.2.3c1 (the <a href="http://pypi.python.org/pypi/MySQL-python/">current latest version</a>) to build and install on Mac OS X, because I hit something that I didn't see mentioned in a number of similar posts.</p><p>Here are some links that discuss getting MySQL-python to build on Mac OS X:</p><ul><li><a href="http://www.keningle.com/?p=11">MySQL-Python and Apple OSX 10.5 (Leopard)</a></li>
<li><a href="http://antoniocangiano.com/2007/12/22/how-to-install-django-with-mysql-on-mac-os-x/">How to install Django with MySQL on Mac OS X</a></li>
<li><a href="http://friendlybit.com/tutorial/install-mysql-python-on-mac-os-x-leopard/">Install MySQL-python on Mac OS X (leopard)</a></li>
</ul><p>What follows are the steps (slightly different) that I needed to get MySQL-python to install.</p><a name='more'></a><br />
<h2>How to install MySQL-python on Mac OS X</h2><ol><li><p>My Setup</p><pre><code>Mac OS X 10.5/Intel
Xcode 3.0
ActivePython 2.6
</code></pre><p>Though I am using ActivePython, the issues should be the same for a Python from python.org.</p></li>
<li><p>Download and install MySQL 'pkg' format install for Mac OS X. For me this was the "Mac OS X 10.5 x86" package:  <code>mysql-5.1.34-osx10.5-x86.dmg</code> The following might work:</p><pre><code>wget http://dev.mysql.com/get/Downloads/MySQL-5.1/mysql-5.1.34-osx10.5-x86.dmg/from/http://mirror.csclub.uwaterloo.ca/mysql/
</code></pre></li>
<li><p>Download the <a href="http://pypi.python.org/pypi/MySQL-python/">latest MySQL-python package</a>.</p><pre><code>cd /tmp
wget http://pypi.python.org/packages/source/M/MySQL-python/MySQL-python-1.2.3c1.tar.gz
tar xzf MySQL-python-1.2.3c1.tar.gz
cd MySQL-python-1.2.3c1
</code></pre></li>
<li><p>Build it.</p><pre><code># ensure mysql_config is on your PATH
export PATH=$PATH:/usr/local/mysql/bin
python setup.py build
</code></pre><p>For me this failed as follows:</p><pre><code>gcc -arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -bundle -undefined dynamic_lookup build/temp.macosx-10.3-i386-2.6/_mysql.o -L/usr/local/mysql/lib -lmysqlclient_r -lz -lm -lmygcc -o build/lib.macosx-10.3-i386-2.6/_mysql.so
ld: warning in build/temp.macosx-10.3-i386-2.6/_mysql.o, file is not of required architecture
ld: warning in /usr/local/mysql/lib/libmysqlclient_r.dylib, file is not of required architecture
ld: warning in /usr/local/mysql/lib/libmygcc.a, file is not of required architecture
</code></pre><p>I didn't see this mentioned in others' post on this. I suspect they may not have hit this because they were building against the system Python (in /usr/bin/python, /System/Library/Frameworks/Python.framework/Versions/Current) which may have some tweaks to just handle this.</p><p>In any case the problem here is that my Python install (ActivePython 2.6) is a universal build (including i386 and ppc). By default distutils (the library behind <code>python setup.py build</code>) tries to build binary Python extensions for all the same architectures. However, the MySQL you just installed is only for x86 so it borks.</p><p>The fix is to use the ARCHFLAGS environment variable that distutils will pick up on to only build for your architecture:</p><pre><code>ARCHFLAGS=`arch` python setup.py build
</code></pre></li>
<li><p>Install it.</p><pre><code>sudo python setup.py install
</code></pre></li>
</ol>
