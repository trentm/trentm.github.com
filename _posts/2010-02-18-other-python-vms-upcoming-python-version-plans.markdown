---
layout: post
title: other Python VM's upcoming Python version plans
published: true
---


Some quick notes about the coming plans by the "other" Python implementations
from today's Python Language Summit at PyCon 2010:

- IronPython: 
    - plan is to do Python 2.7 first, focus for this year
    - python 3.2 for the end of next year hopefully
    - other work on IDE stuff
- Pynie (i.e. Parrot) -- Allison Randall:
    - about 4 major features away from pure Python syntax (did dicts last
      night)
    - targetting py3k repo and test suite: should be on track for python 3.2
- Jython:
    - plan to target 2.6 (b/c 2to3 depends on 2.6)
    - temporarily skip 2.7 and target 3.x (probably 3.2)
    - then if 3.x adoption isn't fully there, then go back and add Python 2.7
    - will require JDK 2.7 for Python 3 support (b/c of new support for
      dynamic languages)
- PyPy (Holger):
    - plan is Benjamin will port to Python 2.7 in the summer
    - only have slight deviations from CPython: idea is to merge back with
      CPython so don't have deviations. Typcically 1 or 2 line changes in ~25
      modules.


