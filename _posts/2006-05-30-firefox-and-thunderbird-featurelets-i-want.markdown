---
layout: post
title: Firefox and Thunderbird featurelets I want
date: 2006-05-30T00:30:00.009-07:00
published: true
categories: [programming, General, ui]
---

<p>I use <a href="http://www.mozilla.com/firefox/">Firefox</a> and <a href="http://www.mozilla.com/thunderbird/">Thunderbird</a>. (For the latter I recently switched from using mutt -- the last luddite at <a href="http://www.activestate.com/">work</a> to finally switch to one of them new fangled GUI things for email.) Here are a couple fixes/featurelets that I want in them.</p>

<ul>
    <li>I set Firefox to open new URLs in a new tab. This is the behaviour I want <strong>most</strong> of the time. However, there is the odd time that I want to lock a particular browser window. I.e., I'd like subsequent decisions on where to open a new URL to ignore this window.  For example, while editing this blog posting in my browser, I would like new URLs (ones I'm hunting for to link from this post) to open in another browser window. Ditto when I'm working on my calendar in the browser. Or in gmail. What if Firefox had a "pin" button (as provided in some Linux window managers)? That would be handy.</li>

    <li>Say you previously sent this email:

<pre>
    To: friend@example.com
    From: me@example.com
    Subject: Here are some pics from my weekend
</pre>

And, of course, you forgot to attach the pics. So you reply to your own email. In <a href="http://www.mutt.org/">mutt</a> and gmail when you reply to that email you get:

<pre>
    To: friend@example.com
    From: me@example.com
    Subject: Re: Here are some pics from my weekend
</pre>

In Thunderbird, when you "Reply All" you get these headers:

<pre>
    To: me@example.com
    Cc: friend@example.com
    Subject: Re: Here are some pics from my weekend
</pre>

That is just wrong. Even worse is when you just hit "Reply":

<pre>
    To: me@example.com
    Subject: Re: Here are some pics from my weekend
</pre>

I guess your friend just won't see how your weekend went.


[Update: I couldn't <a href="http://tinyurl.com/rdh4p">find</a> a bug for this so I added <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=339686">this one</a>.]


[Update 2: ... and quickly closed: "fixed for 2.0". Cool.]

</li>

</ul>
