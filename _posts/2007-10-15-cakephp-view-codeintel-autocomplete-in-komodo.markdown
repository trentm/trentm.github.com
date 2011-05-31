---
layout: post
title: CakePHP view codeintel (autocomplete) in komodo
date: 2007-10-15T01:48:00.009-07:00
published: true
categories: [komodo, codeintel]
---

<p>It is great to see more and more posts these days about adding functionality to Komodo. Only a few month back, daily blog posts about Komodo tended to be of the "Tried Komodo. Like it. Using it for blah.". Now blog posts about Komodo are often "Tried Komodo. Like it. Using it for blah. Used the macro or extension system to add blah."</p>

<p>For example, <a href="http://traviscline.com/blog/2007/10/12/komodo-cakephp-view-macros/">this post by Travis Cline</a> shows a brilliant little hack to get Komodo's PHP codeintel (autocomplete and calltips) to work with the implicit environment for CakePHP views ('.ctp' files). It is a great example of the kinds of things you can do with Komodo macros.</p>

<p>Note to self: Look into providing this same functionality via a special CakeViewEnvironment class that does a similar thing and that is attached to any buffer for a CakePHP view. Every "buffer" in Komodo's codeintel system (there is one buffer for each open file and each file used for autocomplete info) has an "env" attribute which is a instance of the "Environment" class. This class defines special runtime environment information -- typically just Komodo preferences and environment variables. However, subclasses can provide other info. An example is the "KoJavaScriptMacroEnvironment" that is attached to a buffer for editing a Komodo JavaScript macro in the editor. This environment class hooks up the Komodo JS API catalog so that you get autocomplete for Komodo JS macro API.</p>

<p>I have to look into (1) documenting this (when we have the <a href="http://wiki.openkomodo.com/">Open Komodo wiki</a> setup, that'll probably be the right place) and (2) ensuring that extensions can provide these environment classes and do interesting things with them. Currently it might require some custom work on the codeintel engine to hook this up. But codeintel Environment classes are the plan.</p>
