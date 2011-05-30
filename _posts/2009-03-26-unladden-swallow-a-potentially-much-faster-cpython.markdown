---
layout: post
title: "unladden swallow: a (potentially *much*) faster CPython"
published: true
categories: [python, programming, activestate]
---

<p>Discussed a bit at the <a href="http://us.pycon.org/2009/about/summits/language/">Python Language Summit</a> at <a href="http://us.python.org/">PyCon</a> this morning: <a href="http://code.google.com/p/unladen-swallow/"><strong>unladen-swallow</strong></a> is a Google project to do a lot of performance work on CPython's VM. </p>

<ul>
<li>Currently have about 30% speed up.</li>
<li>Currently for Python 2 (2.4, I think).</li>
<li>Currently focused on Linux and Python 3, but committed to get patches back to the core (which implies Python 3 support). "This is a branch, not a fork."</li>
<li>Currently in <em>use</em> on Youtube (where most of the frontend is Python).</li>
</ul>

<p>They are shooting for a <strong>5x</strong> speedup.  From the <a href="http://code.google.com/p/unladen-swallow/wiki/ProjectPlan">ProjectPlan</a>:</p>

<blockquote>Our long-term proposal is to replace CPython's custom virtual machine with a JIT built on top of LLVM, while leaving the rest of the Python runtime relatively intact. We have observed that Python applications spend a large portion of their time in the main eval loop. In particular, even relatively minor changes to VM components such as opcode dispatch have a significant effect on Python application performance. We believe that compiling Python to machine code via LLVM's JIT engine will deliver large performance benefits.</blockquote>

<p>Jesse has a <a href="http://jessenoller.com/2009/03/26/pycon-unladen-swallow/">good write-up</a>.</p>
