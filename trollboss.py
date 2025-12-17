import random as r
from spelaren import *
from ryggsäck import *
from troll import *
from slowtypeshii import slowprint

def trollhättan_final_boss():
    slowprint("""
Stanken är outhärdlig när du kliver in i tronsalen.
Kungen sitter framför dig på en tron gjord av ben.
Han reser sig upp, skrattandes.
Du står framför den enda Monkel Tronkel den 3:e, Kungen över alla troll!""")
    input("Tryck enter för att fortsätta...")
    rensa()
    slowprint("""
Monkel Tronkel: Ha ha ha! Så du är den meslige människan som tog sig igenom alla mina soldater, jag måste säga att jag är imponerad.
                Men du kommer aldrig att besegra mig, för jag är inte som mina soldater, jag är en gud bland troll!
                Nu är det dags för ditt äventyr att ta slut!""")
    input("Tryck enter för att fortsätta...")
    rensa()
    fas_1()

def fas_1():
    # klass.exp += 1000 
    # kant = 100* (1.1)**klass.lvl
    # while klass.exp>kant:
    #     klass.exp-=kant
    #     levelup()
    #     kant = 100* (1.1)**klass.lvl
    slowprint("En strid bryter ut!")
    boss = fiende("Monkel Tronkel III")
    i=0
    slowprint("Monkel: Du kommer aldrig att lyckas!")
    salt = 3
    while boss.hp>0 and klass.hp>0 and i<=5:
        if klass.mhp-5<klass.hp:
            klass.hp = klass.hp - (klass.mhp-klass.hp)
            klass.mhp -= 5
        else:
            klass.mhp -= 5
        slowprint("""
Monkel stinker och du tappar 5 max hp!
Monkel verkar ladda upp en stark attack...
Vad vill du göra?
1. Attackera
2. Kolla ryggsäck
3. Ta skydd""")
        vval = input("--->")
        valt = False
        while not valt:
            if vval == "1":
                attack = r.randint(0,klass.atk)
                bförsvar =  boss.atk
                if attack > bförsvar:
                    skada = attack - bförsvar
                    if skada > boss.hp:
                        slowprint("Monkel faller ihop när du slår honom, är det över?")
                        boss.hp = 0
                    else:
                        boss.hp -= skada
                        slowprint(f"Du för {skada} skada på Monkel, han har nu {boss.hp} häsla kvar!")
                else:
                    slowprint("Din attack går inte igenom Monkels försvar...")
                valt = True
            elif vval == "2":
                öppna_säckfan()
                Valt = True
            elif vval == "3":
                if i<5:
                    slowprint("Du tar skydd, men Monkel gör inget än,han bara fortsätter ladda upp...")
                elif i==5 and salt>0:
                    slowprint(f"Du tar skydd och undviker Monkels superattack! Dock finns det bara {salt} skyddsalternativ kvar...")
                    salt-=1
                elif i==5 and salt==0:
                    slowprint("Du försöker skygga dig men tar Monkels fulla attack, och tar 100 skada!")
                valt= True
            else:
                slowprint("Välj ett alternativ tack...")
            
        i += 1
        if boss.hp<boss.mhp//2 and boss.special>0:
            boss.special -= 1
            slowprint("Monkeltar 50 hp från dig!")
            boss.hp += 50
            klass.hp -= 50
        if i==5 and vval != "3":
            slowprint("Monkel attackerar och du tar 100 skada!!!")
        else:
            slowprint(f"Monkel laddar upp mer energi, det serut som han kommer attackera om {5-i} turer...")
        

