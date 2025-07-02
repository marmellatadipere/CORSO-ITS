'''
Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing 
methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  
A query on a given date allows for retrieving a given new date. Note that a date is an object for your database; 
it must be instantiated from a string.


Database di date: scrivere una classe che gestisca un database di date con il formato gg.mm.aaaa. 
È necessario implementare metodi per aggiungere una nuova data, eliminare una data specifica, 
modificarne una ed eseguire una query su una data specifica. Una query su una data specifica consente di recuperare
una nuova data specifica. Si noti che una data è un oggetto per il database; deve essere istanziata da una stringa.

'''

from datetime import datetime, date
from typing import Any

class Data:
    def __init__(self,data_singola:str) -> None :
        # Converte una stringa 'gg.mm.aaaa' in un oggetto datetime.date
        try:
            self.data:date = datetime.strptime(data_singola, "%d.%m.%Y").date()
        except ValueError:
            # Se il formato non è corretto, solleva un'eccezione
            raise ValueError(f"Formato data non valido: {data_singola}. Usa 'gg.mm.aaaa'.")
        
    def __str__(self):
        return self
        
    def addDate (self) -> str:
        