---
layout: post
title: Komodo 3.5.1 nits (with workarounds)
date: 2005-12-01T07:15:00.009-08:00
published: true
categories: [komodo, activestate]
---

<p>We released Komodo 3.5.1 yesterday. A few issues have come up since then that may be annoying for some Komodo users. Until we can get a new release out fixing these issues, here is what they are and how to work around them (if you happen to hit one):</p>

<ul><li>XSLT Autocomplete is busted on Windows. <a href="http://bugs.activestate.com/Komodo/show_bug.cgi?id=41898">Bug 41898</a>. <br /><br />The workaround is Find and edit &quot;koXMLStateMachineReader.py&quot; in your Komodo installation
(&lt;install-dir&gt;/lib/mozilla/python/komodo/). Change the &quot;print&quot;
statement on line 211 (i.e. in the handle__unknown() method) to a
&quot;pass&quot; statement. I.e.:<br /><pre>&nbsp; &nbsp; ...<br />&nbsp; &nbsp; def handle__unknown(self, node, *args):<br />&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; pass<br />&nbsp; &nbsp; ...</pre></li>

<li><span>Perl syntax checking might give syntax errors on &quot;use&quot; statements not being able to find a module in the same directory as a script that you are editing. I wrote <a href="http://aspn.activestate.com/ASPN/Mail/Message/komodo-discuss/2920833">a tale of 3 (or 4?) Dave's</a> describing the background, but the main issue is that Komodo by default syntax checks your Perl code with Perl taint mode even though you probably don't <em>run </em>your code with taint mode.<br /><br />The workaround, if you hit this, is simply to change the default Perl syntax checking mode to not use taint mode (i.e. &quot;-cw&quot; instead of &quot;-cwT&quot;). This will be the new default in future Komodo versions.<br /><br /></span></li>

<li><span>On Windows Tablet PCs (Do you think <a href="http://scobleizer.wordpress.com/">Scoble</a> scripts?), opening the find/replace dialog would not put keyboard focus into the find pattern textbox. <a href="http://bugs.activestate.com/Komodo/show_bug.cgi?id=42441">Bug 42441</a>.<br /><br />The workaround is to apply this patch to &quot;&lt;installdir&gt;/lib/mozilla/chrome/jaguar/content/find/find.js&quot;:
<pre>@@ -278,6 +278,7 @@<br />&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; getService(Components.interfaces.koIFindService);<br />&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;_Initialize();<br />&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;window.focus();<br />+&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; widgets.panel.pattern.focus(); // Bug 42441<br />&nbsp; &nbsp;&nbsp; } catch (ex) {<br />&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;log.exception(ex);<br />&nbsp; &nbsp;&nbsp; }</pre></span></li>

<li><span>Changing Windows file associations in the &quot;Windows Integration&quot; preferences panel would fail with &quot;[Errno 9] Bad file descriptor&quot;. <a href="http://bugs.activestate.com/Komodo/show_bug.cgi?id=42957">Bug 42957</a>.<br /><br />The workaround is to apply <a href="http://bugs.activestate.com/Komodo/showattachment.cgi?attach_id=3284">this patch</a> (attached to the bug report) to &quot;koInitService.py&quot; in your Komodo installation.<br /></span></li></ul>

<p>I'll try to post workarounds for any more issues that we find before we are able to put up a new release. Thanks to all of you that posted bug reports.</p>
