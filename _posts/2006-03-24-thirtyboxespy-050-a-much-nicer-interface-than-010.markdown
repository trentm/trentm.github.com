---
layout: post
title: "thirtyboxes.py 0.5.0: a much nicer interface than 0.1.0"
date: 2006-03-24T14:49:00.009-08:00
published: true
categories: [python, programming, General]
---

<p>I've put up a new thirtyboxes.py binding to the <a href="http://30boxes.com/">30boxes</a> <a href="http://www.30boxes.com/api/">web API</a>: <a href="http://code.google.com/p/python-thirtyboxes/">http://code.google.com/p/python-thirtyboxes/</a></p><p>For example:</p><pre>>>> import thirtyboxes
>>> tb = thirtyboxes.ThirtyBoxes()
>>> tb.find_user(1)
{'avatar': 'http://static.flickr.com/25/97988637_27ec96a24f_o.jpg',
'createDate': datetime.date(2005, 9, 10),
'firstName': 'Nick',
'id': 1,
...}

>>> from datetime import date, timedelta
>>> today = date.today()
>>> tomorrow = today + timedelta(1)
>>> tb.events(start=today, end=tomorrow)
{'events': [{'allDayEvent': False,
     'end': datetime.datetime(2006, 3, 25, 22, 0),
     'id': 156569,
     'invitation': {'isInvitation': False},
     'notes': ''
     'privacy': 'shared',
     'repeatEndDate': None,
     'repeatType': 'no',
     'start': datetime.datetime(2006, 3, 25, 19, 0),
     'summary': 'Bagpipe practice',
     'tags': 'pipes'}],
 'listEnd': datetime.date(2006, 3, 26),
 'listStart': datetime.date(2006, 3, 25),
 'userId': 1234}

>>> tb.search('caber toss')
...returns events for caber tossing
</pre><p>Or, from the command line</p><pre>$ alias 30b='python -m thirtyboxes.py'
$ 30b user 1234
--- 30boxes user
name           : Hamish McDonald
id             : 1234
personalSite   : http://hamish.example.com/
avatar         : ...
createDate     : 2006-02-05
startDay       : 0
use24HourClock : False
feeds          :
- hamish's Photos (http://www.flickr.com/services/feeds/pho...
</pre><p>Any feedback is appreciated.</p>
