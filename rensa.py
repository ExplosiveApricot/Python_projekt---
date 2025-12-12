import os

def rensa():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
