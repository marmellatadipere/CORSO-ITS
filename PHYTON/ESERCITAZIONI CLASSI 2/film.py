class Film:
    def __init__(self, titolo: str, durata: float) -> None:
        self.titolo = titolo
        self.durata = durata

    def __str__(self):
        return f"{self.titolo} : {self.durata} h"


class Sala:
    def __init__(self, num: int, filmOggi: Film, pTot: int) -> None:
        self.num = num
        self.film = filmOggi
        self.pTot = pTot
        self.postiprenotati = 0

    def prenota_posti(self, num_posti: int) -> str:
        if self.posti_disponibili() >= num_posti:
            self.postiprenotati += num_posti
            return f"{num_posti} posti prenotati per il film '{self.film.titolo}' nella sala {self.num}."
        else:
            return f"Errore: solo {self.posti_disponibili()} posti disponibili nella sala {self.num}."

    def posti_disponibili(self) -> int:
        return self.pTot - self.postiprenotati

    def __str__(self):
        return f"Sala num.{self.num}, programma {self.film} | posti rimanenti: {self.posti_disponibili()}"


class Cinema:
    def __init__(self):
        self.sale: list[Sala] = []

    def aggiungi_sala(self, sala: Sala):
        self.sale.append(sala)

    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for sala in self.sale:
            if sala.film.titolo.lower() == titolo_film.lower():
                pdisp = sala.posti_disponibili()
                if pdisp <= 0:
                    return f"Errore: nessun posto disponibile per '{titolo_film}' nella sala {sala.num}."
                elif num_posti > pdisp:
                    return f"Errore: solo {pdisp} posti disponibili per '{titolo_film}' nella sala {sala.num}."
                else:
                    return sala.prenota_posti(num_posti)
        return f"Errore: il film '{titolo_film}' non è in programmazione."
    

    