---
layout: post
title: ActivePython 2.4.3.12 is released (Windows-only bugfix)
date: 2006-04-12T07:51:00.009-07:00
published: true
categories: [python, activestate]
---

<p><a href="http://www.activestate.com/Products/ActivePython/">ActivePython 2.4.3.12</a> was just released to fix a problem with how PATHEXT is set on Windows. From the release notes:

</p>

<ul>
<li>[Windows] Fix a bug that results in &quot;.pyo&quot; and &quot;.pyc&quot; being placed on the
PATHEXT environment variable before &quot;.py&quot; for clean installs. <a href="http://bugs.activestate.com/ActivePython/show_bug.cgi?id=33311">Bug
33311</a>. This can cause surprises for command-line usage for Python
scripts when not specifying the &quot;.py&quot; extension. The new installer
will fix PATHEXT on machines that hit this bug.
</li>
</ul>

<p>

See <a href="http://groups.google.ca/group/comp.lang.python/browse_thread/thread/90e36791afbb90b8/c0705f28c2b3b2bf?lnk=st&amp;q=can't+pass+command-line+arguments&amp;rnum=1&amp;hl=en#c0705f28c2b3b2bf">
this python-list thread</a> for more details.


</p>

<p>The release notes are <a href="http://aspn.activestate.com/ASPN/docs/ActivePython/2.4/relnotes.html#release_history">here</a> and the announcements should be hitting the lists soon.</p>
