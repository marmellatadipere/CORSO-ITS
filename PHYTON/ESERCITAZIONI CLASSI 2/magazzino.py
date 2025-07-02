class Prodotto:
    def __init__(self, nome: str, quantita: int):
        self.nome = nome
        self.quantita = quantita

    def __str__(self):
        return f"{self.nome}: {self.quantita} disponibili"

class Magazzino:
    def __init__(self):
        self.prodotti = {}

    def aggiungi_prodotto(self, prodotto: Prodotto):
        if prodotto.nome in self.prodotti.keys():
            self.prodotti[prodotto.nome] += prodotto.quantita
        else:
            self.prodotti[prodotto.nome] = prodotto.quantita

    def cerca_prodotto(self, nome: str) :
        if nome in self.prodotti:
            return f"{self.prodotti[nome]} disponibili"
        else:
            return None

    def verifica_disponibilità(self, nome: str) -> str:
        if nome in self.prodotti.keys() and self.prodotti[nome] > 0:
            return f"{nome} disponibile: {self.prodotti[nome]} pezzi"
        else:
            return f"{nome} non disponibile in magazzino"

magazzino = Magazzino()

p1 = Prodotto("pokemon", 30)
p2 = Prodotto("magic", 20)
p3 = Prodotto("pokemon", 10)

magazzino.aggiungi_prodotto(p1)
magazzino.aggiungi_prodotto(p2)
magazzino.aggiungi_prodotto(p3)

# Ricerca e disponibilità
print(magazzino.cerca_prodotto("pokemon"))          
print(magazzino.verifica_disponibilità("pokemon"))  
print(magazzino.verifica_disponibilità("lorcana")) 