---
layout: post
title: an intro to Komodo extensions
date: 2007-09-06T07:33:00.009-07:00
published: true
categories: [komodo, mozilla]
---

<p>Komodo uses the Mozilla extension mechanism -- same <code>.xpi</code> files as Firefox to install an extension, <a href="http://developer.mozilla.org/en/docs/Bundles">same kind of bundle content in an extension</a>. However, Komodo adds a number of "hooks" that can be used to customize Komodo with an extension (see the end of this post).</p>

<p>In Komodo 4.2 (currently in beta) we've been working at improving the extension story. Part of my work there has been to improve the tools for building them. To that end Komodo 4.2 now includes a sort of "SDK" with a few tools:</p>

<dl>
<dt>koext</dt>
<dd>A tool for building and generating stubs for Komodo extensions. A recently added a (very brief) <a href="http://community.activestate.com/forum/introduction-building-komodo-extension">intro to using koext</a> to Komodo's extension forum.</dd>
<dt>luddite</dt>
<dd>A tool for working with Komodo's UDL (User-Defined Languages) system. The UDL system (new in Komodo 4.0) provides a way to define lexers for new languages. Lexers are used mainly for syntax coloring, but can also be used by Komodo Code Intelligence system for provide autocomplete and calltips. Eric wrote up <a href="http://blogs.activestate.com/ericp/2007/01/kid_adding_a_ne.html">a long intro to UDL</a> a while back. UDL currently isn't for the faint of heart, but it provides an execellent system for robust lexing of code languages -- in particular it supports *multi-language* code (e.g. JavaScript in HTML, Ruby in RHTML, CSS in Django HTML).</dd>
<dt>codeintel</dt>
<dd>A tool to help writing a language support for Komodo's Code Intelligence system. I'll write more on this later.</dd>
</dl>

<p>These tools are all works in progress but they are used internally as part of normal Komodo development, so should be usable for Komodo extension authors.</p>

<p>Komodo's <code>koext</code> tool briefly describes all the current Komodo extension "hooks":</p>

<pre>
$ koext help hooks

  Many parts of Komodo's functionality can be extended with a
  Komodo extension. We call those "hooks" here. The following is
  a list of all extension hooks that Komodo currently supports.

  The "source tree files" sections below are conventions for
  placement of sources files. If you use these conventions, then
  `koext build' will automatically be able to build your extension
  properly.

  chrome
      Chrome is the collective term for XUL (content), JavaScript
      (content), CSS (skin), images (skin) and localized files
      (locale, typically DTDs) that can be used to extend the
      Komodo UI. This works in Komodo extensions in exactly the
      same way as any other Mozilla-base application (such as
      Firefox). See `koext help chrome' for some tips.

      source tree files:
          chrome.manifest
          content/            # XUL overlays, dialogs and JavaScript
          skin/               # CSS
          locale/             # localized files (typically DTDs)

  XPCOM components
      XPCOM components are placed here. These can be written in
      Python or JavaScript. (C++-based components are possible
      as well, but currently the Komodo SDK does not support
      building them.)

      source files:
          components/
              *.idl           # interface definitions
              *.py            # PyXPCOM components
              *.js            # JavaScript XPCOM components

  templates
      A file hierarchy under here maps into Komodo's "New File"
      dialog. For example, "templates/Common/Foo.pl" will result
      in a new Perl file template called "Foo" in the "Common"
      folder of the "New File" dialog.

      source files:
          templates/

  lexers
      Komodo User-Defined Languages (UDL) system provides a
      facility for writing regular expression, state-based lexers
      for new languages (including for multi-lang languages).
      ".lexres" files are built from ".udl" source files with
      the "luddite" tool (in this SDK). See `koext help udl' and
      Komodo's UDL documentation for more details.

      source files:
          udl/
              *-mainlex.udl   # a .lexres will be build for each of these
              *.udl           # support files to be included by
                              #   "*-mainlex.udl" files

  XML catalogs
      An extension can include an XML catalog (and associates
      schemas) defining namespace to schema mappings for XML
      autocomplete.

      source files:
          catalog.xml         # Note: This may move to xmlcatalogs/...

  API catalogs
      An extension can include API catalogs to provide autocomplete
      and calltips for 3rd party libraries. An API catalog is a CIX
      file (an XML dialect) that defines the API of a
      library/project/toolkit.

      source files:
          apicatalogs/        # .cix files here will be included
                              #   in the API catalog list in the
                              #   "Code Intelligence" prefs panel

  Python modules
      An extension can supply Python modules by placing then in
      the "pylib" directory of the extension. This "pylib" directory
      will be appended to Komodo's Python runtime sys.path.

      source files:
          pylib/

  codeintel
      An extension can provide the Code
      Intelligence logic (for autocomplete and calltips, for
      "Jump to Definition" and for the Code Browser in Komodo IDE)
      for new languages.

      source files:
          pylib/              # lang_*.py files here are picked up
                              #   by the codeintel system.
</pre>
