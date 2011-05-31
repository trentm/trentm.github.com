---
layout: post
title: thirtyboxes.py &mdash; a Python 30boxes.com API
date: 2006-02-23T16:58:00.009-08:00
published: true
categories: [python, programming, ui]
---

<p><a href="http://30boxes.com/">30boxes.com</a> is a nice web calendaring service, <a href="http://www.joelonsoftware.com/items/2006/02/08.html">maligned</a> somewhat by Joel Spolsky. I've been using <a href="http://www.trumba.com/">Trumba</a> for a while, but have now switched to 30boxes. So far I am pretty happy with the change. The "One Box" (any name for it would have been cheesy) is a great answer to the tedium of adding events quickly.</p>

<p>30boxes.com has started adding a <a href="http://30boxes.com/api/">web API</a> <a href="http://30boxes.com/blog/index.php/2006/02/10/hacking-30-boxes-already/">as promised</a> (it is read-only right now). I've cobbled together <a href="http://code.google.com/p/python-thirtyboxes/">a Python binding to this API</a>. I hope some folks find it useful. Please let me know if you love it, hate it, have problems with it, whatever.</p>

<pre>$ python
&gt;&gt;&gt; import thirtyboxes
&gt;&gt;&gt; thirtyboxes.events_TagSearch("work")
'&lt;?xml version="1.0" encoding="ISO-8859-1"?&gt;
&lt;rsp stat="ok"&gt;
&lt;eventlist&gt;
...'
</pre>
