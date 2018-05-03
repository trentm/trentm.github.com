---
layout: post
title: History feature in Komodo 5.1.0 alpha 1
date: 2009-02-04T08:08:00.009-08:00
published: true
categories: [komodo, activestate, mozilla]
---

<p>We released Komodo 5.1.0 alpha 1 today! Get it here:</p>

<div style="margin-left: 30px;"><a href="http://downloads.activestate.com/Komodo/releases/5.1.0a1/">http://downloads.activestate.com/Komodo/releases/5.1.0a1/</a></div>

<p>Please try it out and give us your feedback:</p>

<table class="attrlist">
<tr><th>email</th><td><a href="http://listserv.activestate.com/mailman/listinfo/komodo-beta">http://listserv.activestate.com/mailman/listinfo/komodo-beta</a></td></tr>
<tr><th>bugs</th><td><a href="http://bugs.activestate.com/enter_bug.cgi?product=Komodo">http://bugs.activestate.com/enter_bug.cgi?product=Komodo</a></td></tr>
<tr><th>forums</th><td><a href="http://community.activestate.com/products/Komodo">http://community.activestate.com/products/Komodo</a></td></tr>
</table>

<p>This is the first release of Komodo 5.1 on the way to a planned final release
around <strike>mid-May</strike> <em>[<strong>Update:</strong> mid-March. Subconsciously I keep hoping for more time. :)]</em>. (I'll write about our Komodo 5.1 plans in a separate post).
Here I want to talk about Komodo's new "History" feature.</p>

<h2>History overview</h2>

<p><a href="https://www.flickr.com/photos/trento/3253669957/" title="screenshot of Komodo 5.1's history feature"><img src="//farm4.static.flickr.com/3009/3253669957_903874fa5c_o.jpg" width="570" height="448" alt="screenshot of Komodo 5.1's history feature" /></a></p>

<p>Komodo's History feature is like your browser's history, but for the editor.
Back and Forward buttons in the toolbar. Same default keybindings as in
Firefox <sup class="footnote-ref" id="fnref-1"><a href="#fn-1">1</a></sup>. Simple.</p>

<p>Komodo's history is a bit different than a browser's. In a browser, you have
a separate history session for each tab. This doesn't make as much sense
for an editor. Komodo's history is per-window <sup class="footnote-ref" id="fnref-2"><a href="#fn-2">2</a></sup>. That means that the Back
button will move you back to the last place you were, be that in the current
file or in another file in the same window. This means that jumping back:</p>

<ul>
<li>after a <a href="http://docs.activestate.com/komodo/5.0/editor.html#go_to_def">Go To Definition</a>, or</li>
<li>after opening a new file, or</li>
<li>after jumping to a find result</li>
</ul>

<p>is as easy as clicking "Back".</p>

<p>More than any new feature in Komodo, the first time we hooked the feature up
it felt immediately useful. Of course, this is just an alpha release so there
is lots of polishing to do. Read on for some of the other things we hope to do
with this.</p>

<h2>Future work</h2>

<p>Some other things Komodo will be able to support with this:</p>

<ul>
<li><strong>Opening recent files quickly.</strong> Chances are good that a file you want to
open in your editor is a file you've edited before (and recently). The
history database now provides Komodo with the data it needs to support that.</li>
<li><strong>Find in recent files.</strong> Often I'll want to look at some snippet of code
that I remember writing in the last few days, but can't remember what
file (or even what project) that was in.</li>
<li><p><strong>Support <code>''</code> command in Vi-mode</strong>. From the Vim help:</p>

<pre><code>''  ``                  Move to the position before latest jump.
</code></pre></li>
<li><p>Hooking <code>Back</code> and <code>Forward</code> into the MS Intellimouse's (and other mice, I
suspect) side buttons -- as is the default in Firefox.</p></li>
</ul>

<h2>Backend code</h2>

<p>For those interested, most of the backend of the history system is <a href="http://svn.openkomodo.com/openkomodo/view/openkomodo/trunk/src/history/editorhistory.py">here in
"editorhistory.py"</a>
in the Open Komodo subversion repository.</p>

<p>For JavaScript code (most interesting to Komodo extension developers) there is
a new <a href="http://grok.openkomodo.com/source/xref/openkomodo/trunk/src/chrome/komodo/content/library/history.js"><code>ko.history</code>
API</a>
with the most relevant methods being:</p>

<ul>
<li><code>ko.history.note_curr_loc(view)</code>: Tell the history system to note the
current editor location before jumping somewhere.</li>
<li><code>ko.history.history_back(n)</code>: Go back <code>n</code> locations.</li>
<li><code>ko.history.history_forward(n)</code>: Go forward <code>n</code> locations.</li>
</ul>

<p>Komodo's history database shares some ideas with <a href="https://developer.mozilla.org/en/The_Places_database">Firefox 3's Places
database</a>. In particular
the idea of splitting visited locations (URLs in Firefox, editor locations in
Komodo) and <em>visits</em> into separate database tables was helpful. They are, of
course, both SQLite3 databases.</p>

<div class="footnotes">
<hr />
<ol>
<li id="fn-1">
<p>The keybindings aren't yet there for Mac OS X in alpha 1. They will be
there for alpha 2.&nbsp;<a href="#fnref-1" class="footnoteBackLink" title="Jump back to footnote 1 in the text.">&#8617;</a></p>
</li>

<li id="fn-2">
<p>Currently it is shared by multiple Komodo windows, but will be changed to
be per window.&nbsp;<a href="#fnref-2" class="footnoteBackLink" title="Jump back to footnote 2 in the text.">&#8617;</a></p>
</li>
</ol>
</div>
