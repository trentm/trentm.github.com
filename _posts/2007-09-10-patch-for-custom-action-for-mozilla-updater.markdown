---
layout: post
title: "patch for &#8220;custom action&#8221; for mozilla updater"
date: 2007-09-10T09:07:00.009-07:00
published: true
categories: [komodo, mozilla]
---

<p><a href="http://dl.getdropbox.com/u/1301040/blog/2007/09/moz_updater_customaction.patch">Here is a patch</a> (against a slightly out of date updater.cpp on the Mozilla 1.8 branch) that would add support for a:</p>

<pre>customaction "relative-path-to-executable"</pre>

<p>action in the "update.manifest" for a partial or full update (<code>.mar</code> file) for the <a href="http://wiki.mozilla.org/AUS">Mozilla update system</a>.</p>

<p>I'm just chucking this up here quickly for lack of a better place to put it right now. Komodo uses the Mozilla update system and will possibly need this patch at some point. </p>

<p>Limitations: </p>

<ul>
<li>It ignores the return value of the spawned executable.</li>
<li>It doesn't support arguments to the executable.</li>
</ul>
