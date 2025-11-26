import random as r
from spelaren import *
from ryggsäck import *
from troll import *

def trollhättan_final_boss():
    Monkel = fiende(50,500,20000)
    print("""
System: Du känner stank från alla vinklar, men den börjar bli starkare varje steg du tar, tills en gigantisk figur dyker upp i din synvinkel
        Framför dig står den fetaste varelsen du någonsin sett, kungen av Trollhättan, Monkel Tronkel den 3:e.
Monkel: Vilken svag människa står framför mig?""")
    namn =  input("System: Kanske är dags att säga ditt namn --->")
    print(f"""
Monkel: {namn} alltså. 
System: han ställer sig upp, marken vibrerar
Monkel: Dags att dö människa""")
    i_strid = True
    while i_strid and Monkel.hp>0 and klass.hp>0:
        print(f"Stanken borrar in sig i dina näsborrar, du tappar 5 hp")
        klass.hp-=5