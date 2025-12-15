from slowtypeshii import *
from spelaren import *
from ryggsäck import *
from troll import *
from rensa import *
from trollboss import *

def trollhättan():
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
    rensa()
    slowprint("""
Efter att ha gått nedför trappan öppnas äntligen vyn framför dig. Där du nu ser Trollhättan, trollens kungarike.
Långt borta ser du  en enorm byggnad, som förmodligen är där kungen finns. 
Det är dags.""")
    input("Tryck enter för att fortsätta...")
    slowprint("""
Du börjar din vandring, stanken blir starkare och starkare för varje steg du tar.""")

            
        
