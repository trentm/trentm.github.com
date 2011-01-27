---
layout: post
title: quick hack how to move a part of a Mercurial (hg) repo to git
published: true
---

My quick dirty hack to move a (small) part of a Mercurial (hg) repo to Git.
In my case this was for moving my single file "testlib.py" from
[here on bitbucket](http://bitbucket.org/trentm/sandbox/src/tip/testlib/)
to
[here on github](http://github.com/trentm/testlib/tree/master/lib/)

1. Dump the log of that part of the hg repo to a file.

        export WORKDIR=$HOME/tmp/migrate
        cd HGREPO/foo
        hg log -pv . > $WORKDIR/full.patch

2. Create the starter git repo

        cd $WORKDIR
        git init foo

3. Break up the log into a number of "changesetNNN.patch" files with this
   Python code:
   
        # parse.py
        import codecs
        changeset = []
        i = 0
        
        def write_changeset():
            global changeset
            if not changeset:
                return
            codecs.open("changeset%05d.patch" % i, 'w', "utf-8").write(''.join(changeset))
            i += 1
            changeset = []
        
        for line in open("full.patch"):
            if line.startswith("changeset:"):
                write_changeset()
            changeset.append(line)
        write_changeset()

    and then run:
    
        python parse.py

4. Apply and commit each patch with this Python script

        # Usage: python apply.py TARGET-REPO-BASE-DIR
        import os
        from os.path import *
        from glob import glob
        import subprocess
        from pprint import pprint
        
        def apply_patch(target_repo_base_dir, patch_path):
            content = open(patch_path).read()
            header, diff = content.split('\n\n\n', 1)
            assert diff.startswith("diff --git a")
            fields = {}
            lines = header.splitlines(False)
            for i, line in enumerate(lines):
                key, value = line.split(':', 1)
                if key == "description":
                    fields[key] = '\n'.join(lines[i+1:])
                    break
                value = value.strip()
                fields[key] = value
            # Do any path renamings here. For example, I wanted to move from
            # "testlib/testlib.py" in the old repo to "lib/testlib.py" in the new.
            diff = diff.replace('a/testlib/testlib.py', 'a/lib/testlib.py')
            diff = diff.replace('b/testlib/testlib.py', 'b/lib/testlib.py')
            f = open(patch_path+".diff", 'w')
            f.write(diff)
            f.close()
            f = open(patch_path+".msg", 'w')
            f.write(fields["description"])
            f.close()
            cwd = target_repo_base_dir
            subprocess.check_call(['git', 'apply', '--whitespace=nowarn',
                abspath(patch_path+".diff")], cwd=cwd)
            subprocess.check_call(['git', 'add', 'lib/testlib.py'], cwd=cwd)
            subprocess.check_call(['git', 'commit', '--date', fields["date"],
                '-F', abspath(patch_path+".msg")], cwd=cwd)
        
        if __name__ == "__main__":
            target_repo_base_dir = sys.argv[1]
            patches = list(sorted(glob("changeset*.patch")))
            for patch_path in patches:
                print "--", patch_path
                apply_patch(target_repo_base_dir, patch_path)

    Then run:
    
        python apply.py foo    # apply all changeset*.patch files to "foo" git repo
        
Now you can push this Git repo to github or whereever.


# To improve on

- You currently need to manually create the dir structure first.
- This doesn't currently used the parse "user" field from the hg commit log
  for the "git commit -a AUTHOR" command. Mainly this is because I didn't need
  that, but also because the "user" value in the hg log isn't the configured
  full user name and email, but just the short username. Maybe that was just me.


