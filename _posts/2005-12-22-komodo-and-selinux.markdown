---
layout: post
title: Komodo and SELinux
date: 2005-12-22T01:31:00.009-08:00
published: true
categories: [komodo, activestate]
---

<p>Recently we had been noticing some reports of Komodo startup failing on some modern Linux boxes. See <a href="http://bugs.activestate.com/Komodo/show_bug.cgi?id=43260">bug 43260</a>. It was tracked down to SELinux on the particular machine disallowing text-segment relocation in a specific shared object in Komodo.</p>

<p>The problem became more acute with the recent releases because <a href="http://fedora.redhat.com/docs/selinux-faq/">Fedora Core 4 now comes with SELinux</a> installed, enabled and enforcing (in certain areas of the file system) by default.</p>

<p>(Gory details: Basically there is a micro chance for a security hole during text-segment relocation when loading a shared object that was not compiled with position-independent code -- i.e. without &quot;-fPIC&quot; with gcc. I need to find the reference -- deep in a PDF a co-worker found -- that described those details again.)</p>

<p>So either you need to build all your .so's -fPIC or you need to set SELinux attributes appropriately (a.k.a. set the &quot;security context&quot;) on certain files post-install. Komodo 3.5.x did a bit of both. First we made the changes that we could to get all .so's building -fPIC. However, we still have one that could not be, so we need to set its security context on install. One does this &quot;chcon&quot; (change context).</p>

<pre>chcon -t <strong>security-context-name</strong> path/to/file.so</pre>

<p>Easy peasy. Except one thing. What is that &quot;security-context-name&quot;? On FC4 it is &quot;texrel_shlib_t&quot;. (This is what Komodo's Linux installer attempts to do on that one file, &quot;libnpscimoz.so&quot;, if SELinux is detected.) On CentOS (a clone of RHEL) it is apparently something else because:</p>

<pre>chcon: failed to change context of /home/msoulier/komodo/lib/mozilla/plugins/libnpscimoz.so to user_u:object_r:texrel_shlib_t: Invalid argument</pre>

<p>On other Linux distros: who knows? I am not currently aware of a way to programmatically figure out what the built-in and user-defined set of valid security context names is for a given SELinux install. Any pointers anyone could provide would be appreciated.</p>
