import random as r
from spelaren import *
from ryggsäck import *
from troll import *
from slowtypeshii import slowprint

def trollhättan_final_boss():
    i=0
    Monkel = fiende(50,500,500,20000,"Monkel Tronkel III")
    slowprint("""
System: Du känner stank från alla vinklar, men den börjar bli starkare varje steg du tar, tills en gigantisk figur dyker upp i din synvinkel
        Framför dig står den fetaste varelsen du någonsin sett, kungen av Trollhättan, Monkel Tronkel den 3:e.
Monkel: Vilken svag människa står framför mig?""")
    namn =  input("System: Kanske är dags att säga ditt namn --->")
    slowprint(f"""
Monkel: {namn} alltså. 
System: han ställer sig upp, marken vibrerar
Monkel: Dags att dö människa
System: En strid bryter ut! Monkel har {Monkel.atk} skada, {Monkel.hp} hälsa och {Monkel.int} intelligens!""")
    while Monkel.hp>0 and klass.hp>0:
        i+=1
        if klassval == "2":
            slowprint("System: Du stinker! Men Monkel tar ingen skada av det...")
            slowprint("     Men du är också immun mot hans stank!")
        else:
            slowprint("Stanken borrar in sig i dina näsborrar, du tappar 1 max hp")
        if klass.hp == klass.mhp:
            klass.mhp-=1
            klass.hp-=1
        else:
            klass.mhp-=1

        slowprint("""
System: Du känner din drivkraft stärker dina attacker. Allt hänger på detta, vad vill du göra? 
1. Attackera
2. Inventory
3. Utsmarta """)
        viktigt_val = input("---> ")

        if viktigt_val=="1":
            viktig_skada = r.randint(0,klass.atk)
            monkel_skada = r.randint(0,Monkel.atk)
            if viktig_skada>=monkel_skada:
                skada = viktig_skada+10-monkel_skada
                if skada>=Monkel.hp:
                    Monkel.hp=0
                else:    
                    Monkel.hp -= skada
                slowprint(f"""
System: Din attack träffar Monkel och han tar {skada} skada!!
        han har nu {Monkel.hp} hp kvar!""")

            else:
                skada = monkel_skada-viktig_skada
                klass.hp -=skada
                slowprint(f""" 
System:Du på något sätt missar den fetaste varelsen någonsin och tar {skada} skada.
Bara {klass.hp} hp kvar!
""")
        elif viktigt_val == "2":
            öppna_säckfan()
            if "Konstigt mynt" in ryggsäck:
                Monkel.hp=0
                slowprint(""" 
System: När du öppnar din ryggsäck händer något konstigt. 
        Myntet, som du fick av Nikodemus, börjar glöda till, och Monkel faller ihop på plats""")
        elif viktigt_val == "3":
            slowprint("""
System: Är du helt dum???? 
        Han har 20 000 intelligens! 
        Det är ju bara självmord och jämföra dina stats med hans!!!""")
    if Monkel.hp ==0:
        slowprint("""
System: Striden pågår i vad som känns i en evighet, men tillslut  faller Monkel ihop. 
        Du har vunnit!
        Eller?""")
        klass.mhp += i
        klass.hp = klass.mhp



def fas_två():
    svagpunkt = False
    slowprint("""
Monkel: Trodde du verkligen att du hade besegrat mig?!?! 
        Du är bara en mesig människa, du kommer aldrig lyckas!!!!!""")
    Monkel2 = fiende(100000000000000,100000000000000,100000000000000,100000000000000)
    slowprint(f"""
System: Du stöter på Monkel en andra gång! 
        Han har statsen {Monkel2.hp} häsla, {Monkel2.atk} attack och {Monkel2.int} intelligens...
        """)
    while not svagpunkt and klass.hp>0:
        slowprint("System: Monkel stinker ännu mer nu, du tappar 20 max hp!")
        if klass.hp+20>klass.mhp:
            klass.hp -= klass.mhp-klass.hp
            klass.mhp -= 20
        slowprint("""
System: Vad vill du göra? 
1. Attackera 
2. Öppna ryggsäck 
3. Utsmarta 
4. Leta efter svagheter """)
        vval2 = input("----> ")
        if vval2 == "1":
            slowprint("""
System: Det  där är nog inte en bra idé...""")
        elif vval2 == "2":
            öppna_säckfan()
            slowprint("System: Det verkar inte finnas något av användning...")
        elif vval2 == "3":
            slowprint("""
System: Det  där är nog inte en bra idé...""")
        elif vval2 == "4":
            slowprint(""" 
System: Vad ska vi göra? Att slåss är ur bilden
    1.Kolla fötter
    2.Kolla mage 
    3.Kolla armar 
    4.Kolla hals
    5.Kolla ansikte""")
            inspaning = input("---> ")
            if inspaning == "1":
                slowprint("""
System: Din fotfetish får dig att kolla på hans stinkande fötter. Inget speciellt kommer till tanke""")
            elif inspaning == "2":
                slowprint("""
System: Det enda du ser är otroligt mycket fläsk""")
            elif inspaning == "3":
                slowprint("""
System: Du ser inget viktigt""")
            elif inspaning == "4":
                slowprint(""" 
System: Det ser ut som han har en kristall runt ett smycke! Det är säkert viktigt! Ta det!
        När du tar tag i smycket kommer ett otroligt ljus upp, och Monkel minskar i storlek, nu lika stor som du
Monkel: Nej!!! Vad har du gjort!!! Du tog min rätt till tronen!!!
System: Denna kristall ger dig alltså  makten att regera över trollhättan, vill du sätta på den? y/n""")
                regera_eller_ej = input("---> ")
                if regera_eller_ej == "y" or regera_eller_ej == "Y":
                    slowprint("System: Du tar på dig kristallen, men kraften är för mycket för att hantera. Du dör på fläcken.")
                    klass.hp = 0
                else:
                    slowprint("System: Du krossar kristallen och därmed Monkels hopp om tronen. Du räddade Åva från trollhotet! Grattis!")
                    svagpunkt = True

trollhättan_final_boss()
fas_två() 