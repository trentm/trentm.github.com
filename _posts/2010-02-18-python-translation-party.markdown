---
layout: post
title: Python Translation Party
published: true
---


I've **updated [Python Translation
Party](http://pythontranslationparty.appspot.com/)** to recent versions of
[`lib2to3`](http://svn.python.org/projects/sandbox/trunk/2to3/lib2to3/) and
[`lib3to2`](http://bitbucket.org/amentajo/lib3to2/). I spoke with Joe Amenta at
the [PyCon 2010 poster
session](http://us.pycon.org/2010/conference/posters/accepted/) (he had a
poster on his `lib3to2` work) and he mentioned that the best thing I could do
with Python Translation Party for him was to update to the latest. :) Updating
to the latest is a *little* difficult because App Engine runs Python 2.5.2 and
`lib3to2` targets Python 2.7, so some small backporting was in order.

At the least, the new update results in fewer "booms" -- i.e. when there is
some sort of unexpected error in translating either way. The "boom" section of
the ["Crash other parties"
page](http://pythontranslationparty.appspot.com/crash/) before:

<p><img src="https://dl.dropbox.com/u/1301040/blog/2010/02/party_crash_before.png"/></p>

and after:

<p><img src="https://dl.dropbox.com/u/1301040/blog/2010/02/party_crash_after.png"/></p>

One boom remains. I'll have to dig in to see if this is a lib3to2 bug, lib2to3
bug, or party bug.

