---
layout: post
title: building MSI patch packages (.msp) with WiX
date: 2007-05-29T03:32:00.009-07:00
published: true
categories: [wix, install, komodo, programming, mozilla]
---

<p>This post includes a complete and concrete example of building an MSI patch package (a .msp file to upgrade an existing .msi installation) with WiX.</p>

<h3>Background</h3>

<p>I'm responsible for building the <a href="http://www.activestate.com/products/activepython/">ActivePython</a> and <a href="http://www.activestate.com/products/komodo_ide/">Komodo</a> installers at <a href="http://www.activestate.com/">ActiveState</a>. On Windows we build MSI packages for installation.</p>

<p>Currently I'm investigating auto-update support for Komodo 4.2. Because Komodo is based on Firefox/Mozilla we can benefit from the excellent <a href="http://wiki.mozilla.org/Software_Update">Mozilla update system</a> (I'll write another post about our experience with it). However, integrating with an MSI-based installation isn't something the Mozilla update system does out of the box: Firefox and Thunderbird don't use MSI for their installers (they use NSIS), hence I suspect working with MSI was never a design consideration.</p>

<p>While working out how to best marry MSI and Moz update, I investigated producing MSI patch packages (.msp files) for Komodo updates. MSI is a complex and complicated technology (it would be nice if the latter, at least, wasn't the case). Back in the day I used InstallShield for building our MSI packages, but now <a href="http://wix.sourceforge.net/">WiX</a> is the best way to build .msi's -- by far.  WiX helps a lot, but building appropriate MSI packages is still quite difficult. The following two pages helped me get to successfully building .msp's. Hopefully this concrete example will help others too.</p>

<ul>
<li><a href="http://wix.sourceforge.net/manual-wix2/patch_building.htm">Patch Building</a></li>
<li><a href="http://www.tramontana.co.hu/wix/lesson4.php">Wix Tutorial - Part 4</a> </li>
</ul>

<h3>ActiveFoo 1.0</h3>

<p>For this example we'll build .msi installers for versions 1.0.0 and 1.0.1 of the the mythical "ActiveFoo" app ("activefoo-1.0.0.msi" and "activefoo-1.0.1.msi"). Then we'll build a '.msp' that will upgrade a 1.0.0 install to 1.0.1. We'll have the following files:</p>

<pre>
1.0.0/
    activefoo.wxs       # This describes "activefoo-1.0.0.msi"
    config.wxi
    installimage/       # The ActiveFoo install image
        CHANGES.txt
        foo.exe
        README.txt
1.0.1/
    activefoo.wxs       # This describes "activefoo-1.0.1.msi"
    config.wxi
    installimage/       # The install image with changes for 1.0.1
        CHANGES.txt
        README.txt
    upgrade-1.0.0.wxs   # This describes the '.msp'.
make.py                 # 'python make.py' to build everything
README.txt
</pre>

<p>Here is a <a href="http://dl.getdropbox.com/u/1301040/blog/2007/05/wix_and_msp/wix_and_msp.zip">zip of the working files</a> for this example, if you'd like to play along.</p>

<p>We have a simple install image with three files (foo.exe, README.txt and CHANGES.txt). The WiX code to build an installer for ActiveFoo 1.0.0 is <a href="http://dl.getdropbox.com/u/1301040/blog/2007/05/wix_and_msp/1.0.0/activefoo.wxs">1.0.0/activefoo.wxs</a>:</p>

<pre>
&lt;?xml version="1.0" encoding="utf-8"?&gt;

&lt;?include config.wxi ?&gt;

&lt;Wix xmlns="http://schemas.microsoft.com/wix/2003/01/wi"&gt;
  &lt;Product Name="$(var.ProductName)" Id="$(var.ProductCode)"
           Language="1033" Codepage="1252" Version="$(var.ProductVersion)"
           Manufacturer="Acme" UpgradeCode="$(var.UpgradeCode)"&gt;

    &lt;Package Id="????????-????-????-????-????????????" Keywords="Installer"
      Description="$(var.ProductName)"
      Comments="blah blah" Manufacturer="Acme"
      InstallerVersion="200" Languages="1033" Compressed="yes"
      SummaryCodepage="1252" /&gt;

    &lt;Media Id="1" Cabinet="media.cab" EmbedCab="yes" /&gt;

    &lt;!-- Define some of the dir-structure. --&gt;
    &lt;Directory Id="TARGETDIR" Name="SourceDir"&gt;
      &lt;Directory Id="ProgramFilesFolder" Name="PFILES"&gt;
        &lt;Directory Id="INSTALLDIR" Name="$(var.InstallId)"
                   LongName="$(var.InstallName)" /&gt;
      &lt;/Directory&gt;
    &lt;/Directory&gt;

    &lt;!-- Define the feature hierarchy (just one feature in this simple
         example). --&gt;
    &lt;Property Id="INSTALLLEVEL" Value="1000" /&gt;
    &lt;Feature Id="core" Title="ActiveFoo" Description="The Foo core"
             Level="1"&gt;
      &lt;ComponentRef Id="MainExe" /&gt;
      &lt;ComponentRef Id="ReadMeFiles" /&gt;
    &lt;/Feature&gt;

    &lt;!-- Define all the components. --&gt;
    &lt;DirectoryRef Id="INSTALLDIR"&gt;
      &lt;Component Id="MainExe" Guid="6ee6fda3-6f50-47bf-99b9-6031c720428e"&gt;
        &lt;File Id="MainExe" Name="foo.exe" DiskId="1"
              src="installimage\foo.exe" Vital="yes" /&gt;
      &lt;/Component&gt;
      &lt;Component Id="ReadMeFiles" DiskId="1"
                 Guid="8f2255f3-3eaf-4c82-9688-3545cd9b2018"&gt;
        &lt;File Id="README.txt" Name="README.txt"
              src="installimage\README.txt" /&gt;
        &lt;File Id="CHANGES.txt" Name="CHANGES.txt"
              src="installimage\CHANGES.txt" /&gt;
      &lt;/Component&gt;
    &lt;/DirectoryRef&gt;

  &lt;/Product&gt;
&lt;/Wix&gt;
</pre>

<p>with some configuration variables included from <a href="http://dl.getdropbox.com/u/1301040/blog/2007/05/wix_and_msp/1.0.0/config.wxi">1.0.0/config.wxi</a>:</p>

<pre>
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;Include&gt;
  &lt;?define ProductCode = "cdc5e50f-b490-4a37-8ff6-22e3cb3d690e" ?&gt;
  &lt;?define UpgradeCode = "ed340ed8-aa91-4bf6-9dcf-d7f6f4d43737" ?&gt;

  &lt;?define ProductName = "ActiveFoo" ?&gt;
  &lt;?define InstallName = "ActiveFoo" ?&gt;
  &lt;?define InstallId = "AFoo10" ?&gt;
  &lt;?define ProductVersion = "1.0.0" ?&gt;
  &lt;?define ProductURL = "http://www.example.com/products/activefoo/" ?&gt;
&lt;/Include&gt;
</pre>

<p>(Note that this WiX project is simplistic. In a real world WiX project you'd
likely have a <em>UI</em> element for a user UI, define Add/Remove Programs -- ARP
-- properties, etc.)</p>

<p>Use the provided "make.py" script to build "activefoo-1.0.0.msi":</p>

<pre class="dos">
C:\tmp\wix_and_msp&gt; python make.py -v 100
INFO:make:build target '100'
DEBUG:make:running 'candle -nologo activefoo.wxs' in '1.0.0'
activefoo.wxs
DEBUG:make:running 'light -nologo -o ../activefoo-1.0.0.msi activefoo.wixobj' in '1.0.0'
INFO:make:'activefoo-1.0.0.msi' created
</pre>

<p>and install it. You should now have a "ActiveFoo" folder in your "Program Files".</p>

<h3>ActiveFoo 1.0.1</h3>

<p>Version 1.0.1 has the following changes:</p>

<ol>
<li>The ProductVersion is incremented to 1.0.1. We aren't change the ProductCode
so this qualifies in MSI parlance as a
"<a href="http://msdn2.microsoft.com/en-us/library/aa370579.aspx">minor
upgrade</a>", as opposed to a "small update" or a "major upgrade").</li>
<li>We've added a note to "CHANGES.txt" for the new release.</li>
<li>We've removed the "foo.exe" file from the install image. This is so we can
see how file removal can be accomplished with a "minor upgrade". There is
a lot of documentation out there than says that file removal can't be done
with an MSI minor upgrade. We'll see that that isn't true. I haven't seen
any justification for why minor upgrades shouldn't remove files.</li>
</ol>

<p>Normally, for these changes, the only updates to the WiX sources to build
"activefoo-1.0.1.msi" would be to (a) update the "ProductVersion" string and
(b) remove the <em>File</em> and <em>Component</em> elements for "foo.exe". However, working
from this comment in
<a href="http://www.installsite.org/files/iswi/Upgrading.html">Minor and
Major Upgrades Using IPWI</a>:</p>

<pre><code>If you need to remove any files or registry data during the upgrade, add
records to the RemoveFile or RemoveRegistry tables of the newer database.
</code></pre>

<p>I've found that to get WiX to put a <em>RemoveFile</em> entry for, in this case,
"foo.exe", I needed to add an explicit <em>RemoveFile</em> element:</p>

<pre>
      ...
      &lt;Component Id="MainExe" Guid="6ee6fda3-6f50-47bf-99b9-6031c720428e"&gt;
        &lt;!-- Note: This is how to explicitly remove files in an update. --&gt;
        &lt;RemoveFile Id="removefile1" On="install" Name="foo.exe"/&gt;
      &lt;/Component&gt;
      ...
</pre>

<p>The ProductVersion we updated in "<a href="http://dl.getdropbox.com/u/1301040/blog/2007/05/wix_and_msp/1.0.1/config.wxi">1.0.1\config.wxi</a>":</p>

<pre class="dos">
C:\tmp\wix_and_msp&gt;diff -u 1.0.0\config.wxi 1.0.1\config.wxi
--- 1.0.0\config.wxi    Mon May 28 17:33:01 2007
+++ 1.0.1\config.wxi    Mon May 28 17:33:03 2007
@@ -6,7 +6,7 @@
   &lt;?define ProductName = "ActiveFoo" ?&gt;
   &lt;?define InstallName = "ActiveFoo" ?&gt;
   &lt;?define InstallId = "AFoo10" ?&gt;
-  &lt;?define ProductVersion = "1.0.0" ?&gt;
+  &lt;?define ProductVersion = "1.0.1" ?&gt;
   &lt;?define ProductURL = "http://www.example.com/products/activefoo/" ?&gt;
 &lt;/Include&gt;
</pre>

<p>Now we can build "activefoo-1.0.1.msi":</p>

<pre class="dos">
C:\tmp\wix_and_msp&gt; python make.py -v 101
INFO:make:build target '101'
DEBUG:make:running 'candle -nologo activefoo.wxs' in '1.0.1'
activefoo.wxs
DEBUG:make:running 'light -nologo -o ../activefoo-1.0.1.msi activefoo.wixobj' in '1.0.1'
INFO:make:'activefoo-1.0.1.msi' created
</pre>

<h3>ActiveFoo 1.0.1 update</h3>

<p>The basic process for building a '.msp' is:</p>

<ol>
<li>Get an administrative install of the old version. I hadn't known this
before: An administrative install effective just extracts the file payload
from an .msi into a given directory leaving a lighter .msi with just the
MSI database tables. AFAIK this is the same thing as if you had built an
"uncompressed MSI" -- i.e. one in which <code>&lt;Package Compressed='no'
.../&gt;</code>. <em>make.py</em> will put this in "1.0.1\build\before".</li>
<li>Get an administrative install of the new version. <em>make.py</em> will put this
in "1.0.1\build\after".</li>
<li>Write a WiX file that describes the patch.</li>
<li>Compile to a <em>Patch Creation Properties</em> (.pcp) file with WiX.</li>
<li>Compile to a '.msp' file with the "msimsp.exe" utility from the MSI SDK
(Part of the Microsoft Platform SDK).</li>
</ol>

<p>Here is a our WiX file describing the patch (<a href="http://dl.getdropbox.com/u/1301040/blog/2007/05/wix_and_msp/1.0.1/upgrade-1.0.0.wxs">1.0.1\upgrade-1.0.0.wxs</a>) with comments inline:</p>

<pre>
&lt;?xml version='1.0' encoding='windows-1252'?&gt;

&lt;Wix xmlns='http://schemas.microsoft.com/wix/2003/01/wi'&gt;
  &lt;!-- TODO: Update PatchCreation Id for each new patch.
             Can we just use WiX's '????????-????-????-????-????????????' ? --&gt;
  &lt;PatchCreation Id='e8ee6400-7877-47e4-9519-ce17e3f1d59b'
                 CleanWorkingFolder='yes'
                 WholeFilesOnly='no'
                 AllowMajorVersionMismatches='yes'
                 AllowProductCodeMismatches='no'&gt;

    &lt;PatchInformation Description="ActiveFoo 1.0.1 Patch"
                      Comments='blah blah'
                      Manufacturer='Acme'
                      Languages='1033'
                      Compressed='yes' /&gt;

    &lt;!-- TODO: Play with other values of 'Classification'. Does msiexec's
         behaviour actually change for different values? --&gt;
    &lt;PatchMetadata Description="ActiveFoo 1.0.1 Patch"
                   DisplayName="ActiveFoo 1.0.1 Patch"
                   TargetProductName='ActiveFoo 1.0'
                   ManufacturerName='Acme'
                   MoreInfoURL='http://www.example.com/products/activefoo'
                   Classification='Update'
                   AllowRemoval='yes' /&gt;

    &lt;!-- From &lt;http://wix.sourceforge.net/manual-wix2/patch_building.htm&gt;
         """
         The SequenceStart value is influenced by the number of files that
         the previous patch delivered, as well as the number of files that
         this patch will deliver. This tells PatchWiz.dll to start assigning
         File sequence numbers from this number. So if this patch ships 11
         files, and the next patch uses a SequenceStart of 1020, it will step
         on the 11th file's assigned sequence number. In this case the next
         patch would use a SequenceStart of 1030, and 03 as the patch id to
         avoid conflicts with this patch. This scheme helps prevent this by
         coordinating the SequenceStart (file sequence numbers) with the
         patch sequence number. Also, note that the SequenceStart of the
         first patch must be greater than the number of files in the original
         installation. If the original installation contained more than 1000
         files(rare), then the SequenceStart for the first patch must be set
         to a higher value (e.g 2010.)
         """
    --&gt;
    &lt;!-- Name is max 8 chars. *How* unique does this have to be? --&gt;
    &lt;Family Name='Fam101' DiskId='2' MediaSrcProp='AFoo10_2_1_01'
            SequenceStart='1010'&gt;
      &lt;UpgradeImage Id='AFoo10Upgrade'
                    SourceFile='after\activefoo-1.0.1.msi'&gt;
        &lt;TargetImage Id='AFoo10Target' Order='1' IgnoreMissingFiles='no'
                     SourceFile='before\activefoo-1.0.0.msi' /&gt;
      &lt;/UpgradeImage&gt;
    &lt;/Family&gt;

    &lt;TargetProductCode Id='cdc5e50f-b490-4a37-8ff6-22e3cb3d690e' /&gt;
  &lt;/PatchCreation&gt;
&lt;/Wix&gt;
</pre>

<p>Use <em>make.py</em> to build the patch:</p>

<pre class="dos">
C:\tmp\wix_and_msp&gt; python make.py -v 101_upgrade
INFO:make:build target '101_upgrade'
DEBUG:make:running 'msiexec /a activefoo-1.0.0.msi TARGETDIR=C:\tmp\wix_and_msp\1.0.1\build\before'
DEBUG:make:running 'msiexec /a activefoo-1.0.1.msi TARGETDIR=C:\tmp\wix_and_msp\1.0.1\build\after'
        1 file(s) copied.
DEBUG:make:running 'candle -nologo upgrade.wxs' in 'C:\tmp\wix_and_msp\1.0.1\build'
upgrade.wxs
DEBUG:make:running 'light -nologo upgrade.wixobj' in 'C:\tmp\wix_and_msp\1.0.1\build'
DEBUG:make:running '"C:\Program Files\Microsoft Platform SDK\Samples\SysMgmt\Msi\Patching\MsiMsp.Exe" -s upgrade.pcp -p C:\tmp\wix_and_msp\activefoo-1.0.1-upgrade-1.0.0.msp -l upgrade.log' in 'C:\tmp\wix_and_msp\1.0.1\build'
INFO:make:'activefoo-1.0.1-upgrade-1.0.0.msp' created
INFO:make:To install the update, run:
  msiexec /p activefoo-1.0.1-upgrade-1.0.0.msp REINSTALL=ALL REINSTALLMODE=omus
</pre>

<p>You should now be able to install "activefoo-1.0.1-upgrade-1.0.0.msp" over an
ActiveFoo 1.0.0 installation to upgrade to ActiveFoo 1.0.1. Note that some docs
out there mention an MSI bug preventing installation of a '.msp' by double-clicking
on that. I've found that I <em>am</em> able to install by double-clicking on my WinXP box
with Windows Installer V 3.01.4000.1823.</p>

<h3>Notes/Limitations</h3>

<ol>
<li>Having to explicitly put in <em>RemoveFile</em> elements to ensure upgrades remove
them is a pain. It would be nice if WiX inferred that automatically. WiX v3 is
<a href="http://wix.sourceforge.net/faq.html">slated to include</a> "Patch
creation support" and "ClickThrough". Perhaps these will go a long way to
making all of this easier.</li>
<li>There are many variables to tweak here that I haven't played with. I haven't
deployed any .msp's built as describe here to users on any scale so I
there may be gremlins lurking in this procedure.</li>
</ol>

<p>I'd be happy to hear about others' experiences working with WiX and MSI patches.</p>
