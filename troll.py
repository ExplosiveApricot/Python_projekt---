import random as r
from spelaren import * 
from ryggsäck import *
from levelup import  *
from slowtypeshii import slowprint
from rensa import rensa

monster_namn = ["Gruk, förstöraren","Grubb", "Gnorp", "Greg", "Zarg", "Snorre","Grippy", "Knorp" ]
class fiende:
    def __init__ (self,namn = None):
        self.namn = namn if namn else r.choice(monster_namn)
        if namn == "Monkel Tronkel Jr":
            self.atk = 5
            self.mhp = 30
            self.hp = 30
            self.int = 5
            self.special = 0
            self.exp = 25
        elif namn == "Blorg den korte":
            self.atk = 5
            self.mhp = 50
            self.hp = 50
            self.int = 10
            self.special = 0
            self.exp = 40
        elif namn == "Gorg den fete":
            self.atk = 1
            self.mhp = 150
            self.hp = 150
            self.int = 15
            self.special = 0
            self.exp = 75
        elif namn == "Zull den mäktige":
            self.atk = 70
            self.mhp = 100
            self.hp = 100
            self.int = 10
            self.special = 0
            self.exp = 150
        elif namn == "Throg den smarte":
            self.atk = 10
            self.mhp = 100
            self.hp = 100
            self.int = 70
            self.special = 0
            self.exp = 150
        elif namn == "Gruk, förstöraren":
            self.atk = 75
            self.mhp = 350
            self.hp = 350
            self.int = 70
            self.special = 1
            self.exp = 300
        elif namn == "Trollvakt":
            self.atk = 100
            self.mhp = 100
            self.hp = 100
            self.int = 100
            self.special = 0
            self.exp = 100
        elif namn == "Trollgeneral":
            self.atk = 150
            self.mhp = 200
            self.hp = 200
            self.int = 150
            self.special = 1
            self.exp = 200
        elif namn == "Kungens väktare":
            self.atk = 200
            self.mhp = 300
            self.hp = 300
            self.int = 200
            self.special = 1
            self.exp = 500
        elif namn == "Gregg den listige":
            self.atk = 50
            self.mhp = 400
            self.hp = 400
            self.int = 200
            self.special = 1
            self.exp = 750
        elif namn == "Monkel Tronkel III":
            self.atk = 150
            self.mhp = 500
            self.hp = 500
            self.int = 2000
            self.special = 2
        elif namn == "Monkel Tronkel, gud över trollhättan":
            self.atk = 200
            self.mhp = 750
            self.hp = 750
            self.int = 2000
            self.special = 3
            self.superspecial = 1
        else:
            self.atk = r.randint(1,20)
            self.mhp = r.randint(20,200)
            self.hp = self.mhp
            self.int = r.randint(5,50)
            self.special = 0
            self.exp = self.atk//3 + self.mhp//3 + self.int//3
