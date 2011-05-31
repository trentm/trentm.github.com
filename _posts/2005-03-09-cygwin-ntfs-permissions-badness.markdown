---
layout: post
title: cygwin + NTFS permissions = badness
date: 2005-03-09T03:03:00.009-08:00
published: true
categories: [programming]
---

<p><a href="http://www.cygwin.com/">Cygwin</a> is "a Linux-like environment for Windows." Basically it provides all (or at least a large set) of the standard Linux command line tools for Windows. A lot of open source projects (e.g. Mozilla, for a big one) have based their Windows build systems on Cygwin because it simplifies the problems with trying to get a <code>make</code>-based build system to work on Windows.</p>

<p>NTFS (the file system for WinNT, Win2k, WinXP, Win2k3) uses Access Control Lists (ACLs) for managing file permissions. If you have ever been frustrated by not being able delete a file on Windows: <a href="http://support.microsoft.com/default.aspx?scid=kb;en-us;320081">your NTFS ACLs might be the culprit</a>.</p>

<p>I don't pretend to fully understand NTFS ACLs, but follow along with this little experiment and decide if you think there is a problem waiting to happen here. For this experiment you'll need <a href="http://www.microsoft.com/windows2000/techinfo/reskit/tools/existing/xcacls-o.asp"><code>xcacls.exe</code> from the Windows Resource Kit</a>. This is a little command-line tool for dumping NTFS ACL information. You can also view ACL information by opening the "Propeties" dialog for a file in Explorer and selecting the "Security" tab.</p>

<p>First let's create a small test file in the regular Windows command shell (<code>cmd.exe</code>) and list the NTFS ACL information:</p>

<pre>
C:\temp>echo this is foo.txt > foo.txt

C:\temp>xcacls foo.txt
C:\temp\foo.txt BUILTIN\Administrators:F
                ACTIVE\trentm:F
                NT AUTHORITY\SYSTEM:F
                BUILTIN\Users:R
</pre>

<p>This seems reasonable: the "Administrators", "trentm" (that's me), and "SYSTEM" users have full (F) permissions on that file and the "Users" account has read (R) access.</p>

<p>Now let's create a file using one of the cygwin utilities and dump the NTFS ACL information. I'll use <code>tee</code> here, but other tools that create files (like <code>tar</code>, <code>gzip</code>, etc.) will have the same result.</p>

<pre>
C:\temp>echo this is bar.txt | tee bar.txt
this is bar.txt

C:\temp>xcacls bar.txt
C:\temp\bar.txt ACTIVE\trentm:(special access:)
                              STANDARD_RIGHTS_ALL
                              DELETE
                              READ_CONTROL
                              WRITE_DAC
                              WRITE_OWNER
                              SYNCHRONIZE
                              STANDARD_RIGHTS_REQUIRED
                              FILE_GENERIC_READ
                              FILE_GENERIC_WRITE
                              FILE_READ_DATA
                              FILE_WRITE_DATA
                              FILE_APPEND_DATA
                              FILE_READ_EA
                              FILE_WRITE_EA
                              FILE_READ_ATTRIBUTES
                              FILE_WRITE_ATTRIBUTES

                BUILTIN\Users:(special access:)
                              READ_CONTROL
                              SYNCHRONIZE
                              FILE_GENERIC_READ
                              FILE_GENERIC_WRITE
                              FILE_READ_DATA
                              FILE_WRITE_DATA
                              FILE_APPEND_DATA
                              FILE_READ_EA
                              FILE_WRITE_EA
                              FILE_READ_ATTRIBUTES
                              FILE_WRITE_ATTRIBUTES

                Everyone:(special access:)
                         READ_CONTROL
                         SYNCHRONIZE
                         FILE_GENERIC_READ
                         FILE_GENERIC_WRITE
                         FILE_READ_DATA
                         FILE_WRITE_DATA
                         FILE_APPEND_DATA
                         FILE_READ_EA
                         FILE_WRITE_EA
                         FILE_READ_ATTRIBUTES
                         FILE_WRITE_ATTRIBUTES
</pre>

<p>I don't want to unnecessarily ring alarm bells because my experience has shown that this usually doesn't cause problems in normal usage of the cygwin tools (we use them heavily here at ActiveState). However, yesterday <strong>something</strong> happened with respect to NTFS ACLs on my Windows developement machine yesterday such that I no longer have write permissions for files created by the Cygwin tools. I can't help but think that the difference in ACL information for <code>foo.txt</code> and <code>bar.txt</code> in this experiment is part of the problem.</p>
