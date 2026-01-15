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
    fas_2()


boss = fiende("Monkel Tronkel III")
slutboss = fiende("Monkel Tronkel, gud över trollhättan")



def fas_1():
    slowprint("En strid bryter ut!")
    i=0
    slowprint("Monkel: Du kommer aldrig att lyckas!")
    salt = 3
    while boss.hp>0 and klass.hp>0:
        klass.hp-=5
        i+=1
        input("Tryck enter för att fortsätta...")
        rensa()
        slowprint(f"""
Monkel stinker och du tappar 5 hp!
Nu har du {klass.hp}/{klass.mhp} hälsa kvar!
Monkel verkar ladda upp en stark attack...
Vad vill du göra?
1. Attackera
2. Kolla ryggsäck
3. Ta skydd""")
        vval = input("--->")
        if vval == "1":
            attack = r.randint(0,klass.atk)
            bförsvar =  boss.atk
            if attack > bförsvar:
                skada = attack - bförsvar
                if skada > boss.hp:
                    slowprint("Monkel faller ihop när du slår honom, är det över?")
                    boss.hp = 0
                    break
                else:
                    boss.hp -= skada
                    slowprint(f"Du för {skada} skada på Monkel, han har nu {boss.hp} häsla kvar!")
            else:
                slowprint("Din attack går inte igenom Monkels försvar...")
        elif vval == "2":
            öppna_säckfan()
            if "Deoderant" in ryggsäck:
                slowprint("Monkel tappar hälften av sin häsla av deon!")
                slutboss.hp = 0.5*slutboss.hp
            if "Styrkebryggd" in ryggsäck and klass.bryggdnedräkning == 0:
                slowprint("Din styrkebryggd ökar din attack!")
                klass.atk += 5
            if  "Mattebok" in ryggsäck and klass.boknedräkning == 0:
                slowprint("Din mattebok ökar din intelligens!")
                klass.int += 5
            if "Guldäpple" in ryggsäck:
                slowprint("Guldäpplet läker 50 hp!")
                klass.hp += 50
            if "livselixir" in ryggsäck and klass.hp < klass.mhp-25:
                slowprint("Livselixiret läker 25 hp!")
                klass.hp += 25
            else:
                slowprint("Du har inget av användning!")
        elif vval == "3":
            if i%5>0:
                slowprint("Du tar skydd, men Monkel gör inget än,han bara fortsätter ladda upp...")
            elif i%5==0 and salt>0:
                salt -= 1
                slowprint(f"Du tar skydd och undviker Monkels superattack! Dock finns det bara {salt} skyddsalternativ kvar...")
            elif i%5==0 and salt==0:                    
                slowprint("Du försöker skygga dig men tar Monkels fulla attack, och tar 100 skada!")
                
        else:
            slowprint("Eftersom du inte valde ett alternativ går du till anfall...")
            vval = "1"
            
        
        if boss.hp<boss.mhp//2 and boss.special>0:
            boss.special -= 1
            slowprint("Monkel använder sin special och tar 50 hp från dig!")
            boss.hp += 50
            klass.hp -= 50
        if i%5==0 and vval != "3":
            slowprint("Monkel attackerar och du tar 100 skada!!!")
            klass.hp -= 100
        else:
            slowprint(f"Monkel laddar upp mer energi, det serut som han kommer attackera om {5-i%5} turer...")
    if klass.hp <=0:
        slowprint("""
Du har tagit otroligt mycket skada och känner att dina knän kommer att vika ihop.

Monkel: Ha ha ha! Trodde du verkligen att du hade en chans! Tack för underhållningen iallafall, ha ha ha!

Du kan inte låta Åva gå under! Res dig, kämpa!!!""")
        input("Tryck enter för att fortsätta...")
        slowprint("""
...

                  
                  
...
                  

Din styrka börjar återvända. Du kan inte låta Monkel vinna!
Din vilja ger dig 1000 exp!""")
        klass.exp += 1000 
        kant = 100* (1.1)**klass.lvl
        while klass.exp>kant:
            klass.exp-=kant
            levelup()
            kant = 100* (1.1)**klass.lvl
        slowprint("""
Monkel: Va?! Vad händer nu? Är du ute efter stryk. Ha ha! Dags för runda två!""")
        input("Tryck enter för att fortsätta...")
        rensa()
    elif boss.hp == 0:
        slowprint("""
Monkel: Okej, jag får medge att du är en värdig motståndare, men jag har inte visat mitt allt än.
                  
Du tjänar 1000 exp för att du vann första rundan!""")
        klass.exp += 1000 
        kant = 100* (1.1)**klass.lvl
        while klass.exp>kant:
            klass.exp-=kant
            levelup()
            kant = 100* (1.1)**klass.lvl
