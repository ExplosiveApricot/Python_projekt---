from spelaren import *
from slowtypeshii import slowprint

def levelup():
    klass.lvl += 1

    if klassval == "2":
        klass.stk += 5
        klass.mhp += 25
        klass.base_atk += 5  # Öka base_atk istället för atk
        klass.hp = klass.mhp
        klass.int += 10
        slowprint(f"""
Du levlar upp! Du har nu statsen: {klass.atk} atk, {klass.mhp} hp, {klass.int} int och {klass.stk} stinknivå!""")
    elif klassval == "3":
        klass.mhp += 25
        klass.hp = klass.mhp
        klass.base_atk += 10  # Öka base_atk istället för atk
        klass.int += 10
        slowprint(f"""
Du levlar upp! Du har nu statsen: {klass.atk} atk, {klass.mhp} hp och {klass.int} int!""")
    else:
        klass.mhp += 25
        klass.hp = klass.mhp
        klass.base_atk += 10  # Öka base_atk istället för atk
        klass.int += 5
        slowprint(f"""
Du levlar upp! Dina stats är nu: {klass.atk} atk, {klass.mhp} hp och {klass.int} int!""")
