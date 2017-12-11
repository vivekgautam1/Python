#!/usr/bin/env python

import sys

print sys.argv

fname = sys.argv[1]
with open(fname, "r") as f:
    content = f.readlines()

content = [x.strip() for x in content]
print content
if any(sys.argv[2] in s for s in content):
    print "Failure found for %s" % sys.argv[2]
