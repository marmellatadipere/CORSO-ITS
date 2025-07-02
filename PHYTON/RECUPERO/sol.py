class ContactManager:
    def __init__(self):
        self.contacts: dict[str, list[str]] = {}

    def create_contact(self, name: str, phone_numbers: list[str]):
        if name in self.contacts:
            return "Errore: il contatto esiste già."
        self.contacts[name] = phone_numbers
        return {name: self.contacts[name]}

    def add_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        if phone_number in self.contacts[contact_name]:
            return "Errore: il numero di telefono esiste già."
        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}

    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        if phone_number not in self.contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        self.contacts[contact_name].remove(phone_number)
        return {contact_name: self.contacts[contact_name]}

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        if old_phone_number not in self.contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        index = self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number
        return {contact_name: self.contacts[contact_name]}

    def list_contacts(self):
        return list(self.contacts.keys())

    def list_phone_numbers(self, contact_name: str):
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        return self.contacts[contact_name]

    def search_contact_by_phone_number(self, phone_number: str):
        matching_contacts = [name for name, numbers in self.contacts.items() if phone_number in numbers]
        if not matching_contacts:
            return "Nessun contatto trovato con questo numero di telefono."
        return matching_contacts
    
manager = ContactManager()

print(manager.create_contact("Mario", ["1234567890"]))  
# {'Mario': ['1234567890']}

print(manager.add_phone_number("Mario", "0987654321"))  
# {'Mario': ['1234567890', '0987654321']}

print(manager.list_phone_numbers("Mario"))  
# ['1234567890', '0987654321']

print(manager.update_phone_number("Mario", "1234567890", "1111111111"))  
# {'Mario': ['1111111111', '0987654321']}

print(manager.remove_phone_number("Mario", "0987654321"))  
# {'Mario': ['1111111111']}

print(manager.search_contact_by_phone_number("1111111111"))  
# ['Mario']

print(manager.list_contacts())  
# ['Mario']manager = ContactManager()

print(manager.create_contact("Mario", ["1234567890"]))  
# {'Mario': ['1234567890']}

print(manager.add_phone_number("Mario", "0987654321"))  
# {'Mario': ['1234567890', '0987654321']}

print(manager.list_phone_numbers("Mario"))  
# ['1234567890', '0987654321']

print(manager.update_phone_number("Mario", "1234567890", "1111111111"))  
# {'Mario': ['1111111111', '0987654321']}

print(manager.remove_phone_number("Mario", "0987654321"))  
# {'Mario': ['1111111111']}

print(manager.search_contact_by_phone_number("1111111111"))  
# ['Mario']

print(manager.list_contacts())  
# ['Mario']