def flerastrid(a,b,c):
    i_strid = True
    flychans = [0,1,2,3,4,5]
    antal_troll = 3
    slowprint(f"Du möter {antal_troll} stycket troll!")
    troll_nr1 = fiende(a)
    troll_nr2 = fiende(b)
    troll_nr3 = fiende(c)
    slowprint(f"""Du möter följande troll:
1. {troll_nr1.namn}
2. {troll_nr2.namn}
3. {troll_nr3.namn}""")
    while antal_troll>0 and klass.hp>0 and i_strid:
        slowprint(f"Du har {klass.hp} hp kvar!")
        if  klass.hp <= 10:
            slowprint("Din hälsa är låg, vill du fly?")
            slowprint("Skriv j för ja, n för nej ---> ")
            flykt = input()
            if flykt == "j":
                flychans = [0,1,2,3,4,5]
                if r.choice(flychans) == 0 or r.choice(flychans) == 1 or r.choice(flychans) == 2:
                    slowprint("Du lyckas fly från striden!")
                    i_strid = False
                    if klassval == "3":
                        slowprint("Du förlorar all din aura för att du flyr!")
                        klass.stk = 0
                    break
                else:
                    slowprint("Du misslyckas med att fly!")
                
            else:
                slowprint("Du väljer att stanna och slåss!")
        if klassval == "2":
            slowprint(f"Trollen tar {klass.stk} skada av din stank!")
            if troll_nr1.hp>0:
                troll_nr1.hp -= klass.stk
            if troll_nr2.hp>0:
                troll_nr2.hp -= klass.stk
            if troll_nr3.hp>0:    
                troll_nr3.hp -= klass.stk
            if troll_nr1.hp <= 0:
                slowprint(f"Du har dödat {troll_nr1.namn} med din stank!")
                antal_troll -= 1
            elif troll_nr2.hp <= 0:
                slowprint(f"Du har dödat {troll_nr2.namn} med din stank!")
                antal_troll -= 1
            elif troll_nr3.hp <= 0:
                slowprint(f"Du har dödat {troll_nr3.namn} med din stank!")
                antal_troll -= 1
        slowprint(f"Vilket troll vill du slåss mot?")
        for i in range (1,4):
            if i ==1 and troll_nr1.hp>0:
                slowprint(f"{i}. {troll_nr1.namn} (hp: {troll_nr1.hp})")
            elif i==2 and troll_nr2.hp>0:
                slowprint(f"{i}. {troll_nr2.namn} (hp: {troll_nr2.hp})")
            elif i==3 and troll_nr3.hp>0:
                slowprint(f"{i}. {troll_nr3.namn} (hp: {troll_nr3.hp})")
        slowprint("a. Attackera alla troll")
        slowprint("Öppna ryggsäcken med s")
        val = input("---> ")
        if val == "1" and troll_nr1.hp>0:
            slowprint(f"""Använder du attackera eller utsmarta {troll_nr1.namn}? 
Trollet har statsen atk: {troll_nr1.atk}, int: {troll_nr1.int}. a för attackera, u för utsmarta---> """)
            aval = input()
            if aval == "a":
                din_skada = r.randint(0,klass.atk)
                troll1_försvar = r.randint(0,troll_nr1.atk)
                if din_skada>troll1_försvar:
                    skada = din_skada - troll1_försvar
                    troll_nr1.hp -= skada
                    if troll_nr1.hp <= 0:
                        slowprint(f"Du har dödat {troll_nr1.namn}!")
                        antal_troll -= 1
                        continue
                    slowprint(f"""Du träffar {troll_nr1.namn} och gör {skada} skada!""")
                else:
                    slowprint("Du missar din attack!")
            elif aval == "u":
                din_skada = r.randint(0,klass.int)
                troll1_försvar = r.randint(0,troll_nr1.int)
                if din_skada>troll1_försvar:
                    skada = din_skada - troll1_försvar
                    troll_nr1.hp -= skada
                    if troll_nr1.hp <= 0:
                        slowprint(f"Du har dödat {troll_nr1.namn}!")
                        antal_troll -= 1
                        continue
                    slowprint(f"""Du utsmartar {troll_nr1.namn} och gör {skada} skada!""")
                else:
                    slowprint("Du misslyckas med att utsmarta trollet!")
        elif val == "2" and troll_nr2.hp>0:
            slowprint(f"""Använder du attackera eller utsmarta {troll_nr2.namn}?
Trollet har statsen atk: {troll_nr2.atk}, int: {troll_nr2.int}. a för attackera, u för utsmarta---> """)
            aval = input()
            if aval == "a":
                din_skada = r.randint(0,klass.atk)
                troll2_försvar = r.randint(0,troll_nr2.atk)
                if din_skada>troll2_försvar:
                    skada = din_skada - troll2_försvar
                    troll_nr2.hp -= skada
                    if troll_nr2.hp <= 0:
                        slowprint(f"Du har dödat {troll_nr2.namn}!")
                        antal_troll -= 1
                        continue
                    slowprint(f"""Du träffar {troll_nr2.namn} och gör {skada} skada!""")
                else:
                    slowprint("Du missar din attack!")
            elif aval == "u":
                din_skada = r.randint(0,klass.int)
                troll2_försvar = r.randint(0,troll_nr2.int)
                if din_skada>troll2_försvar:
                    skada = din_skada - troll2_försvar
                    troll_nr2.hp -= skada
                    if troll_nr2.hp <= 0:
                        slowprint(f"Du har dödat {troll_nr2.namn}!")
                        antal_troll -= 1
                        continue
                    slowprint(f"""Du utsmartar {troll_nr2.namn} och gör {skada} skada!""")
                else:
                    slowprint("Du misslyckas med att utsmarta trollet!")
        elif val == "3" and troll_nr3.hp>0:
            slowprint(f"""Använder du attackera eller utsmarta {troll_nr3.namn}?
Trollet har statsen atk: {troll_nr3.atk}, int: {troll_nr3.int}. a för attackera, u för utsmarta---> """)
            aval = input()
            if aval == "a":
                din_skada = r.randint(0,klass.atk)
                troll3_försvar = r.randint(0,troll_nr3.atk)
                if din_skada>troll3_försvar:
                    skada = din_skada - troll3_försvar
                    troll_nr3.hp -= skada
                    if troll_nr3.hp <= 0:
                        slowprint(f"Du har dödat {troll_nr3.namn}!")
                        antal_troll -= 1
                        continue
                    slowprint(f"""Du träffar {troll_nr3.namn} och gör {skada} skada!""")
                else:
                    slowprint("Du missar din attack!")
            elif aval == "u":
                din_skada = r.randint(0,klass.int)
                troll3_försvar = r.randint(0,troll_nr3.int)
                if din_skada>troll3_försvar:
                    skada = din_skada - troll3_försvar
                    troll_nr3.hp -= skada
                    if troll_nr3.hp <= 0:
                        slowprint(f"Du har dödat {troll_nr3.namn}!")
                        antal_troll -= 1
                        continue
                    slowprint(f"""Du utsmartar {troll_nr3.namn} och gör {skada} skada!""")
                else:
                    slowprint("Du misslyckas med att utsmarta trollet!")
        elif val == "a":
            slowprint("Använder du attackera eller utsmarta alla troll? a för attackera, u för utsmarta---> ")
            fval = input()
            if fval == "a":
                din_skada = r.randint(0,klass.atk)
                troll_försvar = 0
                if troll_nr1.hp>0:
                    troll_försvar += r.randint(0,troll_nr1.atk)
                if troll_nr2.hp>0:
                    troll_försvar += r.randint(0,troll_nr2.atk)
                if troll_nr3.hp>0:
                    troll_försvar += r.randint(0,troll_nr3.atk)
                if din_skada>troll_försvar:
                    skada = din_skada - troll_försvar
                    if troll_nr1.hp>0:
                        troll_nr1.hp -= skada
                        if troll_nr1.hp <= 0:
                            slowprint(f"Du har dödat {troll_nr1.namn}!")
                            antal_troll -= 1
                        else:
                            slowprint(f"Du gör {skada} skada på {troll_nr1.namn}!")
                    if troll_nr2.hp>0:
                        troll_nr2.hp -= skada
                        if troll_nr2.hp <= 0:
                            slowprint(f"Du har dödat {troll_nr2.namn}!")
                            antal_troll -= 1
                        else:
                            slowprint(f"Du gör {skada} skada på {troll_nr2.namn}!")
                    if troll_nr3.hp>0:
                        troll_nr3.hp -= skada
                        if troll_nr3.hp <= 0:
                            slowprint(f"Du har dödat {troll_nr3.namn}!")
                            antal_troll -= 1
                        else:
                            slowprint(f"Du gör {skada} skada på {troll_nr3.namn}!")
                else:
                    slowprint("Du missar din attack!")
            elif fval == "u":
                din_skada = r.randint(0,klass.int)
                troll_försvar = 0
                if troll_nr1.hp>0:
                    troll_försvar += r.randint(0,troll_nr1.int)
                if troll_nr2.hp>0:
                    troll_försvar += r.randint(0,troll_nr2.int)
                if troll_nr3.hp>0:
                    troll_försvar += r.randint(0,troll_nr3.int)
                if din_skada>troll_försvar:
                    skada = din_skada - troll_försvar
                    if troll_nr1.hp>0:
                        troll_nr1.hp -= skada
                        if troll_nr1.hp <= 0:
                            slowprint(f"Du har dödat {troll_nr1.namn}!")
                            antal_troll -= 1
                        else:
                            slowprint(f"Du gör {skada} skada på {troll_nr1.namn}!")
                    if troll_nr2.hp>0:
                        troll_nr2.hp -= skada
                        if troll_nr2.hp <= 0:
                            slowprint(f"Du har dödat {troll_nr2.namn}!")
                            antal_troll -= 1
                        else:
                            slowprint(f"Du gör {skada} skada på {troll_nr2.namn}!")
                    if troll_nr3.hp>0:
                        troll_nr3.hp -= skada
                        if troll_nr3.hp <= 0:
                            slowprint(f"Du har dödat {troll_nr3.namn}!")
                            antal_troll -= 1
                        else:
                            slowprint(f"Du gör {skada} skada på {troll_nr3.namn}!")
        elif val == "s":
            öppna_säckfan()
            if "Styrkebryggd" in ryggsäck:
                slowprint("Vill du använda styrkebryggden för en tillfällig styrkeökning på 5?")
                bryggdval = input("Tryck j för ja--->")
                if bryggdval == "j":
                    bryggdnedräkning = 3
                    klass.atk += 5
                    slowprint("Din attack har ökat med 5!")
                    ryggsäck.remove("Styrkebryggd")
                else:
                    slowprint("Du lägger tillbaka styrkebryggden i ryggsäcken.")
            if "Mattebok" in ryggsäck:
                slowprint("Vill du använda matteboken för en tillfällig intelligensökning på 5?")
                bokval = input("Tryck j för ja--->")
                bokval = bokval.lower()
                if bokval == "j":
                    boknedräkning = 3
                    klass.int  += 5
                    slowprint("Din intelligens har ökat med 5!")
                    ryggsäck.remove("Mattebok")
            if "Guldäpple" in ryggsäck:
                slowprint("Vill du äta ett guldäpple?")
                äppleval = input("Tryck j för ja--->")
                äppleval = äppleval.lower()
                if äppleval == "j":
                    klass.hp += 50
                    slowprint("Din hp har ökat med 50! HP:t från guldäpplet övergår MHP!")
                    ryggsäck.remove("Guldäpple")
            if "Livselixir" in ryggsäck and klass.hp <=klass.mhp-25:
                slowprint("Vill du använda ett livselixir för att återställa 25 hp?")
                elixirval = input("Tryck j för ja--->")
                elixirval = elixirval.lower()
                if elixirval == "j":
                    klass.hp += 25
                    slowprint("Du återställer 25 hp!")
        else:
            slowprint("Välj ett giltigt alternativ!")
        trolltur = True
        while trolltur:
            Troll_attack = r.randint(1,3)
            if troll_nr1.hp>0:
                försvar = r.randint(0,klass.atk)
                troll1_atk = r.randint(0,troll_nr1.atk)
                troll1_int = r.randint(0,troll_nr1.int)
                if troll_nr1.special > 0 and troll_nr1.hp < (troll_nr1.mhp//2):
                    slowprint(f"{troll_nr1.namn} använder sin special och tar 50 hp från dig!")
                    klass.hp -= 50
                    troll_nr1.special -= 1
                    troll_nr1.hp += 50
                if troll1_atk>troll1_int:
                    if troll1_atk>försvar:
                        skada = troll1_atk - försvar
                        klass.hp -= skada
                        slowprint(f"{troll_nr1.namn} attackerar dig och gör {skada} skada!")
                    else:
                        slowprint(f"{troll_nr1.namn} missar sin attack!")
                else:
                    if troll1_int>försvar:
                        skada = troll1_int - försvar
                        klass.hp -= skada
                        slowprint(f"{troll_nr1.namn} utsmartar dig och gör {skada} skada!")
            if troll_nr2.hp>0:
                försvar = r.randint(0,klass.atk)
                troll2_atk = r.randint(0,troll_nr2.atk)
                troll2_int = r.randint(0,troll_nr2.int)
                if troll_nr2.special > 0 and troll_nr2.hp < (troll_nr2.mhp//2):
                    slowprint(f"{troll_nr2.namn} använder sin special och tar 50 hp från dig!")
                    klass.hp -= 50
                    troll_nr2.special -= 1
                    troll_nr2.hp += 50
                if troll2_atk>troll2_int:
                    if troll2_atk>försvar:
                        skada = troll2_atk - försvar
                        klass.hp -= skada
                        slowprint(f"{troll_nr2.namn} attackerar dig och gör {skada} skada!")
                    else:
                        slowprint(f"{troll_nr2.namn} missar sin attack!")
                else:
                    if troll2_int>försvar:
                        skada = troll2_int - försvar
                        klass.hp -= skada
                        slowprint(f"{troll_nr2.namn} utsmartar dig och gör {skada} skada!")
            if troll_nr3.hp>0:
                försvar = r.randint(0,klass.atk)
                troll3_atk = r.randint(0,troll_nr3.atk)
                troll3_int = r.randint(0,troll_nr3.int)
                if troll_nr3.special > 0 and troll_nr3.hp < (troll_nr3.mhp//2):
                    slowprint(f"{troll_nr3.namn} använder sin special och tar 50 hp från dig!")
                    klass.hp -= 50
                    troll_nr3.special -= 1
                    troll_nr3.hp += 50
                if troll3_atk>troll3_int:
                    if troll3_atk>försvar:
                        skada = troll3_atk - försvar
                        klass.hp -= skada
                        slowprint(f"{troll_nr3.namn} attackerar dig och gör {skada} skada!")
                    else:
                        slowprint(f"{troll_nr3.namn} missar sin attack!")
                else:
                    if troll3_int>försvar:
                        skada = troll3_int - försvar
                        klass.hp -= skada
                        slowprint(f"{troll_nr3.namn} utsmartar dig och gör {skada} skada!")
            trolltur = False
        input("Tryck enter för att  fortsätta...")
        rensa()
    if antal_troll == 0:
        slowprint(f"Du vann striden! Du tjänar {troll_nr1.exp + troll_nr2.exp + troll_nr3.exp} exp! Och kanske ett föremål...")
        if klass.bryggdnedräkning > 0:
            klass.bryggdnedräkning -= 1
            if klass.bryggdnedräkning <= 0:
                klass.atk -= 5
                slowprint("Effekten av styrkebryggden har försvunnit och din attack minskar med 5.")
        if klass.boknedräkning > 0:
            klass.boknedräkning -= 1
            if klass.boknedräkning <= 0:
                klass.int -= 5
                slowprint("Effekten av matteboken har försvunnit och din intelligens minskar med 5.")
        föremål_chans = r.randint(1,8)
        if föremål_chans == 1:
            slowprint("Trollet hade ett livselixir och du plockar upp det!")
            ryggsäck.append("Livselixir")
        elif föremål_chans == 2:
            slowprint("Trollet hade en styrkebryggd och du plockar upp den!")
            ryggsäck.append("Styrkebryggd")
            slowprint("Vill du använda styrkebryggden för en tillfällig styrkeökning på 5?")
            bryggdval = input("Tryck j för ja--->")
            if bryggdval == "j":
                klass.bryggdnedräkning = 3
                klass.atk += 5
                slowprint("Din attack har ökat med 5!")
                ryggsäck.remove("Styrkebryggd")
            else:
                slowprint("Du lägger tillbaka styrkebryggden i ryggsäcken.")
        elif föremål_chans == 3:
            slowprint("Trollet hade en mattebok och  du plockar upp den!")
            ryggsäck.append("Mattebok")
            slowprint("Vill du använda matteboken för en tillfällig intelligensökning på 5?")
            bokval = input("Tryck j för ja--->")
            if bokval == "j":
                klass.boknedräkning = 3
                klass.int += 5
                slowprint("Din intelligens har ökat med 5!")
                ryggsäck.remove("Mattebok")
            else:
                slowprint("Du lägger tillbaka matteboken i ryggsäcken.")
        elif föremål_chans == 4:
            slowprint("Trollet hade ett guldäpple och du plockar upp det!")
            ryggsäck.append("Guldäpple")
            slowprint("Vill du använda guldäpplet för en tillfällig hp-ökning på 50?")
            guldäppleval = input("Tryck j för ja--->")
            if guldäppleval == "j":
                klass.hp += 50
                slowprint("Din hp har ökat med 50! HP:t från guldäpplet övergår MHP!")
                ryggsäck.remove("Guldäpple")
            else:
                slowprint("Du lägger tillbaka guldäpplet i ryggsäcken.")
        klass.exp += troll_nr1.exp + troll_nr2.exp + troll_nr3.exp
        threshold = int(100 * (1.1 ** klass.lvl))
        while klass.exp >= threshold:
            klass.exp -= threshold
            levelup()
            threshold = int(100 * (1.1 ** klass.lvl))
        if  klassval == "3":
            slowprint("Du vann striden, så du tjänar 15 aura,eftersom det var en 3v1!")
            klass.stk += 15
        rensa()
        levande = True
        return levande
    elif klass.hp<=0:
        slowprint("Du dog... Åva kommer nu gå under av trollens framafart...")
        levande = False
        return levande
def singelstrid(a):
    i_strid = True
    troll1 = fiende(a)
    slowprint(f"""Du stöter på ett troll: {troll1.namn}!!!!
          Den har {troll1.atk} attack, {troll1.hp} hälsa och {troll1.int} intelligens!!
          """)
    print(f"Din attack är {klass.atk}")
    while troll1.hp>0 and klass.hp>0 and i_strid:
        slowprint(f"Du har {klass.hp} hp kvar!")
        if  klass.hp <= 10:
            slowprint("Din hälsa är låg, vill du fly?")
            slowprint("Skriv j för ja, n för nej ---> ")
            flykt = input()
            if flykt == "j":
                slowprint("Du flyr från striden!")
                if klassval == "3":
                    slowprint("Du förlorar all din aura för att du flyr!")
                    klass.stk = 0
                i_strid = False
                break
            else:
                slowprint("Du väljer att stanna och slåss!")
        if klassval == "2":
            slowprint(f"{troll1.namn} tar {klass.stk} skada av din stank!")
            troll1.hp -= klass.stk
            if troll1.hp <= 0:
                slowprint(f"{troll1.namn} dör av din stank!")
                break
        slowprint("""Vad vill du göra?
1. Attackera  (atk)
2. Kolla säcken
3. Utsmarta   (int)""")
        stridval = input("Ditt val --> ")
        if stridval == "1":
            din_skada = r.randint(0,klass.atk)
            troll1_försvar = r.randint(0,troll1.atk)
            if din_skada>troll1_försvar:
                skada = din_skada - troll1_försvar
                troll1.hp -= skada
                if troll1.hp <= 0:
                    slowprint(f"{troll1.namn} dör av din tuffa attack!")
                    break
                slowprint(f"Du slår hårt mot {troll1.namn}, den träffar!")
                slowprint(f"Du gör {skada} skada, så {troll1.namn} har {troll1.hp} hälsa kvar!")
            else:
                slowprint("Du missar din attack!")
        elif stridval == "2":
            öppna_säckfan()
            if "Styrkebryggd" in ryggsäck:
                slowprint("Vill du använda styrkebryggden för en tillfällig styrkeökning på 5?")
                bryggdval = input("Tryck j för ja--->")
                if bryggdval == "j":
                    bryggdnedräkning = 3
                    klass.atk += 5
                    slowprint("Din attack har ökat med 5!")
                    ryggsäck.remove("Styrkebryggd")
                else:
                    slowprint("Du lägger tillbaka styrkebryggden i ryggsäcken.")
            if "Mattebok" in ryggsäck:
                slowprint("Vill du använda matteboken för en tillfällig intelligensökning på 5?")
                bokval = input("Tryck j för ja--->")
                bokval = bokval.lower()
                if bokval == "j":
                    boknedräkning = 3
                    klass.int  += 5
                    slowprint("Din intelligens har ökat med 5!")
                    ryggsäck.remove("Mattebok")
            if "Guldäpple" in ryggsäck:
                slowprint("Vill du äta ett guldäpple?")
                äppleval = input("Tryck j för ja--->")
                äppleval = äppleval.lower()
                if äppleval == "j":
                    klass.hp += 50
                    slowprint("Din hp har ökat med 50! HP:t från guldäpplet övergår MHP!")
                    ryggsäck.remove("Guldäpple")
            if "Livselixir" in ryggsäck and klass.hp <=klass.mhp-25:
                slowprint("Vill du använda ett livselixir för att återställa 25 hp?")
                elixirval = input("Tryck j för ja--->")
                elixirval = elixirval.lower()
                if elixirval == "j":
                    klass.hp += 25
                    slowprint("Du återställer 25 hp!")
        elif stridval == "3":
            din_skada = r.randint(0,klass.int)
            troll1_försvar = r.randint(0,troll1.int)
            if din_skada>troll1_försvar:
                skada = din_skada - troll1_försvar
                troll1.hp -= skada
                if troll1.hp <= 0:
                    slowprint(f"{troll1.namn} dör av din hjärnkraft!")
                    break
                slowprint(f"Du utsmartar {troll1.namn} och gör {skada} skada!")
                slowprint(f"nu har {troll1.namn} {troll1.hp} hälsa kvar!")
            else:
                slowprint("Du misslyckas med att utsmarta trollet!")
        if troll1.atk>troll1.int:
            if troll1.namn == troll1.special >0 and troll1.hp < (troll1.mhp//2):
                slowprint(f"{troll1.namn} använder sin special och tar 50 hp från dig!")
                klass.hp -= 50
                troll1.special -= 1
                troll1.hp += 50
            försvar = r.randint(0,klass.atk)
            troll1_atk = r.randint(0,troll1.atk)
            if troll1_atk>försvar:
                skada = troll1_atk - försvar
                klass.hp -= skada
                slowprint(f"{troll1.namn} attackerar dig och gör {skada} skada!")
            else:
                slowprint(f"{troll1.namn} missar sin attack!")
        else:
            if troll1.special >0 and troll1.hp < (troll1.mhp//2):
                slowprint(f"{troll1.namn} använder sin special och tar 50 hp från dig!")
                klass.hp -= 50
                troll1.special -= 1
                troll1.hp += 50
            försvar = r.randint(0,klass.int)
            troll1_int = r.randint(0,troll1.int)
            if troll1_int>försvar:
                skada = troll1_int - försvar
                klass.hp -= skada
                slowprint(f"{troll1.namn} utsmartar dig och gör {skada} skada!")
            else:
                slowprint(f"{troll1.namn} misslyckas med att utsmarta dig!")
        input("Tryck enter för att fortsätta...")
        rensa()

    if troll1.hp <= 0:
        slowprint(f"Du vann striden! Du tjänar {troll1.exp} exp! Och kanske ett föremål...")
        if klass.bryggdnedräkning > 0:
            klass.bryggdnedräkning -= 1
            if klass.bryggdnedräkning <= 0:
                klass.atk -= 5
                slowprint("Effekten av styrkebryggden har försvunnit och din attack minskar med 5.")
        if klass.boknedräkning > 0:
            klass.boknedräkning -= 1
            if klass.boknedräkning <= 0:
                klass.int -= 5
                slowprint("Effekten av matteboken har försvunnit och din intelligens minskar med 5.")
        föremål_chans = r.randint(1,8)
        if föremål_chans == 1:
            slowprint("Trollet hade ett livselixir och du plockar upp det!")
            ryggsäck.append("Livselixir")
        elif föremål_chans == 2:
            slowprint("Trollet hade en styrkebryggd och du plockar upp den!")
            ryggsäck.append("Styrkebryggd")
            slowprint("Vill du använda styrkebryggden för en tillfällig styrkeökning på 5?")
            bryggdval = input("Tryck j för ja--->")
            if bryggdval == "j":
                klass.bryggdnedräkning = 3
                klass.atk += 5
                slowprint("Din attack har ökat med 5!")
                ryggsäck.remove("Styrkebryggd")
            else:
                slowprint("Du lägger tillbaka styrkebryggden i ryggsäcken.")
        elif föremål_chans == 3:
            slowprint("Trollet hade en mattebok och  du plockar upp den!")
            ryggsäck.append("Mattebok")
            slowprint("Vill du använda matteboken för en tillfällig intelligensökning på 5?")
            bokval = input("Tryck j för ja--->")
            if bokval == "j":
                klass.boknedräkning = 3
                klass.int += 5
                slowprint("Din intelligens har ökat med 5!")
                ryggsäck.remove("Mattebok")
            else:
                slowprint("Du lägger tillbaka matteboken i ryggsäcken.")
        elif föremål_chans == 4:
            slowprint("Trollet hade ett guldäpple och du plockar upp det!")
            ryggsäck.append("Guldäpple")
            slowprint("Vill du använda guldäpplet för en tillfällig hp-ökning på 50?")
            guldäppleval = input("Tryck j för ja--->")
            if guldäppleval == "j":
                klass.hp += 50
                slowprint("Din hp har ökat med 50! HP:t från guldäpplet övergår MHP!")
                ryggsäck.remove("Guldäpple")
            else:
                slowprint("Du lägger tillbaka guldäpplet i ryggsäcken.")
        slowprint(f"{troll1.namn} dog och du får {troll1.exp} exp! ")
        klass.exp += troll1.exp
        threshold = int(100 * (1.1 ** klass.lvl))
        while klass.exp >= threshold:
            klass.exp -= threshold
            levelup()
            threshold = int(100 * (1.1 ** klass.lvl))
            rensa()
        levande = True
        return levande
    elif klass.hp<=0:
        slowprint("Du dog... Åva kommer nu gå under av trollens framafart...")
        levande = False
        return levande
    if klassval == "3" and troll1.hp <= 0:
        slowprint("Du vann striden, så du tjänar 5 aura!")
        klass.stk += 5
        rensa()
