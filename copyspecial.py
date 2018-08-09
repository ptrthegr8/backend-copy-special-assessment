#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    cmd = 'ls -l ' + dir
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    special_files = re.findall(r'\w+[_]\.\w+', output)
    special_paths = map(lambda x: os.path.abspath(
        os.path.join(dir, x)), special_files)
    return special_paths


def copy_to(paths, dir):
    if not os.path.exists(os.path.abspath(dir)):
        os.makedirs(os.path.abspath(dir))
    for path in paths:
        shutil.copy(path, os.path.abspath(dir))


def zip_to(paths, zippath):
    cmd = 'zip -j {} '.format(zippath) + " ".join(paths)
    print 'Command being run:', cmd
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    print output


def main(args=None):
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('from_dir', help='origin dir for special files')
    results = parser.parse_args(args)

    return (results.todir,
            results.tozip,
            results.from_dir)

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

if __name__ == "__main__":
    todir, tozip, from_dir = main(sys.argv[1:])
    if todir and from_dir:
        copy_to(get_special_paths(from_dir), todir)
    if tozip and from_dir:
        zip_to(get_special_paths(from_dir), tozip)
