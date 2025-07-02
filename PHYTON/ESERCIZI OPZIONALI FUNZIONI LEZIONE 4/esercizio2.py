import random

def indovina():
    print("Hai 5 tentativi per indovinare un numero da 1 a 50")
    numero = random.randint(1,51)
    numero_tentativi: int = int(input("quanti tentativi ti servono?"))
    while numero_tentativi > 0:
        risposta:int = int(input(f"prova a indovinare,{numero_tentativi} tentativi rimasti!"))
        if risposta == numero:
            print("hai vinto")
            break
        elif risposta > numero:
            print("troppo alto")
        else:
            print("troppo basso")
    else: 
        print(" hai perso ")




indovina()
