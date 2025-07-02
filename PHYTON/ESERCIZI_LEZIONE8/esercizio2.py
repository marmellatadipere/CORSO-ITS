def validate_password(password: str) -> bool:

    errori: list = [str]

#almeno 20 caratteri
    if len(password) < 20:
        errori.append("password troppo corta")

#almeno 3 maiuscole
    maiuscole = 0
    for carattere in password:
        if carattere.isupper():
            maiuscole += 1
        if maiuscole < 3:
            errori.append("meno di 3 maiuscole")

 #almeno 4 caratteri speciali
    speciali:int=0
    for c in password:
        if c.isalnum() == False:
            speciali +=1
    if speciali < 4:
        errori.append("Meno di 4 caratteri speciali")

    if errori:
        raise ValueError("Password non valida: " + ", ".join(errors))
    return True

# Test
try:
    print(validate_password("AB!@#defghijklmnopqrstuv"))
except ValueError as e:
    print(e)
