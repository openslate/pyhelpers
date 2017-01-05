import sys
import os

rows, cols = os.popen('stty size', 'r').read().split()
cols = int(cols)


def progbar(t, c=None):
    """
    Draw progress bar of t/100 across screen width c
    """
    if c is None:
        n = t
        start = " %2d%% [" % (n * 100)
    else:
        n = float(c)/float(t)
        start = "(%d/%d) %2d%% [" % (c, t, n * 100)
    end = "]\r"
    blocks = (cols - (len(start) + len(end) - 1))
    mid = "=" * (int(blocks * n) - 1)
    sys.stdout.write(start + mid + ">" + " " * (blocks - (len(mid)+1)) + end)
    sys.stdout.flush()
