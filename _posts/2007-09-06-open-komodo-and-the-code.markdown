---
layout: post
title: open komodo and the code
date: 2007-09-06T01:57:00.009-07:00
published: true
categories: [komodo, mozilla]
---

<p>Yesterday we (ActiveState) announced <a href="http://www.activestate.com/openkomodo/">Open Komodo</a>, an open-source project seeded with much of the core of <a href="http://www.activestate.com/Products/komodo_edit/">Komodo Edit</a> and <a href="http://www.activestate.com/Products/komodo_ide/">Komodo IDE</a> with the goals of produce a platform/framework for and (codename Komodo Snapdragon) an IDE for client-side open web development. </p>

<p>That's a mouthful. <a href="http://blogs.activestate.com/shanec/2007/09/holy-komodo.html">Shane</a> and <a href="http://ascher.ca/blog/2007/09/05/open-komodo-thoughts/">David</a> have done a good job giving some wider perspective on what the Open Komodo project could mean (if all goes well). David went so far as to invent new language to make his points.</p>

<p>Some quick thoughts from a coder's perspective:</p>

<ul>
<li><p>The source will be available in a <a href="http://www.selenic.com/mercurial/wiki/">Mercurial</a> repository in (quoting Shane paraphrasing Mike Shaver) "Two F**king Months!". Early November -- or earlier if we can.</p></li>
<li><p>Komodo is a Mozilla-based application with the added heavy use of <a href="http://developer.mozilla.org/en/docs/PyXPCOM">PyXPCOM</a> for much of the core logic. That means the app comes together like this: </p>

<ul>
<li>Get a slightly tweaked mozilla build (C++, JavaScript, XUL).</li>
<li>Get a slightly tweaked Python build (C).</li>
<li>Add a bunch of core logic (Python). For example, the guts of Komodo's Find/Replace system is written in Python -- using Python's unicode-aware regular expression engine.</li>
<li>Add Komodo chrome (XUL, JavaScript, CSS, DTDs).</li>
</ul>

<p>What this means is that to work on and add significant functionality to Komodo, all you tend to need to know is XUL, JavaScript and Python. From early on in Komodo's development we've felt that this is one of Komodo's aces in the hole: <strong>developing in the dynamic languages is so much faster</strong>. I remember David Ascher making the comment way back that if Subversion had been written in Python, it would have been ready years sooner. And now two of the primary DVCS, Mercurial and Bazaar, are written in Python.</p></li>
<li><p>Komodo uses the same extension mechanisms as Firefox. It is easy to build a .xpi to add functionality to Komodo. We really hope that a community of Komodo extension authors will develop.</p></li>
<li><p>Komodo builds and runs on Windows, Linux and Mac OS X. Given some work there is little reason the Open Komodo code base couldn't be made to run well on Solaris, BSD, etc.</p></li>
</ul>

<p>If any of this sounds interesting to you as an open-source tinkerer, then give <a href="http://www.activestate.com/Products/komodo_edit/">Komodo Edit</a> or <a href="http://www.activestate.com/store/evallicense.aspx?PliGuid=8E08763F-FC3D-456F-BE10-F0D725F660F8&">Komodo IDE a try</a>. The first app that will come out of the Open Komodo project (Komodo Snapdragon) will look and feel a lot like them.</p>

<p>In subsequent posts, and especially once the source code repository is up, I plan to blog here about Komodo's internals.</p>
