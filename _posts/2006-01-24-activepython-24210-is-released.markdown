---
layout: post
title: ActivePython 2.4.2.10 is released
date: 2006-01-24T06:52:00.009-08:00
published: true
categories: [python, activestate]
---

<div style="float: right; margin-left: 10px; margin-bottom: 10px;"> <a title="photo sharing" href="http://www.flickr.com/photos/trento/66727800/"><img src="http://static.flickr.com/28/66727800_9692d76006_m.jpg" style="border: 2px solid rgb(0, 0, 0);" /></a> <br /> <span style="font-size: 0.9em; margin-top: 0px;">&nbsp; <a href="http://www.flickr.com/photos/trento/66727800/">python skeleton</a>&nbsp; <br />&nbsp; Originally uploaded by <a href="http://www.flickr.com/people/trento/">trento</a>. </span></div>

<p><a href="http://www.activestate.com/Products/ActivePython/">ActivePython 2.4.2.10</a> is out!</p>

<p>Highlights include:
</p>

<ul>
<li>Early support for Mac OS X for Intel platform (macosx-x86).</li>
<li>Upgrade to PyWin32 build 207 on Windows/x86</li>
<li>Upgrade Tkinter to Tcl/Tk 8.4.12</li>
<li>Support for Windows/x64 (win64-x64). Note that PyWin32 has not been ported to 64-bit Windows so this build does not include PyWin32.</li>
<li>Support for Linux/x86_64 (linux-x86_64)</li>
<li>Fixed a problem on Mac OS X/PowerPC that unintentionally created a dependency on <a href="fink.sourceforge.com">Fink</a> for the &quot;bz2&quot; and &quot;curses&quot; extensions. (Thanks, Bob!)</li>
<li>The Windows &quot;debug libraries&quot; package now allows installation into non-ActivePython Python installations of the same version. This <a href="http://mail.python.org/pipermail/python-dev/2005-December/058448.html">was requested</a> by Dave Abrahams for the Boost folks.</li>
<li>Changed Intel 32-bit architecture platform name from &quot;ix86&quot; to &quot;x86&quot;, changing package names for some ActivePython builds.</li>
</ul>

<p>See <a href="http://mail.python.org/pipermail/python-list/2006-January/322323.html">the announcements</a> for full details.</p>
