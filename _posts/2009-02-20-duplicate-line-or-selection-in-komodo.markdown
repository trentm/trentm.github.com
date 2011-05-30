---
layout: post
title: "&#8220;duplicate line or selection&#8221; in Komodo"
date: 2009-02-20T01:46:00.009-08:00
published: true
categories: [komodo, activestate]
---

<p>I saw <a href="http://www.botsko.net/blog/2009/02/duplicate-lineselection-in-komodo-5/">this blog entry</a> this morning:</p>

<blockquote>
<h3>Duplicate Line/Selection in Komodo 5</h3>

<p>Exploring the ability to create macros and bind them to key commands in Komodo IDE. I'm reposting the below macro that duplicates the lines or the current selection. Thus functionality was previously is Zend Studio 5, went missing from 6, and thanks to the macro, is available in Komodo. Enjoy!</p>

<p>...</p></blockquote>

<p>I thought I should mention the Komodo bug -- <a href="http://bugs.activestate.com/show_bug.cgi?id=78819">Extend functionality of the "duplicate line" function</a> -- on which <a href="http://blogs.activestate.com/ericp/">Eric</a> added a new core command to Komodo to do just this... with the added bonus that it also works for block/column selections. This was added just yesterday. Here is the <a href="http://svn.openkomodo.com/openkomodo/revision?rev=3018">checkin to Komodo Edit's repository</a>. The nightly builds of Komodo 5.1.0a2 from last night has this in it:</p>

<p>Komodo IDE: <a href="http://downloads.activestate.com/Komodo/nightly/komodoide/latest-trunk/">http://downloads.activestate.com/Komodo/nightly/komodoide/latest-trunk/</a></p>

<p>Komodo Edit: <a href="http://downloads.activestate.com/Komodo/nightly/komodoedit/latest-trunk/">http://downloads.activestate.com/Komodo/nightly/komodoedit/latest-trunk/</a></p>

<p>You can assign any key to this command in Komodo's "Editor | Key Bindings" preferences panel. The command name is "Editor: Duplicate Line or Selection".</p>
