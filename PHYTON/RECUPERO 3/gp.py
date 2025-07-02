import random
import re

class Creatura:
    def __init__(self, nome: str):
        self.setNome(nome)

    def setNome(self, nome: str):
        if isinstance(nome, str) and nome.strip():
            self.nome = nome
        else:
            self.nome = "Creatura Generica"

    def getNome(self):
        return self.nome

    def __str__(self):
        return f"Creatura: {self.nome}"


class Alieno(Creatura):
    def __init__(self, nome: str):
        self.__setMatricola()
        self.__setMunizioni()
        # Controllo sul nome
        if re.match(r"^Robot-\d{5}$", nome):
            nome_finale = nome
        else:
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            nome_finale = f"Robot-{self.matricola}"
        super().__init__(nome_finale)

    def __setMatricola(self):
        self.matricola = random.randint(10000, 90000)

    def getMatricola(self):
        return self.matricola

    def __setMunizioni(self):
        self.munizioni = [x**2 for x in range(15)]

    def getMunizioni(self):
        return self.munizioni

    def __str__(self):
        return f"Alieno: {self.getNome()}"


class Mostro(Creatura):
    def __init__(self, nome: str, urloVittoria: str, gemitoSconfitta: str):
        self.setVittoria(urloVittoria)
        self.setSconfitta(gemitoSconfitta)
        self.setAssalto()
        super().__init__(nome)

    def setAssalto(self):
        # genera lista casuale con 15 valori unici
        self.assalto = random.sample(range(1, 100), 15)

    def getAssalto(self):
        return self.assalto

    # SET & GET Vittoria
    def setVittoria(self, vittoria: str):
        if vittoria != "GRAAAHHH":
            self.vittoria = "GRAAAHHH"
        else:
            self.vittoria = vittoria

    def getVittoria(self):
        return self.vittoria

    # SET & GET Sconfitta
    def setSconfitta(self, sconfitta: str):
        if sconfitta != "Uuurghhh":
            self.sconfitta = "Uuurghhh"
        else:
            self.sconfitta = sconfitta

    def getSconfitta(self):
        return self.sconfitta

    def __str__(self):
        nomeCamel = ""
        for i, carattere in enumerate(self.getNome()):
            if i % 2 == 0:
                nomeCamel += carattere.lower()
            else:
                nomeCamel += carattere.upper()
        return f"Mostro: {nomeCamel}"