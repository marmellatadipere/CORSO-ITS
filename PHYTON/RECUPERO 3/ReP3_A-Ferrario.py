import random
import re

class Creatura:
    def __init__(self, nome:str):
        self.setnome(nome)

    def setnome(self, nome:str):
        if isinstance(nome, str):
            self.nome = nome
        else:
            self.nome = "Creatura Generica"
    
    def getNome(self):
        return self.nome

    def __str__(self):
        return f"Creatura : {self.nome}"

class Alieno(Creatura):
    def __init__(self, nome:str, matricola:int, munizioni:list[int]):
        self.__setMatricola(matricola)
        self.__setMunizioni(munizioni)
        if re.match(r"^Robot-\d{5}$", nome):
            nomealieno = nome
        else:
            nomealieno = f"Robot-{self.matricola}"
        super().__init__(nomealieno)

    
    def __setMatricola(self):
        self.matricola = random.randint(10000,90000)
    def getMatricola(self):
        return self.matricola

    def __setMunizioni(self):
        self.munizioni:list[int] = [x**2 for x in range(15)]
    def getMunizioni(self):
        return self.munizioni
    
    def str(self):
        return f"Alieno: {self.getNome()}"

class Mostro(Creatura):
    def __init__(self, nome, urloVittoria:str, gemitoSconfitta:str, assalto:list[int]):
        self.setVittoria(urloVittoria)
        self.setSconfitta(gemitoSconfitta)
        self.setAssalto()
        super().__init__(nome)

    def setAssalto(self):
        x = random.randint(1,100)
        self.assalto:list[int] = [x for x in range(15) if x not in self.assalto]

    def getAssalto(self):
        return self.assalto

    #GET E SET VITTORIA
    def setVittoria(self, vittoria:str) : 
        if vittoria != "GRAAAHHH":
            self.vittoria = "GRAAAHHH"
        else:
            self.vittoria = vittoria
    def getVittoria(self):
        return self.vittoria


    #GET E SET SCONFITTA
    def setSconfitta(self, sconfitta:str) : 
        if sconfitta != "Uuurghhh":
            self.sconfitta = "Uuurghhh"
        else:
            self.sconfitta = sconfitta
    def getSconfitta(self):
        return self.sconfitta
    

    def __str__(self):
        nomeCaMel = ""
        for carattere in self.nome:
            if len(nomeCaMel) % 2 == 0:
                nomeCaMel += carattere.upper()
            else:
                nomeCaMel += carattere.lower()
        return f"Mostro: {nomeCaMel}"



def pariUguali(a: list[int], b: list[int]):
    c:list[int] = []
    while len(c) < min(len(a), len(b)):
        for i in range(min(len(a), len(b))):
            if a[i] % 2 == 0 and b[i] % 2 == 0:
                c.append(1)
            else:
                c.append(0)
        return c
        
def combattimento(a: Alieno, m: Mostro):
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Errore: uno dei due oggetti non è valido (Alieno o Mostro). Combattimento interrotto.")
        return None
    else:
        scontro = pariUguali(a.getMunizioni(), m.setAssalto())
        counter1 = scontro.count(1)
        if counter1 > 4:
            print(m.getVittoria())
            print(m.getVittoria())
            print(m.getVittoria())
        else:
            print(m.getSconfitta())
        

        

def proclamaVincitore(c: Creatura):
    if isinstance(c, Alieno):
        print("Winner : ALieno")
    if isinstance(c, Mostro):
        print("Winner: Mostro")
    print(10 * "*")
    print("*", " " * 8, "*")
    print(f"("*",{Creatura.getNome},"*")")
    print("*", " " * 8, "*")
    print(10 * "*")



if __name__ == "main":
    alieno1 = Alieno("massimo", 3333)
    mostro1 = Mostro("samuele")