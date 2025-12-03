from spelaren import *
def levelup():
    if klassval == "2":
        klass.stk += 5
        klass.mhp += 5
        klass.hp += 5
        klass.int += 5
        klass.lvl += 1
        print(f"""
System: Du levlar upp! Du tjänar fem på varje stat, förutom attack för du är svag! Du stinker också mer...""")
    elif klassval == "3":
        klass.mhp += 5
        klass.hp += 5
        klass.atk += 5
        klass.int += 5
        klass.lvl += 1
        print(f"""
System: Du levlar upp! Du tjänar fem på varje stat!""")
    else:
        klass.mhp += 5
        klass.hp += 5
        klass.atk += 5
        klass.lvl += 1
        print(f"""
System: Du levlar upp! Du tjänar fem på varje stat, förutom intelligens för du är dum i huvudet!""")