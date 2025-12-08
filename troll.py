import random as r
from spelaren import * 
from ryggsäck import *
from levelup import  *
from slowtypeshii import slowprint

monster_namn = ["Krull", "Skuggspore", "Bergknarr", "Grum", "Råttskalle", "Mossa", "Grovhen","Monkel Tronkel Jr.","Flåddus","Dregel","Slemmis","Tjockis","Bulten","Grötis","Klumpen","Fnykis","Blåfis","Snorkel","Dunsen","Knotten", "Don Qui Qui", "Fettimus Prime","Sir Stinkerlot","Lurifax","Tjocko McGee","Gnagis","Skrämsis","Bamsis","Trögtroll","Fetknopp","Dumle","Kladdis","Fluffis","Mullis","Tjocke-Tommy","Gröt-Fredrik","Snuskis","Bubblis","Klump-Filip","Dreggel-Doris","Slemmiga-Sara","Feta-Fredrik"]

class fiende:
    def __init__ (self,atk,mhp,hp,int,namn=None):
        self.mhp = mhp
        self.hp = hp
        self.atk = atk
        self.int = int
        self.namn = namn if namn else r.choice(monster_namn)



def troll_strid(a,mh,h,i):
    i_strid = True
    troll1 = fiende(a,mh,h,i)
    slowprint(f"""System: Du stöter på ett troll: {troll1.namn}!!!!
          Den har {troll1.atk} attack, {troll1.hp} hälsa och {troll1.int} intelligens!!
          """)
    while troll1.hp>0 and klass.hp>0 and i_strid:
        if klassval == "2":
            slowprint(f"{troll1.namn} är immun mot din stank")
        stridval = input("""System: Vad vill du göra?
                            1. Attackera  (atk)
                            2. Kolla säcken  
                            3. Utsmarta   (int)
                    Ditt val --> """)
        if stridval == "1":
            din_skada = r.randint(0,klass.atk)
            troll1_skada = r.randint(0,troll1.atk)
            if din_skada>troll1_skada:
                skada = din_skada-troll1_skada
                troll1.hp -= skada
                if troll1.hp <= 0:
                    slowprint(f"{troll1.namn} dör av din tuffa attack!")
                    if troll1.hp <= 0:
                        slowprint(f"""
System: {troll1.namn} dog och du får {troll1.mhp} exp! """)
                        klass.exp += troll1.mhp
                        threshold = int(100 * (1.1 ** klass.lvl))
                        while klass.exp >= threshold:
                            klass.exp -= threshold
                            levelup()
                            threshold = int(100 * (1.1 ** klass.lvl))
                            break
                slowprint(f"""System: Du slår hårt mot {troll1.namn}, den träffar!
                    Du gör {skada} skada, så {troll1.namn} har {troll1.hp} hälsa kvar!
                      """)
            elif din_skada==troll1_skada:
                slowprint("System: Du missar, men det gör också trollet!")
            else:
                skada = troll1_skada-din_skada
                klass.hp -= skada
                slowprint(f"""System: Ditt feta arsle missar {troll1.namn} och du tar {skada} skada!!!
                      Nu har du bara {klass.hp} hälsa kvar *emoji som biter på naglarna eller något*""")
        elif stridval == "2":
            öppna_säckfan()
        elif stridval == "3":
            din_skada = r.randint(0,klass.int)
            troll1_skada = r.randint(0,troll1.int)
            if din_skada>troll1_skada:
                skada = din_skada-troll1_skada
                troll1.hp-=skada
                if troll1.hp <= 0:
                    troll1.hp=0
                    slowprint(f"{troll1.namn} dör av din hjärnkraft!")
                elif skada >= 20:
                    slowprint(f"""System: Du får {troll1.namn} att slå sig själv med en sten med din skarpa tunga 
                          Du gör {skada} skada 
                          nu har {troll1.namn} {troll1.hp} hälsa kvar!""")
                elif skada>=10:
                    slowprint(f"""System: Du lägger krokben på {troll1.namn}!
                          Du gör {skada} skada!!
                          nu har {troll1.namn} {troll1.hp} hälsa kvar!""")
                else:
                    slowprint(f"""Du utsmartar {troll1.namn}!
                          Du gör {skada} skada!!
                          nu har {troll1.namn} {troll1.hp} hälsa kvar!""")
            elif din_skada==troll1_skada:
                slowprint("""Ni båda försöker utsmarta varandra men det händer absolut ingenting!!""")
            else:
                skada = troll1_skada-din_skada
                klass.hp-=skada
                slowprint(f"""System: {troll1.namn} utsmartar dig!
                Du tar {skada} skada
                Du har {klass.hp} hälsa kvar!""")
    if troll1.hp <= 0:
        slowprint(f"""
System: {troll1.namn} dog och du får {troll1.mhp} exp! """)
        klass.exp += troll1.mhp
        threshold = int(100 * (1.1 ** klass.lvl))
        while klass.exp >= threshold:
            klass.exp -= threshold
            levelup()
            threshold = int(100 * (1.1 ** klass.lvl))