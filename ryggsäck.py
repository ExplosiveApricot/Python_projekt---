ryggsäck=[]
from slowtypeshii import slowprint

def öppna_säckfan():
    if len(ryggsäck)>0:
        for item in ryggsäck:
            slowprint(item)
    else:
        slowprint("Det är tomt här...")
