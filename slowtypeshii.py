import time
import sys

def slowprint(*args, sep=' ', end='\n', delay=0.04):
    """långsam utskrift av text till konsolen"""
    text = sep.join(str(a) for a in args)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()