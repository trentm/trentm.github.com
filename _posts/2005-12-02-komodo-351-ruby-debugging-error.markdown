---
layout: post
title: "Komodo 3.5.1: ruby debugging error"
date: 2005-12-02T03:53:00.009-08:00
published: true
categories: [komodo, activestate]
---

<p><a href="http://bugs.activestate.com/show_bug.cgi?id=43011">Bug 43011</a>. Most users shouldn't hit this, but if you get an error something like this while debugging Ruby in Komodo:

</p>

<pre>c:/ruby/lib/ruby/site_ruby/1.8/rubygems/custom_require.rb:18:in `require__': No such file to load -- no such mod (LoadError)<br />&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; from c:/ruby/lib/ruby/site_ruby/1.8/rubygems/custom_require.rb:18:in `re quire'<br />&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; from -:1 </pre>

<p>then (until Komodo 3.5.2 comes out) you may need to applied the workaround described in that bug.</p>

<p>Komodo's Ruby debugger includes a binary Ruby extension for speeding up some parts of the debugging process. (This was very important for making Rails debugging, for example, performant.) Komodo *also* includes a pure Ruby fallback implementation when the binary extension doesn't work -- for example if a new version of Ruby comes out or for platform compat issues, at least debugging should still work.</p>

<p>The problem was that some of those fallback files got installed to the wrong dir. Oops. That will be fixed in subsequent builds.</p>
