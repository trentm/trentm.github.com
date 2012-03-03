---
layout: post
title: Thoughts on Google Chrome -> Firefox
published: true
date: 2012-03-03T14:16:37.857274
categories: []
---

I recently switched from Google Chrome (back) to Firefox -- currently Aurora
(12.0a2). Some thoughts.

The main thing that brought me back is the Awesome Bar. Firefox's algorithm for
suggestions/auto-complete in the Awesome Bar is just much better than Google
Chrome's. In Chrome I often found myself frustrated that I wouldn't get, e.g.
"https://dev.example.com/jira/browse/OS-123" suggested when entering "OS" or
"OS-" or "OS-1" when I'd been using that URL frequently and recently.
Yeah for FF's frecency.

Love FF's Awesome Bar suggesting "switch to tab" if I already have one
of the hits open.


# Chrome Pros (I.e., please steal these Firefox)

- search in page:
    - i like it at the top
    - it goes away under conditions where FF's sticks around. Not sure
      what those conds are yet
    - I like that that it shows how many hits on the whole page.
    - I like that it highlights *all* in one color and the current hit
      in another color. Actually Firefox's search in page offers "highlight
      all", but it isn't the default.
    - **showing where the hits are on the scrollbar is huge**
- I like that I have a bookmarks bar on the default chrome new tab page
  I don't want a permanent bookmarks bar: only when opening a new page.
- Like the "right-click > Close Tabs to the Right" to clean up after a digression.


# Firefox Cons

- Cmd+A in a listbox in Chrome selects all. No so in FF.
- Holy crazy hard to set FF as the default browser. Online instructions
  (back around Firefox 8 time) used to say to use *Safari*. Lame.
  Now in Aurora I find this option buried in the "Advanced" prefs pane.
  In Safari this is the first option.
- The url popup at the bottom when hovering over links is on the left by
  default (good), but is on the right when the search bar is up!? Why?
  Because the search bar is stickier than I think it should be (Esc doesn't
  always close it), it is unpredicatable where that URL popup is.
- HTTP basic auth sheet is on the whole window, rather than specific to a
  tab. Sometimes I want to click back to another tab to copy/paste the
  username/password creds (e.g. to my gmail).

# Firefox RFEs

- Aurora "Inspect Element": I want this to remember which panes I had open,
  e.g. whether the "HTML" and "Style" buttons were pressed.


Yes, I should open tickets for all these things. I'm hoping this post will
so motivate me.
