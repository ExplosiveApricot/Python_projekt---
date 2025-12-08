ryggsäck=[]
from slowtypeshii import slowprint

def öppna_säckfan():
    if len(ryggsäck)>0:
        # fix: iterera över listan direkt
        for item in ryggsäck:
            slowprint(item)
    else:
        slowprint("System: Det är tomt här...")