def fas_2():
    slowprint("""
Monkel växer ännu mer, och något runt hans hals lyser till...

Monkel: Dags att visa min sanna styrka!""")
    input("Tryck enter för att fortsätta...")
    rensa()
    i = 0
    p = 0
    slowprint(f"""
En sista strid bryter ut...          
Monkel har {slutboss.atk} atk, {slutboss.mhp} häsla och {slutboss.int} intelligens!
""")
    while i < 2:
        slowprint("""Vad vill du göra? Allt hänger på detta!
1. Attackera
2. Öppna ryggsäck
3. Ta skydd""")
        vval = input("--->")
        if vval == "1" and p == 0:
            slowprint("Ett grönt  ljus dyker upp och blockar din attack!")
            i += 1
            p += 1
        elif vval == "1" and p == 1:
            slowprint("Du testar igen, men samma gröna ljus dyker upp.")
            i += 1
        elif vval == "2":
            öppna_säckfan()
            slowprint("Det kommer inte hjälpa just nu...")
        elif vval == "3":
            slowprint("Monkel står bara där, skrattandes.")
        
    slowprint("Det verkar inte som blint attackerande inte kommer att göra något...")
    input("Tryck enter för att fortsätta...")
    rensa()
    slowprint("""
Du måste hitta ett sätt att komma igenom Monkels försvar...
Men hur?

                         
...
              
              
...
            
              
Efter att ha funderat en stund kommer du på en idé!
""")
    input("Tryck enter för att fortsätta...")
    rensa()
    slowprint("""
Monkel stank är fruktansvärd, den har nog en förmåga att blocka attacker.
Du måste använda dig av något som kan motverka stanken, som en deoderant!

""")              
    input("Tryck enter för att fortsätta...")
    rensa()
    if "Deoderant" in ryggsäck:
        slowprint("Du använder din deoderant på Monkel!")
        slowprint("Monkels försvar går sönder!")
        fas_2_strid()
    else:
        slowprint("""
Spelaren: Grishpojkar!!!! Ge mig en deoderant!

En deo kommer flygande från himlen och träffar Monkel rakt i ansiktet!""")
    fas_2_strid()

def fas_2_strid():
    slowprint("Monkel: Imponerande, du hittade min svaghet, men det kommr bara förlänga tiden till ditt öde!!!")
    input("Tryck enter för att fortsätta...")
    rensa()
    vval2 = ""
    slowprint("""Dags för den slutgiltiga striden!""")
    while slutboss.hp>0 and klass.hp>0:
        specialtid = 0
        if specialtid == 1:
            slowprint("Monkel använder sin special och snor 50 hp från dig!")
        if slutboss.hp<slutboss.mhp//2 and slutboss.special>0:
            specialtid = 1
            if vval2 == "3":
                slowprint("Men du blockar den!")
                slutboss.special -= 1
                specialtid = 0
            else:
                klass.hp -= 50
                slutboss.hp += 50
                slutboss.special -= 1
        mskada = r.randint(0,slutboss.atk)
        dförsvar = r.randint(0,klass.atk)
        if mskada > dförsvar:
            if vval2 == "3":
                slowprint("Du blockar Monkels attack!")
            skada = mskada - dförsvar
            klass.hp -= skada
            slowprint(f"Du tar {skada} skada av Monkel, du har nu {klass.hp}/{klass.mhp} kvar!")
        elif dförsvar > mskada:
            slowprint("Du blockar Monkels attack!")
        if klassval == "2":
            slowprint(f"Monkel tar {klass.stk} skada av din stank, och du tar 10 skada av hans")
            slutboss.hp -= klass.stk
            klass.hp -= 10
        else:
            slowprint("Du tar 10 skada av Monkels stank!")
            klass.hp -= 10
        slowprint("""
Vad vill du göra?
1. Attackera
2. Öppna ryggsäck
3. Skydda dig""")
        vval2 = input("--->")
        if vval2 == "1":
            skada = r.randint(0,klass.atk)
            slutboss.hp -= skada
            if slutboss.hp < 0:
                slowprint("Monkel faller ihop när du slår honom, är det över?")
                slutboss.hp = 0
                break
            else:
                slowprint(f"Du gör {skada} skada på Monkel! Han har nu {slutboss.hp} hp kvar!")
        elif vval2 == "2":
            öppna_säckfan()
            if "Deoderant" in ryggsäck:
                slowprint("Monkel tappar hälften av sin häsla av deon!")
                slutboss.hp = 0.5*slutboss.hp
            if "Styrkebryggd" in ryggsäck and klass.bryggdnedräkning == 0:
                slowprint("Din styrkebryggd ökar din attack!")
                klass.atk += 5
            if  "Mattebok" in ryggsäck and klass.boknedräkning == 0:
                slowprint("Din mattebok ökar din intelligens!")
                klass.int += 5
            if "Guldäpple" in ryggsäck:
                slowprint("Guldäpplet läker 50 hp!")
                klass.hp += 50
            if "livselixir" in ryggsäck and klass.hp < klass.mhp-25:
                slowprint("Livselixiret läker 25 hp!")
                klass.hp += 25
            else:
                slowprint("Du har inget av användning!")
        elif vval2 == "3":
            slowprint("Du skyddar inkommande attack!")

    if slutboss.hp <=0:
        slowprint("""
Monkel: Nej.. Detta får inte hända! Jag är en gud! Hur kan du, en simpel människa, besegra mig!!!

Monkel tros falla till marken, men någonting händer med honom...

Monkel: Juvel av trollhättan! Ge mig din kraft! Hjälp mig erövra Åva!!!

En stråle av ljus kommer från en juvel runt Monkels hals och det omsluter honom helt. 
Men kristallen spricker av all den kraft och  monkels hals exploderar tillsammans med kristallen.
Hans livlösa kropp faller till marken. Du har besegrat Monkel Tronkel den III och räddade Åva! Gratulerar!
""")
    elif klass.hp <=0:
        slowprint("Du dog... Åva kommer nu att gå under av trollens framfart...")
        klass.levande = False