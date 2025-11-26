import random as r
from spelaren import * 
from ryggsäck import *


class monster:
    def __init__ (self,atk,hp,int):
        self.hp=hp
        self.atk=atk
        self.int=int




def troll_strid(a,h,i):
    i_strid = True
    troll1 = monster(a,h,i)
    print(f"""System: Du stöter på ett troll!!!!
          Den har {troll1.atk} attack, {troll1.hp} hälsa och {troll1.int} intelligens!!
          """)
    while troll1.hp>0 and klass.hp>0 and i_strid:
        stridval = input(print(f"""System: Vad vill du göra?
                            1. Attackera  (atk)
                            2. Kolla säcken  
                            3. Utsmarta   (int)
                    Ditt val --> """))
        if stridval == "1":
            din_skada = r.randint(0,klass.atk)
            troll1_skada = r.randint(0,troll1.atk)
            if din_skada>troll1_skada:
                skada = din_skada-troll1_skada
                troll1.hp -= skada
                if skada>=troll1.hp:
                    print("Trollet dör av din  tuffa attack!")
                    break
                else:
                    continue
                print(f"""System: Du slår hårt mot demonfan, den träffar!
                    Du gör {skada} skada, så demonfan har {troll1.hp} hälsa kvar!
                      """)
            elif din_skada==troll1_skada:
                print("System: Du missar, men det gör också demonen!")
            else:
                skada = troll1_skada-din_skada
                klass.hp -= skada
                print(f"""System: Ditt feta arsle missar demonfan och du tar {skada} skada!!!
                      Nu har du bara {klass.hp} hälsa kvar *emoji som biter på naglarna eller något*""")
        elif stridval == "2":
            öppna_säckfan()
        elif stridval == "3":
            din_skada = r.randint(0,klass.int)
            troll1_skada = r.randint(0,troll1.int)
            if din_skada>troll1_skada:
                skada = din_skada-troll1_skada
                troll1.hp-=skada
                if skada>=troll1.hp:
                    troll1.hp=0
                    print("Trollet dör av din hjärnkraft!")
                elif skada >= 20:
                    print(f"""System: Du får trollet att slå sig själv med en sten med din skarpa tunga 
                          Du gör {skada} skada 
                          nu har trollet {troll1.hp} hälsa kvar!""")
                elif skada>=10:
                    print(f"""System: Du läggerkrokben på trollet!
                          Du gör {skada} skada!!
                          nu har trollet {troll1.hp} hälsa kvar!""")
                else:
                    print(f"""Du utsmartar trollet!
                          Du gör {skada} skada!!
                          nu har trollet {troll1.hp} hälsa kvar!""")
            elif din_skada==troll1_skada:
                print("""Ni båda försöker utsmarta varandra men det händer absolut ingenting!!""")
            else:
                skada = troll1_skada-din_skada
                klass.hp-=skada
                (f"""System: Trollet utsmartar dig!
                Du tar {skada}skada
                Du har {klass.hp} hälsa kvar!""")


troll_strid(1,1,1)