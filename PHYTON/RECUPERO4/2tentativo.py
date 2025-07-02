def isDna(s: str) -> bool:
    lista = list(s)
    for elemento in lista:
        if elemento not in ["A" , "C" , "T" , "G"]:
            return False
    return True

    


def biologiaMolecolare(s1:str , s2:str) -> str:
    if isDna(s1) and isDna(s2):
        lista1 = list(reversed(s1))
        lista2 = list(s2)
        nuovalista = []
        counterLunghezza = 0

        for i in range(min(len(lista1), len(lista2))):              
            if lista2[i] != lista1[i]:
                pass
            else:
                carattereSovrapposto = lista2[i]
                nuovalista.append(carattereSovrapposto)
                counterLunghezza += 1
            i += 1
                
    return f"La sequenza massima è {counterLunghezza}\nI caratteri {nuovalista} si sovrappongono"


if __name__ == "__main__" :
    s1= "AAGCTTACG"
    s2= "ACGTTCGA"





    print(biologiaMolecolare(s1,s2))
    