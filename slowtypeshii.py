import time
import sys

def slowprint(text, end='\n', delay=0.02):
    """långsam utskrift av text till konsolen"""
    text = str(text)
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print(end, end='')
