class ContactManager:
    def __init__(self):

        self.contacts: dict[list[str]] = {}
    
    def createContact(self, name:str, phoneNumbers: list[str]) :
        if name in self.contacts:
            return f"Errore: il contatto esiste già."
        else:
            self.contacts[name] = phoneNumbers
        
        return {name : self.contacts[name]}


    def addPhoneNumber(self, contactName:str, phoneNumber: str):
        if contactName not in self.contacts:
            return "Errore: il contatto non esiste"
        if phoneNumber in self.contacts[contactName]:
            return "Errore: il numero di telefono esiste già"

        self.contacts[contactName] = phoneNumber
        return {contactName: self.contacts[contactName]}
    
    def removePhoneNumber(self, contactName:str, phoneNumber: str):
        if contactName not in self.contacts:
            return "Errore: il contatto non esiste"
        if phoneNumber not in self.contacts[contactName]:
            return "Errore: il numero di telefono non esiste"

        self.contacts[contactName].remove(phoneNumber)
        return {contactName: self.contacts[contactName]}
    
    def updatePhoneNumber(self, contactName: str, oldPhoneNumber: str, newPhoneNumber:str):
        if oldPhoneNumber in self.contacts[contactName]:
            self.contacts[contactName] = newPhoneNumber
        else:
            return "Errore il numero non esiste"
        if contactName not in self.contacts:
            return "Errore: il contatto non esiste"
        return {contactName : newPhoneNumber}
    
    def listContacts(self) -> list[str]:
        
        listachiavi = []
        for key, value in self.contacts:
            listachiavi.append(key)

        return listachiavi
    
    def listPhoneNumbers(self,contactName:str):
        if contactName in self.contacts:
            return self.contacts[contactName]
        else:
            return "Errore: il contatto non esiste"
        
    def searchContactByPhoneNumber(self, phoneNumber: str):
        if phoneNumber not in self.contacts:
            return "Errore: il numero di telefono non esiste"
        
        listaC = []
        for contatto, telefono in self.contacts:
            if telefono in self.contacts[phoneNumber]:
                listaC.append(contatto)

        return listaC





manager = ContactManager()

print(manager.createContact("Mario", ["1234567890"]))  
# {'Mario': ['1234567890']}

print(manager.addPhoneNumber("Mario", "0987654321"))  
# {'Mario': ['1234567890', '0987654321']}

print(manager.listPhoneNumbers("Mario"))  
# ['1234567890', '0987654321']

print(manager.updatePhoneNumber("Mario", "1234567890", "1111111111"))  
# {'Mario': ['1111111111', '0987654321']}

#print(manager.removePhoneNumber("0987654321"))
# {'Mario': ['1111111111']}

print(manager.searchContactByPhoneNumber("1111111111"))  
# ['Mario']

print(manager.listContacts())  
# ['Mario']