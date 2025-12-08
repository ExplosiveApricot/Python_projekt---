from spelaren import *
from slowtypeshii import slowprint

def levelup():
    # öka level först så tröskel-beräkningar stämmer om du vill använda dem senare
    klass.lvl += 1

    if klassval == "2":
        klass.stk += 5
        klass.mhp += 5
        # sätt aktuell hp till max (healar vid levelup)
        klass.hp = klass.mhp
        klass.int += 5
        slowprint(f"""
System: Du levlar upp! Du tjänar fem på varje stat, förutom attack för du är svag! Du stinker också mer...""")
    elif klassval == "3":
        klass.mhp += 5
        klass.hp = klass.mhp
        klass.atk += 5
        klass.int += 5
        slowprint(f"""
System: Du levlar upp! Du tjänar fem på varje stat!""")
    else:
        klass.mhp += 5
        klass.hp = klass.mhp
        klass.atk += 5
        slowprint(f"""
System: Du levlar upp! Du tjänar fem på varje stat, förutom intelligens för du är dum i huvudet!""")