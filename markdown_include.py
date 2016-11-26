from subprocess import call
import time
import os
import re
import sys

def usage():
    return "python markdown_include.py <filename>"

def cat(filename):
    with open(filename, "r") as f:
        return f.read()

def main(filename):
    with open(filename, "r") as f:
        for line in f:
            m = re.match('^#include "([^"]*)"$', line)
            if m:
                include = m.group(1)
                (root, ext) = os.path.splitext(include)
                pdf = root + ".pdf"
                png = root + ".png"

                print "```tex\n{}```".format(cat(include))
                call(["latexmk", "-pdf", "-quiet", "-interaction=nonstopmode", include])
                call(["convert", "-density", "150", pdf, "-quality", "90", png])
                print "![{}]({})".format(include, png)
            else:
                print line,

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print usage()
        sys.exit(-1)
    main(sys.argv[1])
