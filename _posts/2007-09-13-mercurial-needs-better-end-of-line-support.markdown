---
layout: post
title: mercurial needs better end-of-line support
date: 2007-09-13T09:18:00.009-07:00
published: true
categories: [mercurial, komodo, mozilla]
---

<p>One real world issue with source control systems is the handling of end-of-line characters in text files. Currently Mercurial pretty much punts. The <a href="http://hgbook.red-bean.com/hgbookch2.html#x6-290002.2">hg book says</a>:</p>

<blockquote>
Note: The Windows version of Mercurial does not automatically convert line endings between Windows and Unix styles. If you want to share work with Unix users, you must do a little additional configuration work. XXX Flesh this out.
</blockquote>

<p>The <a href="http://linux.die.net/man/5/hgrc">hgrc man page suggests</a>:</p>

<blockquote>
    NOTE: the tempfile mechanism is recommended for Windows systems,
    where the standard shell I/O redirection operators often have
    strange effects.  In particular, if you are doing line ending
    conversion on Windows using the popular dos2unix and unix2dos
    programs, you *must* use the tempfile mechanism, as using pipes will
    corrupt the contents of your files.


    Tempfile example:

<pre>
    [encode]
    # convert files to unix line ending conventions on checkin
    **.txt = tempfile: dos2unix -n INFILE OUTFILE


    [decode]
    # convert files to windows line ending conventions when writing
    # them to the working dir
    **.txt = tempfile: unix2dos -n INFILE OUTFILE
</pre>
</blockquote>

<p>However (1) unix2dos and dos2unix are generally not available on Windows machines and (2) if dos2unix <em>isn't</em> available the "encoding" here will <strong>silently wipe out your file</strong> to empty content on checkin.</p>

<p>How is Mozilla handling this in their hg repository? Is it mandated that new files added on Windows use Unix line endings or is some kind of conversion for Windows attempted?</p>
