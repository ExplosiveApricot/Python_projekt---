import random as r
from spelaren import * 



class monster:
    def __init__ (self,hp,atk,int):
        self.hp=hp
        self.atk=atk
        self.int=int

demon1 = monster(50,10,20)


def demon1_strid():
    i_strid = True
    print(f"""System: Du stöter på en mindre demon!!!!
          Den har {demon1.atk} attack, {demon1.hp} hälsa och {demon1.int} intelligens!!
          """)
    while demon1.hp>0 and klass.hp>0 and i_strid:
        stridval = input(print("""System: Vad vill du göra?
                            1. Attackera  (atk)
                            2. Fly (försök iallafall) (hp)
                            3. Utsmarta   (int)
                    Ditt val --> """))
        if stridval == "1":
            din_skada = r.randint(0,klass.atk)
            demon1_skada = r.randint(0,demon1.atk)
            if din_skada>demon1_skada:
                skada = din_skada-demon1_skada
                demon1.hp -= skada
                print(f"""System: Du slår hårt mot demonfan, den träffar!
                    Du gör {skada} skada, så demonfan har {demon1.hp} hälsa kvar!
                      """)
            elif din_skada==demon1_skada:
                print("System: Du missar, men det gör också demonen!")
            else:
                skada = demon1_skada-din_skada
                klass.hp -= skada
                print(f"""System: Ditt feta arsle missar demonfan och du tar {skada} skada!!!
                      Nu har du bara {klass.hp} hälsa kvar *emoji som biter på naglarna eller något*""")
        elif stridval == "2":
            print("Du försöker fly")