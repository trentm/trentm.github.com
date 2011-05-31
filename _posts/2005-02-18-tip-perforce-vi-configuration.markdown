---
layout: post
title: "tip: perforce + vi configuration"
date: 2005-02-18T06:10:00.009-08:00
published: true
categories: [perforce]
---

<p>If you use <a href="http://www.perforce.com">Perforce</a> (i.e. the 'p4' command line app) and you use <a href="http://www.vim.org">Vim</a> as your <a href="http://www.perforce.com/perforce/doc.042/manuals/cmdref/env.P4EDITOR.html">P4EDITOR</a> then try this (on Windows):</p>

<pre><code>p4 set "P4EDITOR=C:&#92;PROGRA~1&#92;Vim&#92;vim63&#92;gvim.exe +0 +/&lt;enter&#92;|^&gt;&gt;&gt;&gt;&#92;|^====&#92;|^&lt;&lt;&lt;&lt;&#92;|^&#92;t +nohlsearch"</code></pre>

<p>(presuming that you have installed Vim 6.3 to the default location) and/or this (for Bash shell users on Linux/Un*x):</p>

<pre><code>export P4EDITOR='vim +0 "+/&lt;enter&#92;|^&gt;&gt;&gt;&gt;&#92;|^====&#92;|^&lt;&lt;&lt;&lt;&#92;|^&#92;t" +nohlsearch'</code></pre>

<p>This has Vim jump to the <code>&lt;enter description here&gt;</code> position in a <code>p4 submit</code> form or, if this isn't a submission form (perhaps you are editing a user or client spec) then to the first multi-line form field.</p>

<p><span style="text-decoration:line-through">Unfortunately this still leaves the search highlighting in place. Anybody know how to dismiss that in Vim without hackily just searching for something for which there won't be a hit? Doing the latter results in a warning message.</span> [Update Tue, Feb 22: found out how to clear the current search highlighting.]</p>

<p>[Update Thu, Dec 8: added search for conflict markers during a <code>p4 resolve</code> session.]</p>
