---
layout: post
title: using gmail for outbound email on Mac OS X
published: true
---

# Using gmail for outbound email on Mac OS X

At work I run a number of cron jobs: web log analysis scripts, metrics
gathering, db migration for beta versions of some sites, etc. However, one
thing I've been unable to use effectively on my Mac machines [^1] is
the `MAILTO` facility of cron. Given a foo.cron script like this:

    #!/bin/sh
    export MAILTO=me@example.com
    export SUBJECT="do some daily stuff"

    ...

that is run like this:

    0 0 * * *  $HOME/.../foo.cron > $HOME/var/log/do-some-daily-stuff.log

any output to stderr with be mailed to "me@example.com". That is, it *would* if outgoing email was setup for the currently running MTA (mail transfer agent) on that machine. 

On Mac OS X (since Leopard, I think) the default MTA is Postfix, and Postfix's terminology
for "handle outbound email" is to set the "relayhost". [This
post](http://www.installationexperiences.com/2008/10/using-gmail-for-outbound-smtp-on-mac-os.html)
explains how to configure Postfix on Mac OS X 10.5 (Tiger). What follows is my
summary of the commands -- slightly different than the other post for clarity -- plus a
few thoughts.  Please read the other post for extra details.

    # Create `/etc/postfix/relay_password` with auth information like this:
    #   smtp.gmail.com YOURNAME@gmail.com:YOURPASSWORD
    $ sudo vi /etc/postfix/relay_password
    $ cat /etc/postfix/relay_password
    smtp.gmail.com YOURNAME@gmail.com:YOURPASSWORD

    # Compile this to a Postfix lookup table...
    $ sudo postmap /etc/postfix/relay_password

    # ... and test it.
    $ sudo postmap -q smtp.gmail.com /etc/postfix/relay_password
    YOURNAME@gmail.com:YOURPASSWORD

    # Download the Thawte root certificates from
    # <https://www.verisign.com/support/roots.html> and setup
    # a certificate for Postfix.
    $ firefox https://www.verisign.com/support/roots.html
    $ cd ~/Downloads
    $ unzip -q roots.zip
    $ sudo mkdir /etc/postfix/certs
    $ sudo cp ~/Downloads/Thawte\ Root\ Certificates/Thawte\ Root\ Certificates/thawte\ Premium\ Server\ CA/Thawte\ Premium\ Server\ CA.pem /etc/postfix/certs
    $ sudo c_rehash /etc/postfix/certs/
    Doing /etc/postfix/certs/
    Thawte Premium Server CA.pem => d44d72e8.0

    # Add the following lines to `/etc/postfix/main.cf`:
        relayhost = smtp.gmail.com:587
        # auth
        smtp_sasl_auth_enable = yes
        smtp_sasl_password_maps = hash:/etc/postfix/relay_password
        smtp_sasl_security_options = noanonymous
        # tls
        smtp_tls_security_level = may
        smtp_tls_CApath = /etc/postfix/certs
        smtp_tls_session_cache_database = btree:/etc/postfix/smtp_scache
        smtp_tls_session_cache_timeout = 3600s
        smtp_tls_loglevel = 1
        tls_random_source = dev:/dev/urandom

    # Re-start the Postfix service. (Note: You can also do the re-starting via
    # `launchctl`.)
    sudo postfix stop
    sudo postfix start

    # Now test this by sending email with `mail`:
    $ /usr/bin/mail -s "testing 1 2 3" recipient@example.com
    Howdy, from Postfix on your Mac!
    .
    EOT

Now `recipient@example.com` should have received your test email. If not
check "/var/log/mail.log". Here is a successful log message:

    Nov 10 23:33:26 mower postfix/smtp[56627]: ED1265BBA2A: to=<recipient@example.com>, relay=smtp.gmail.com[74.125.155.109]:587, delay=2.9, delays=0.44/0.94/0.56/0.96, dsn=2.0.0, status=sent (250 2.0.0 OK 1257924806 20sm930503pxi.15)

Here is a **failing** log message (in this case because I'd incorrectly mixed
using "smtp.googlemail.com" instead of "smtp.gmail.com"):

    Nov 10 21:32:14 mower postfix/smtp[55593]: C028D5BB6F8: to=<recipient@example.com>, relay=smtp.googlemail.com[74.125.155.16]:587, delay=0.33, delays=0.05/0.02/0.24/0.02, dsn=5.5.1, status=bounced (host smtp.googlemail.com[74.125.155.16] said: 530-5.5.1 Authentication Required. Learn more at                               530 5.5.1 http://mail.google.com/support/bin/answer.py?answer=14257 20sm817933pxi.3 (in reply to MAIL FROM command))

This setup requires putting your Gmail password in plaintext in
`/etc/postfix/relay_password`, which I'm not too happy about. So I've created a
separate Gmail account with a different password to use for this.

One of the beauties of this setup is that there is a record of all the emails
that have been sent this way in that Gmail account's "Sent mail".



[^1]: I have a Macbook that is my main machine and a Mac Pro that is used for running most of our Komodo builds and some of the heavy log analysis scripts that I run.

