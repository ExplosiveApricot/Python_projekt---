from slowtypeshii import slowprint

class spelaren():
    def __init__(self, atk, mhp, hp, int, stk, lvl, exp):
        self.base_atk = atk 
        self.mhp = mhp
        self.hp = hp
        self.int = int
        self.lvl = lvl
        self.exp = exp
        self.stk = stk

    @property
    def atk(self):
        if klassval == "3": 
            return self.base_atk + self.stk
        elif klassval == "1": 
            return self.base_atk + ((self.mhp - self.hp)-(self.mhp-self.hp)%3)//3
        else: 
            return self.base_atk

klas = False

while not klas:
    slowprint("""
                     
1. Bygg

2. Teknik

3. Samhäll

""")
    klassval = input("Ditt val---> ")

    if klassval == "1":
        klass = spelaren(20,100,100,0,0,0,0)
        slowprint(f"Random Dansk: Du går bygg och har därmed statsen: {klass.atk} atk, {klass.mhp} hp och {klass.int} int. Din skada ökar också med förlorat hp!")
        klas = True

    elif klassval == "2":
        klass = spelaren(0,100,100,20,5,0,0)
        slowprint(f"Random Dansk: Det var alltså du som lukta, du har statsen: {klass.atk} atk, {klass.mhp} hp och {klass.int} int, du  har också {klass.stk} stinknivå.")
        klas = True

    elif klassval == "3":
        klass = spelaren(10,100,100,10,0,0,0)
        slowprint(f"Random Dansk: Du går nu sam med statsen: {klass.atk} atk, {klass.mhp} hp och {klass.int} int. Se till att samla aura!")
        klas = True

    else:
        slowprint("Välj ett av alternativen tack :)")
    
bryggdnedräkning = 0
boknedräkning = 0





