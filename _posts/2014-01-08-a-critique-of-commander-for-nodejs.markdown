---
layout: post
title: A critique of commander for node.js
published: true
date: 2014-01-08T21:21:03.599589
categories: [nodejs]
---

Because [someone (@mgan)
asked](https://twitter.com/mgan/status/420634474770997249) here is my critique
of [commander.js](https://github.com/visionmedia/commander.js), a popular option
parsing library for node.js, and comparison to
[node-dashdash](https://github.com/trentm/node-dashdash), an option parsing
library for node.js that I wrote. This isn't meant as a "you suck, I rock" post.
I wrote dashdash to fill my needs because other libs didn't. I'd be happy if
dashdash worked well for you, but I'm not selling it. :)


## Pros

- Commander.js involves less typing and more compact, which helps for quick
  readability.

- [**Update 2014-03-28:** As of dashdash@1.5.0, custom option types are supported by
  dashdash.]

  Commander.js supports [custom parsing of option
  arguments](https://github.com/visionmedia/commander.js#coercion). That's good
  and something that dashdash doesn't have. Dashdash has a [number of
  canned types](https://github.com/trentm/node-dashdash#option-specs) that
  so far have suited my needs. Adding custom option types would be worthwhile.

- `program.command(...)` support in commander.js is neat. I use
  [node-cmdln](https://github.com/trentm/node-cmdln) for that, but the handling
  in commander.js is certainly more lightweight.

- Commander.js supports an option having an *optional argument*, e.g.:

        node mycmd.js -f ARG
        node mycmd.js -f        # no argument to option '-f'

  Dashdash doesn't support this, so if you need it, then boom.

- Having many
  [examples](https://github.com/visionmedia/commander.js/tree/master/examples)
  is good.


## Cons

- How to get rid of `-h|--help` and `-V|--version`? I definitely advocate that
  all CLI tools have a those options (sometimes just "--version" and not the
  "-V" shortcut), but I don't think an option lib should *require* it.

- That the lib uses `process.exit()` (handling --help, on unknown options) makes
  it difficult to integrate option processing in tools that aren't a small
  command, e.g. a shell.

- Commander.js doesn't allow
  [`interspersed=false`](https://github.com/trentm/node-dashdash#parser-config).
  This is useful in [node-cmdln](https://github.com/trentm/node-cmdln), but I'll
  grant most may not need this.

- No support for multiple uses of the same arg to build up an array (as supported
  by dashdash's `arrayOf*` option types). Commander.js's `list` option type
  is another take on this:

        node mycmd.js --list a,b,c   # program.list === ['a', 'b', 'c']

- Both commander.js and dashdash have automated formatting of help output.
  However, dashdash intentionally only generates the option block and *not*
  the usage string and "options:" section prefix. That's a balance in favour
  of being usable for other help output styles vs. requiring the user to
  write a little bit more themselves.

- If order of options *does* matter then dashdash's `<parsed>._order` can be
  helpful. Again a limited use case.

- Mixing parser and the parsed results. Obviously this is minor, but I
  like the ability to be able to log the parsed options and just have *data*
  logged. Also the sharing of namespace means that you can't have an option
  named `Option`, `Command` or `args`. In fairness in dashdash you can't
  have an option named `_args` or `_order`.

- No equivalent to
  [`allowUnknown=false`](https://github.com/trentm/node-dashdash#parser-config).
  There are [PRs for this](https://github.com/visionmedia/commander.js/search?q=unknown&ref=cmdform&type=Issues)
  on commander.js

- No [environment variable integration](https://github.com/trentm/node-dashdash#environment-variable-integration).

- Dashdash's help output is more configurable. Minor.


There are lots of PRs and tickets open on commander.js, including [one for an
issue that I noticed](https://github.com/visionmedia/commander.js/pull/121) when
playing a bit. This can be good (lots of interested, issues you might
have probably have code available). Far be it for me to complain about keeping
up with issues and PRs on [ones](https://github.com/trentm/json/issues?state=open)
[own](https://github.com/trentm/node-bunyan/issues?state=open)
[projects](https://github.com/trentm/python-markdown2/issues?state=open).

Overall, I think commander.js looks fine for option parsing. Most of my "Cons"
are either minor or a result of my just having had particular use cases that
perhaps commander.js's authors have not. I haven't used commander.js other than
briefly looking at it today, so I could very likely have made mistakes in
grokking commander.js. Feedback is welcome.
