class spelaren():
    def __init__(self,atk,mhp,hp,int,stk,lvl,exp):
        self.atk = atk
        self.mhp = mhp
        self.hp = hp
        self.int = int
        self.lvl = lvl
        self.exp = exp
        self.stk = stk
klas = False

while not klas:
    klassval = input("""
                     
                        1. Bygg

                        2. Teknik

                        3. Samhäll
    Ditt val---> """)

    if klassval == "1":
        klass = spelaren(21,21,21,0,0,1,0)
        print(f"Random Dansk: Du går bygg och har därmed statsen: {klass.atk} atk, {klass.mhp} hp och {klass.int} int")
        klas = True

    elif klassval == "2":
        klass = spelaren(5,16,16,21,5,1,0)
        print(f"Random Dansk: Det var alltså du som lukta, du har statsen: {klass.atk} atk, {klass.mhp} hp och {klass.int} int, du  har också {klass.stk} stinknivå.")
        klas = True

    elif klassval == "3":
        klass = spelaren(14,14,14,14,0,1,0)
        print(f"Random Dansk: Du går nu sam med statsen: {klass.atk} atk, {klass.mhp} hp och {klass.int} int")
        klas = True

    else:
        print("System: Välj ett av alternativen tack :)")





