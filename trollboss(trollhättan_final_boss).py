import random as r
from spelaren import *
from ryggsäck import *
from troll import *

def trollhättan_final_boss():
    Monkel = fiende(50,500,500,20000)
    print("""
System: Du känner stank från alla vinklar, men den börjar bli starkare varje steg du tar, tills en gigantisk figur dyker upp i din synvinkel
        Framför dig står den fetaste varelsen du någonsin sett, kungen av Trollhättan, Monkel Tronkel den 3:e.
Monkel: Vilken svag människa står framför mig?""")
    namn =  input("System: Kanske är dags att säga ditt namn --->")
    print(f"""
Monkel: {namn} alltså. 
System: han ställer sig upp, marken vibrerar
Monkel: Dags att dö människa
System: En strid bryter ut! Monkel har {Monkel.atk} skada, {Monkel.hp} hälsa och {Monkel.int} intelligens!""")
    while Monkel.hp>0 and klass.hp>0:
        print(f"Stanken borrar in sig i dina näsborrar, du tappar 1 max hp")
        if klass.hp == klass.mhp:
            klass.mhp-=1
            klass.hp-=1
        else:
            klass.mhp-=1
        viktigt_val = input(print("""
System: Du känner din drivkraft stärker dina attacker. Allt hänger på detta, vad vill du göra? 
1. Attackera
2. Inventory
3. Utsmarta 
--->"""))

        if viktigt_val=="1":
            viktig_skada = r.randint(0,klass.atk)
            monkel_skada = r.randint(0,Monkel.atk)
            if viktig_skada>=monkel_skada:
                skada = viktig_skada+10-monkel_skada
                if skada>=Monkel.hp:
                    Monkel.hp=0
                else:    
                    Monkel.hp -= skada
                print(f"""
System: Din attack träffar Monkel och han tar {skada} skada!!
        han har nu {Monkel.hp} hp kvar!""")

            else:
                skada = monkel_skada-viktig_skada
                klass.hp -=skada
                print(f""" 
System:Du på något sätt missar den fetaste varelsen någonsin och tar {skada} skada.
Bara {klass.hp} hp kvar!
""")
        elif viktigt_val == "2":
            öppna_säckfan
            if "Konstigt mynt" in ryggsäck:
                Monkel.hp=0
                print(""" 
System: När du öppnar din ryggsäck händer något konstigt. 
        Myntet, som du fick av Nikodemus, börjar glöda till, och Monkel faller ihop på plats""")
        elif viktigt_val == "3":
            print("""
System: Är du helt dum????
        Han har 20 000 intelligens! 
        Det är ju bara självmord och jämföra dina stats med hans!!!""")
    if Monkel.hp ==0:
        print("""
System: Striden pågår i vad som känns i en evighet, men tillslut  faller Monkel ihop. 
        Du har vunnit!
        Eller?""")


def fas_två():
    print("""
Monkel: Trodde du verkligen att du hade besegrat mig?!?!
        Du är bara en mesig människa, du kommer aldrig lyckas!!!!!""")
    Monkel2 = fiende(100000000000000,100000000000000,100000000000000,100000000000000)
    print(f"""
System: Du stöter på Monkel en andra gång! 
        Han har statsen {Monkel2.hp} häsla, {Monkel2.atk} attack och {Monkel2.int} intelligens...
        """)
    while Monkel2.hp>0:
        vval2 = input("System: Vad vill du göra?" \
        "1. Attackera" \
        "2. Öppna ryggsäck" \
        "3. Utsmarta" \
        "4. Leta efter svagheter" \
        "---->")
        