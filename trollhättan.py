from slowtypeshii import *
from spelaren import *
from ryggsäck import *
from troll import *
from rensa import *
from trollboss import *
from levelup import *

def trollhättan():
    while klass.levande == True:
        slowprint("""
    Efter att ha tagit dig ner från den mörka våning 0 på Åva, hittar du en trappa.
    Uppför trappan lyser ett svagt grönt ljus, och det stinker något fruktansvärt
    Om du går ner verkar det som att du inte kommer kunna återvända utan att du gör klart ditt uppdrag...""")
        ned_val = input("Är du redo att gå nedför trappan? j för ja")
        if ned_val == "j":
            rensa()
            slowprint("Du tar ett djupt andetag och går nedför trappan...")
        else:
            slowprint("""Har du mycket av ett val dock???
    Om du inte vill använda någon item såklart.""")
            innan_ned  = input("Vill du använda en item? j för ja")
            if innan_ned == "j":
                öppna_säckfan()
                slowprint("Efter en snabb koll i din ryggsäck bestämmer du dig för att gå ned...")
            else:
                slowprint("Du går nedför trappan...")
        input("Tryck enter för att fortsätta...")
        rensa()
        slowprint("""
    Efter att ha gått nedför trappan öppnas äntligen vyn framför dig. Där du nu ser Trollhättan, trollens kungarike.
    Långt borta ser du  en enorm byggnad, som förmodligen är där kungen finns. Synen ger dig 50 exp!""")
        klass.exp += 50
        kant = 100* (1.1)**klass.lvl
        while klass.exp>kant:
            klass.exp-=kant
            levelup()
            kant = 100* (1.1)**klass.lvl
        slowprint("""Det är dags.""")
        input("Tryck enter för att fortsätta...")
        rensa()
        slowprint("""
    Du börjar din vandring, stanken blir starkare och starkare för varje steg du tar.""")
        input("Tryck enter för att fortsätta...")
        rensa()
        slowprint("""
    Men helt plötsligt, känner du ett andetag på din nacke...
    Det är Gruk, förstöraren!""")
        input("Tryck enter för att fortsätta...")
        rensa()
        singelstrid("Gruk, förstöraren")
        if not klass.levande:
            break
        slowprint("""
    Efter en hårdkamp står du nu segrare över Gruk, 
    men det kommer säkert dra till sig en hel del uppmärksamhet.
    Du måste skynda dig till kungens slott innan allt är för sent!""")
        input("Tryck enter för att fortsätta...")
        rensa()
        slowprint("""
    Du kommer allt närmare slottet, men utanför portarna står det tre troll! 
    Du måste in så en strid är oundviklig...""")
        input("Tryck enter för att fortsätta...")
        rensa()
        flerastrid("Trollvakt","Trollvakt","Trollvakt")
        if not klass.levande:
            break
        slowprint("""När du besegrade fienderna ser du att porten är låst""")
        input("Tryck enter för att fortsätta...")
        slowprint("""Någon i hög rang borde ha en nyckel, en general kanske?
    Du kollar runtomkring och ser en stor byggnad som nära intill slottet. 
    Utanför står det en skylt där det står med stora bokstäver:TROLLENS FÖRSVARSMAKT
    Här finns det säkert en general! Synen ger dig 50 exp!""")
        klass.exp += 50
        kant = 100* (1.1)**klass.lvl
        while klass.exp>kant:
            klass.exp-=kant
            levelup()
            kant = 100* (1.1)**klass.lvl
        input("Tryck enter för att fortsätta...")
        rensa()
        slowprint("""
    Du smyger långsamt in i byggnaden, och du ser tre fiender framför dig.
    Två ser ut som vakterna du mötte tidigare, och en ser starkare ut...
    Det är nog generalen!
    Dags för strid igen...""")
        input("tryck enter för att fortsätta...")
        rensa()
        slowprint("""
    Generalen: Va! Vem är du?! Vakter, till attack!""")
        flerastrid("Trollsoldat","Trollgeneral","Trollsoldat")
        if not klass.levande:
            break
        slowprint("""
    Du lyckades besegra trollen, och ser en nyckel ligga bredvid den fallna generalen.
    Du tar nyckeln och skyndar dig tillbaka till slottet.""")
        input("Tryck enter för att fortsätta...")
        slowprint("""När du väl öppnar porten med nyckeln känner du ännu mera stank...
    Framför dig ser du tillslut dörren till kungens tronrum. 
    Men framför dörren står två enorma vakter, 
    och en liten figur som är Gregg dem listige, kungens rådgivare""")
        input("Tryck enter för att fortsätta...")
        rensa()
        flerastrid("Trollvakt","Gregg den listige","Trollvakt")
        if not klass.levande:
            break
        slowprint("""
    Du lyckades besegra vakterna och Gregg, och skyndar in i tronsalen där kungen väntar...""")
        input("Tryck enter för att fortsätta...")
        rensa()
        trollhättan_final_boss()

    

klass.exp += 10000
kant = 100* (1.1)**klass.lvl
while klass.exp>kant:
    klass.exp-=kant
    levelup()
    kant = 100* (1.1)**klass.lvl
fas_2_strid()