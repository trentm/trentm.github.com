---
layout: post
title: who knew path joining differed so between Python, Ruby, Node, Perl
categories: [path, languages, python, ruby, nodejs, perl]
---

In Python I do a lot of path manipulations for build systems, various
command-line utilities and Komodo support modules. Typically this is with
Python's `os.path` module. One thing I've come to expect of path joining,
`os.path.join`, is this (apparently rare) detail:

    If any component is an absolute path, all previous path components
    will be discarded.

I say "apparently rare" because, in Python:

    $ python
    >>> import os.path
    >>> os.path.join("/Users/trentm", "/var/log")
    '/var/log'

in Ruby:

    $ irb
    >> File.join("/Users/trentm", "/var/log")
    => "/Users/trentm/var/log"

in Node.js:

    $ node
    node> var path = require('path')
    node> path.join("/Users/trentm", "/var/log")
    '/Users/trentm/var/log'

in Perl:

    $ cat pathjoin.pl 
    use File::Spec;
    print File::Spec->join('/Users/trentm', '/var/log'), "\n";
    $ perl pathjoin.pl 
    /Users/trentm//var/log

Conclusions? Certainly none of these libraries is going to change their
behaviour here, with the possible exception of Node which is young and
changing very quickly. I'd say the double '/' in Perl's `File::Spec` is
poor -- though it doesn't give in invalid path. You could certainly argue
that Ruby's and Node's interpretation is less subtle (often a good thing).
I **like** Python's interpretation: `os.path.join` is kind of like
running `cd` for each given path in sequence to get the resultant
directory. It means I don't need a guard against an absolute path input
datum being joined to a current working directory scope.

I'd be curious to know what is typical in other languages, if there are
any takers reading this post. If blog commenting isn't your thing, you
can tweet "@trentmick".
