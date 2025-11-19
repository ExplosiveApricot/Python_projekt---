class spelaren():
    def __init__(self,atk,hp,int):
        self.atk = atk
        self.hp = hp
        self.int = int

klas = False

while not klas:
    klassval = input("""
                        System: Vilken inriktning går du?
                     
                        1. Bygg: 21 atk, 21 hp, 0 int  

                        2. Teknik: 5 atk, 16 hp, 21 int 

                        3. Samhäll: 14 atk, 14 hp, 14 int
    Ditt val---> """)

    if klassval == "1":
        klass = spelaren(21,21,0)
        print(f"Random Dansk: Du går bygg och har därmed statsen: {klass.atk} atk, {klass.hp} hp och {klass.int} int")
        klas = True

    elif klassval == "2":
        klass = spelaren(5,16,21)
        print(f"Random Dansk: Det var alltså du som lukta, du har statsen: {klass.atk} atk, {klass.hp} hp och {klass.int} int")
        klas = True

    elif klassval == "3":
        klass = spelaren(14,14,14)
        print(f"Random Dansk: Du går nu sam med statsen: {klass.atk} atk, {klass.hp} hp och {klass.int} int")
        klas = True

    else:
        print("System: Välj ett av alternativen tack :)")





