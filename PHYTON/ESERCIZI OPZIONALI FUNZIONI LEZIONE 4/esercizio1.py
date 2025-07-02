def grade_student(nome:str, voti:float):
    media = sum(voti) / len(voti)
    if media >= 60:
        print(f"{nome} con una media di {media} ha superato l'esame")
    else:
        print(f"{nome} bocciato")

studenti = [
    ("Adriano", [85, 78, 92]),
    ("Daniele", [58, 64, 47]),
    ("Claudia", [90, 88, 95]),
    ("Leandro", [45, 50, 55])
]

for nome, voti in studenti:
    grade_student(nome,voti)
