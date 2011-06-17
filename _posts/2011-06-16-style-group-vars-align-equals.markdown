---
layout: post
title: "Coding Style: Why to not group variables and align equals"
published: true
date: 2011-06-16T21:43:47.419428
categories: [style]
---

Here is a diff from a `git log -p` stream I was reviewing:

    -var ZPOOL_PATH = '/sbin/zpool'
    -  , ZFS_PATH   = '/sbin/zfs'
    -  , PFEXEC_PATH   = '/bin/pfexec';
    +var ZPOOL_PATH  = '/sbin/zpool'
    +  , ZFS_PATH    = '/sbin/zfs';

If (a) this wasn't using the "group all vars in a single statement" cuteness:

    var ZPOOL_PATH = '/sbin/zpool'
    var ZFS_PATH   = '/sbin/zfs'
    var PFEXEC_PATH   = '/bin/pfexec';

and (b) wasn't using the anti-pattern (IMHO, of course) of aligning '=' in variable declaraction blocks:

    var ZPOOL_PATH = '/sbin/zpool'
    var ZFS_PATH = '/sbin/zfs'
    var PFEXEC_PATH = '/bin/pfexec';

then the diff hunk would have been:

    -var PFEXEC_PATH = '/bin/pfexec';

which is what it should have been.
