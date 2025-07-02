def isDna(s: str) -> bool:
    lista = list(s)
    for elemento in lista:
        if elemento not in ["A" , "C" , "T" , "G"]:
            return False
    return True

    


def biologiaMolecolare(s1:str , s2:str) -> str:
    if isDna(s1) and isDna(s2):
        i = 0
        car = []
        for c in s2:
            if c == s1[i] and c + 1 == s2[i + 1]:
                car.append(c)
    return f"{len(car)} cifre"

if __name__ == "main":
    s1 = "GGTACCGTGA"
    s2 = "CGTGAACCTT"
    print(biologiaMolecolare(s1,s2))

            







       
if __name__ == "__main__" :
    s1= "AAB"
    s2= "AAB"





    print(biologiaMolecolare(s1,s2))
    