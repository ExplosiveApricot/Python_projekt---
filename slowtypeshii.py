import time
import sys

def slowprint(text, end='\n', delay=0):
    """långsam utskrift av text till konsolen"""
    text = str(text)
    for ch in text:
        print(ch, end ='')
        time.sleep(delay)
    print(end, end='')
