'''
9-5. Login Attempts: 
Add an attribute called login_attempts to your User class from Exercise 9-3. 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.
'''

class User:
    login_attempt = 0
    
    def __init__(self, name:str, last_name:str, age: int,):
        self.name = name
        self.lastname = last_name
        self.age = age
        self.login_attempt = 0

    def describe_user(self):
        print(f"\nIl nome e'{self.name}\nIl cognome è {self.lastname}\nL'età è {self.age}")
    
    def greet_user(self):
        print(f"welcome back user {self.name}") 
    
    def login_attempt(self, attempt:int) -> None:
        self



# Create and describe a user named Eric
eric = User('eric', 'matthes', 18)
eric.describe_user()  # Show Eric's profile information
eric.greet_user()  # Greet Eric
