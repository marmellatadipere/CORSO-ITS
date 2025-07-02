from __future__ import annotations
from typing import Any
import datetime

class Progetto:
    pass


class Impiegato:
    _nome: str #noto alla nascita
    _cognome: str #noto alla nascita
    _dataNascita: datetime.date #noto alla nascita
    _progetti = set[progetti]

    
    def __init__(self, nome:str, cognome:str, datadiNascita: datetime.date) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._dataNascita = datadiNascita
        self._progetti = set()
    def nome(self) -> str:
        return self._nome
    def setNome(self, nome:str) -> None:
        self._nome = nome
    def cognome(self, cognome:str) -> None:
        return self._cognome
    def setcognome(self, cognome: str) -> None:
        self._cognome = cognome
    def progetti(self, progetto:Progetto) -> frozenset[progetto]:
        return frozenset (self._progetti)
    def add_progetto(self, progetto:Progetto, impiegato:Impiegato) -> None:
        nuovoProgetto: Progetto = progetto(impiegato=self, progetto=self, data = datetime.datetime)