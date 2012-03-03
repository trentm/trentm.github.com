---
layout: post
title: "Google Code -> GitHub"
published: true
---

Herein a walk-through of moving a project from Google Code to GitHub. The
project is "python-markdown2". It was single-commiter subversion project on
Google Code with one tag and no branches. It had (has) a number of issues in
the issue tracker, a few wiki pages and a few downloads.

This includes a couple tools I wrote for converting between Google Code
and GitHub project wikis and issue trackers. *Note:* I originally did this
migration almost a year ago, so I'm not positive whether recent changes
in the GitHub issues API might break this tool.


# github project

First create the new project on GitHub.


# source code repo

As per <http://help.github.com/svn-importing/>,
[svn2git](https://github.com/nirvdrum/svn2git) is preferred. At first I hit
an inscrutable error from 'svn2git':

    error: pathspec 'master' did not match any file(s) known to git

The only reference I could find with a cure was:

    http://mysz.tumblr.com/post/2515522812/git2svn-no-author-i-bledy-importu

which indicated that you need an entry in "authors.txt" for "(no author)",
something like so:

    (no author) = unknown author <unknown@example.com>

My first import attempt *appeared* to work, but failed to import all commits.
A subsequent attempt (this time with "--verbose" option) worked. Not sure if
"--verbose" makes a difference. I hope not. Here were my steps:

    $ cat ~/tm/authors.txt
    trentm = Trent Mick <trentm@gmail.com>
    (no author) = unknown author <unknown@example.com>
    $ mkdir ~/tm/python-markdown2
    $ cd ~/tm/python-markdown2
    $ svn2git https://python-markdown2.googlecode.com/svn --authors ~/tm/authors.txt
    W: -empty_dir: trunk/test/tm-cases/blog.markdown
    W: -empty_dir: trunk/test/tm-cases/extintro.markdown
    W: -empty_dir: trunk/test/tm-cases/link_defn_alt_title_delims.tags
    W: -empty_dir: trunk/test/tm-cases/safe_mode.html
    W: -empty_dir: trunk/test/tm-cases/safe_mode.opts
    W: -empty_dir: trunk/test/tm-cases/safe_mode.text
    W: -empty_dir: trunk/markdown2.py
    W: -empty_dir: trunk/bin/markdown2
    W: -empty_dir: trunk/test/tm-cases/issue31_gt_escaping.html
    W: -empty_dir: trunk/test/tm-cases/issue31_gt_escaping.tags
    W: -empty_dir: trunk/test/tm-cases/issue31_gt_escaping.text
    Found possible branch point: https://python-markdown2.googlecode.com/svn/trunk => https://python-markdown2.googlecode.com/svn/tags/v1.0.1.17, 240
    Use of uninitialized value $u in substitution (s///) at /usr/local/git/libexec/git-core/git-svn line 1731.
    Use of uninitialized value $u in concatenation (.) or string at /usr/local/git/libexec/git-core/git-svn line 1731.
    refs/remotes/trunk: 'https://python-markdown2.googlecode.com/svn' not found in ''

    Note: checking out 'trunk'.

    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by performing another checkout.

    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -b with the checkout command again. Example:

      git checkout -b new_branch_name

    HEAD is now at acb4fca... TODOne a while back
    error: branch 'master' not found.
    Switched to a new branch 'master'
    Counting objects: 1175, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (1069/1069), done.
    Writing objects: 100% (1175/1175), done.
    Total 1175 (delta 611), reused 0 (delta 0)
    Removing duplicate objects: 100% (256/256), done.

    HEAD is now at cb87cf8... Tweaks to 'header-ids' and 'toc' extras. Also add a ".postprocess(text)" hook for subclasses' convenience.
    Running command: git branch -D master
    Deleted branch master (was cb87cf8).
    Running command: git checkout -f -b master
    Switched to a new branch 'master'
    Running command: git gc
    Counting objects: 1290, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (1166/1166), done.
    Writing objects: 100% (1290/1290), done.
    Total 1290 (delta 681), reused 0 (delta 0)
    Removing duplicate objects: 100% (256/256), done.

Then a sanity check diffing the HEAD state in an svn working copy and a git
clone:

    $ diff -ru -x .svn -x .git python-markdown2.svn python-markdown2 | less
    diff -ru -x .svn -x .git python-markdown2.svn/externals/which/which.py python-markdown2/externals/which/which.py
    --- python-markdown2.svn/externals/which/which.py       2010-10-14 09:55:52.000000000 -0700
    +++ python-markdown2/externals/which/which.py   2011-01-31 21:14:20.000000000 -0800
    @@ -65,7 +65,7 @@
         files without executable access.
     """

    -__revision__ = "$Id: which.py 82 2007-11-06 05:44:22Z trentm $"
    +__revision__ = "$Id$"
     __version_info__ = (1, 1, 3)
     __version__ = '.'.join(map(str, __version_info__))
     __all__ = ["which", "whichall", "whichgen", "WhichError"]

That's an acceptable diff. I don't care about that "$Id$" expansion facility.

Now for ignore-patterns:

    $ cd python-markdown2
    $ svn propget svn:ignore ../python-markdown2.svn > .gitignore
    $ git add .gitignore
    $ git commit -m ".gitignore from svn:ignore" .gitignore
    [master d31e29e] .gitignore from svn:ignore
     1 files changed, 8 insertions(+), 0 deletions(-)
     create mode 100644 .gitignore

In general you'd have to walk the full svn working copy for 'svn:ignore'
properties on any directory. In my case I had a bunch to incorporate (manually)
into my ".gitignore" file:

    $ find . -type d | grep -v .svn | xargs svn pl -v .
    Properties on '.':
      svn:ignore
        *.pyc
        tmp
        externals
        dist
        MANIFEST
        build
        googlecode_upload.py

    Properties on 'externals':
      svn:ignore
        pygments

    Properties on 'externals/which':
      svn:ignore
        *.pyc

    Properties on 'lib':
      svn:ignore
        *.pyc

    Properties on 'perf':
      svn:ignore
        *.pyc
        *.prof
        tmp-*-cases

    Properties on 'sandbox':
      svn:ignore
        *.html

    Properties on 'test':
      svn:ignore
        *.pyc

Time to push this to github:

    cd .../python-markdown2
    git remote add origin git@github.com:trentm/python-markdown2.git
    git push origin master


# Google Code project page -> README.md

A Google Code project's front page is the wiki-formatted project page. A
GitHub project's front page (prose) is the README file. You might want to
start with your Google Code project wiki page content (at
<http://code.google.com/p/PROJNAME/admin>) and use that to create a README.md
(or README.txt or whatever). I already had a README.txt and I'm a Markdown
guy (duh) so I converted it to README.md to have it rendered nicely on my
GitHub project page.


# wiki pages

Google Code for a long time (from the get go?) allowed you to have a wiki for
your project whose content is in Subversion -- nice feature. GitHub more
recently added support for project wiki pages being in a git repo. This will
make moving wiki pages straightforward.

First, create your wiki on GitHub by clicking "Create Wiki Now" on
<https://github.com/USERNAME/PROJNAME/wiki>. Then let's get working copies of
the old and the new:

    cd ...
    svn co https://python-markdown2.googlecode.com/svn/wiki python-markdown2-wiki.svn
    git clone git@github.com:trentm/python-markdown2.wiki.git

At this point you could do a whole subversion history conversion to git, but
I don't care about the wiki editing history.

Let's just copy over and convert the files.

    python googlecode2github/wikiconvert.py \
        trentm/python-markdown2 \
        python-markdown2-wiki.svn \
        python-markdown2.wiki

"wikiconvert.py" is a tool I wrote to help with this conversion.
It doesn't cover the full Google Code wiki syntax, just enough for what
was my typical usage... so you may want to do some post tweaking. However,
it should be a good start. See <https://github.com/github/gollum> for details
on other wiki tweaks you can do on GitHub. "wikiconvert" lives here
<https://github.com/trentm/googlecode2github>.

Review, commit and push in 'python-markdown2.wiki':

    cd python-markdown2.wiki
    git add .
    git diff --staged
    git commit -m "convert wiki from code.google.com/python-markdown2 with 'googlecode2github/wikiconvert'"


# issues

Fully transplanting all issues (along with timing, status, user data, comments,
attachments, etc.) is a fool's errand. Instead we'll just create a shadow
issue for each google code issue so that (a) we have a pointer for all issues
from the new GitHub project and (b) there are no issue number collisions
when new issues are added on GitHub.

"googlecode2github/shadowissues.py" (see
<https://github.com/trentm/googlecode2github>) will do this for us. For each
shadow issue it'll try to reproduce the title, original description and the
closed/open state. To make changes you GH issues, the script will need you
github username and API token. The latter is available at
<https://github.com/account#admin_bucket>. The script will ask interactively
or you can add them to your "~/.gitconfig" via:

    git config --add github.user [github_username]
    git config --add github.token [github_api_token]

As a sanity check, **I suggest that you first run this against a test
github project** (e.g. I used "trentm/ghtest"). This is because
"shadowissues.py" wants the shadow issues to have the issue ids match those
in the Google Code project. You cannot delete issues on a github project (a
good thing) so you only get one chance:

    $ python .../googlecode2github/shadowissues.py python-markdown2 trentm/ghtest
    # Gathering code.google.com/p/python-markdown2 issues.
    # Gathering any github.com/trentm/ghtest issues.
    Migrating issue 1.
     from: http://code.google.com/p/python-markdown2/issues/detail?id=1
       to: https://github.com/trentm/ghtest/issues/1
    ...

Review those created GH-issues, then if things look good, run it for realz:

    $ python .../googlecode2github/shadowissues.py python-markdown2 trentm/python-markdown2
    # Gathering code.google.com/p/python-markdown2 issues.
    # Gathering any github.com/trentm/python-markdown2 issues.
    Migrating issue 1.
     from: http://code.google.com/p/python-markdown2/issues/detail?id=1
       to: https://github.com/trentm/python-markdown2/issues/1
    ...

One last change for issues: Now that you've moved to github, you want new issues
to be added there. You might want to change the Google Code new issue template to
something like this:

    NOTICE: This project has moved to <https://github.com/trentm/python-markdown2>.
    Please report your issue here:

    https://github.com/trentm/python-markdown2/issues

This can be done on the equivalent of
<http://code.google.com/p/python-markdown2/adminIssues> for your project.


# pointer from google code to github

A few extra touches for your Google Code project to provide pointers to
the new GitHub location.

- Summary: append ` (**MOVED TO GITHUB**)`
- Description: prepend `= Note: This project has been moved to [https://github.com/trentm/python-markdown2 trentm/python-markdown2 on GitHub]. =`
- Wiki pages: prepend `= Note: This project has been moved to [https://github.com/trentm/python-markdown2 trentm/python-markdown2 on GitHub]. =`
