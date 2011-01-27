---
layout: post
title: django-markdown-deux Django app
published: true
---

- Project page: http://github.com/trentm/django-markdown-deux
- on PyPI: http://pypi.python.org/pypi/django-markdown-deux/

`django-markdown-deux` is a small Django app that provides template tags for using
[Markdown](http://daringfireball.net/projects/markdown/) using the
[python-markdown2](http://code.google.com/p/python-markdown2/) library. MIT license.

## What's with the &#8220;deux&#8221; in the name?

The obvious name for this project in `django-markdown2`. However, there
[already is one!](http://github.com/svetlyak40wt/django-markdown2) and name
confusion doesn't help anybody. Plus, I took French immersion in school for 12
years: might as well put it to use.

## Quick Usage

### `markdown` template filter

    {{'{% load markdown_deux_tags %'}}}
    ...
    {{'{{ myvar|markdown:"STYLE" '}}}}     {# convert `myvar` to HTML using the "STYLE" style #}
    {{'{{ myvar|markdown '}}}}             {# same as `{{'{{ myvar|markdown:"default" '}}}}` #}


### `markdown` template block tag

    {{'{% load markdown_deux_tags %'}}}
    ...
    {{'{% markdown STYLE %'}}}        {# can omit "STYLE" to use the "default" style #}
    This is some **cool**
    [Markdown](http://daringfireball.net/projects/markdown/)
    text here.
    {{'{% endmarkdown %'}}}

See more usage info, available settings, installation notes, etc. at the github
project page. (I mention on Moz planet because Benjamin is, or was, using
python-markdown2 and I've heard Mozilla is using more Django these days.)


