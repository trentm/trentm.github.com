---
layout: post
title: On a bit of confusion
published: true
---

On a bit of confusion in [ActivePython 2.7 released - and what 2.7 means for Python's future](http://www.activestate.com/blog/2010/07/activepython-27-released), in particular the following paragraph. Before:

> While the Python community has declared a moratorium on major 2.x releases in an effort to facilitate other Python implementations to catch up and, thus, accelerate the adoption of Python 3.x, ActiveState will continue supporting 2.7.x and adding new modules and updating revisions to existing ones as they become available.

After:

> While [you may have read](http://www.python.org/dev/peps/pep-3003/), the Python community has declared a temporary moratorium (suspension) on the Python language syntax in an effort to facilitate other Python implementations to catch up to Python 3.x --- the moratorium does not that mean that python core development has stopped or even slowed down.  
>
> On the contrary, new modules continue to be added, bugs fixed, and performance tweeked --- and, as always, ActiveState will continue supporting 2.7.x with builds, extra modules and PyPM as they become available.

[Jesse Noller](http://twitter.com/jessenoller) accurately noted that the former paragraph was confusing. In particular, a possible interpretation that the Python community isn't going to be supporting Python 2.7 -- which is just [not true](http://docs.python.org/dev/whatsnew/2.7.html#the-future-for-python-2-x). Python 2.7 will be supported for longer than the typical two years that a Python 2.x release is supported.

It is easy to convolve the mostly unrelated *Python language moratorium* and the plan that *Python 2.7 is the last 2.x*. The two are somewhat related in that ultimately the hope is they both lead to smoother adoption of Python 3. The issue (from ActiveState's Product Manager's point of view) is that an enterprise customer can get swayed away from considering Python when reading stuff like the following from [Python moratorium and the future of 2.x](http://lwn.net/Articles/361266/):

> On November 9, Python BDFL ("Benevolent Dictator For Life") Guido van Rossum froze the Python language's syntax and grammar in their current form for at least the upcoming Python 2.7 and 3.2 releases, and possibly for longer still. This move is intended to slow things down, giving the larger Python community a chance to catch up with the latest Python 3.x releases.

It is *very* easy for the less-technical person to interpret "moratorium on Python language syntax" as a stop on *all core Python development*. This differentiation was the kernel of a heated debate I just had with our Product Manager recently.

The intention of the paragraph in the ActiveState blog post is basically to state that the language moratorium isn't something that should dissuade usage businesses from considering Python.

That said: Mea culpa. I had the chance to catch this the first time and didn't.


