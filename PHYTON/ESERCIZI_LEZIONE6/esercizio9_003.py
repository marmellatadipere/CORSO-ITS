'''
9-3. Users: Make a class called User. 
Create two attributes called first_name and last_name, and then create several other attributes 
that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.
'''

class User:
    def __init__(self, name:str, last_name:str, age: int):
        self.name = name
        self.lastname = last_name
        self.age = age

    def describe_user(self):
        print(f"\nIl nome e'{self.name}\nIl cognome è {self.lastname}\nL'età è {self.age}")
    
    def greet_user(self):
        print(f"welcome back user {self.name}") 


# Create and describe a user named Eric
eric = User('eric', 'matthes', 18)
eric.describe_user()  # Show Eric's profile information
eric.greet_user()  # Greet Eric
