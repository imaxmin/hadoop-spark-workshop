#!/usr/bin/env python

import sys

# TODO:
# read the words in the provided pattern file into a set.

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # emit intermediate key-value pair
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1

        # TODO: only emit the words in the pattern set.
        print '%s\t%s' % (word, 1)
