---
layout: post
title: I want a Dave's Quick Search Deskbar equivalent for my Mac
date: 2005-03-10T15:35:00.009-08:00
published: true
categories: [General, ui, macosx]
---

<p>The greatest thing on my Windows dev box at work is <a href="http://www.dqsd.net/">Dave's Quick Search Deskbar</a>. This is probably the number one reason why I feel I am more productive on Windows than on my OS X box at home. I want something like this for my Mac. <a href="http://www.ambrosiasw.com/utilities/iseek/">iSeek</a> is close, but not quite there. </p>

<p>The brilliance of DQSD is (1) the use of simple short keyword conventions to indicate what type of search you want and (2) the level of control (effectively JavaScript) that you have in defining new searches.</p>

<ol><li>
Using short keyword conventions to denote the type of search is <strong>so much faster</strong> than fumbling through a menu list of search types such as you see with iSeek, with the search textboxes in Safari and Firefox, etc.
<ul>
<li>By default, of course, you get a Google search of your term.</li>
<li>Add an exclamation point and you get a Google "I'm feeling lucky" search. The ability to open, say, <a href="http://www.python.org/">python.org</a> in your browser by typing '<code>&lt;Windows+S&gt;python!&lt;Enter&gt;</code>' is invaluable. (<code>&lt;Windows+S&gt;</code> is the hotkey to jump to the DQSD textbox.)</li>
<li>Type '<code>amaz Unicode</code>' to look for Unicode books on Amazon</li>
<li>'<code>wiki foo</code>' to lookup something in Wikipedia</li>
</ul>
</li>

<li>An an indicator of the level of control that I want for custom searches I'll describe the custom "<code>ko</code>" search that I've defined to work with the bug database for <a href="http://www.activestate.com/Products/Komodo/">Komodo</a>, an product that I work on.
<ul>
<li>'<code>ko</code>' just opens the <a href="http://bugs.activestate.com/Komodo/query.cgi">Komodo bug database main page</a></li>
<li>'<code>ko perl autocomplete</code>' searches for <a href="http://bugs.activestate.com/Komodo/buglist.cgi?querytype=simple&type%3Ashort_desc%3Along_desc%3Abug_file_loc%3Astatus_whiteboard%3Akeywords=substring&OR%3Ashort_desc%3Along_desc%3Abug_file_loc%3Astatus_whiteboard%3Akeywords=perl+autocomplete&submit=Search&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED">bugs in Komodo Perl AutoComplete</a>
</li>
<li>'<code>ko 35787</code>' opens <a href="http://bugs.activestate.com/Komodo/show_bug.cgi?id=35787">Komodo bug 35787</a></li>
<li>'<code>ko +</code>' opens the <a href="http://bugs.activestate.com/Komodo/enter_bug.cgi">form for adding a new bug</a></li>
</ul>
</li>
</ol>

<p>Does anybody know of a Mac OS X app that can do this?</p>
