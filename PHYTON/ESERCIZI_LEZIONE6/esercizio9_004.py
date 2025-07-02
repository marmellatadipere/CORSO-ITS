'''
9-4. Number Served: Start with your program from Exercise 9-1. 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this value and 
print it again. Add a method called set_number_served() that lets you set the number of 
customers that have been served. 
Call this method with a new number and print the value again. 
Add a method called increment_number_served() that lets you increment the number of customers 
who’ve been served. Call this method with any number you like that could represent how many customers 
were served in, say, a day of business. 
'''

class Restaurant:
    number_served = 0

    def __init__(self, name:str, cuisinetype:str) -> None :
        self.name = name.title()
        self.cuisinetype = cuisinetype
        self.number_served = 0
    def describe_restaurant(self):
        print(self.name)
        print(self.cuisinetype)
    def open_restaurant(self):
        print("il ristorante e' aperto")
    def set_number_served(self, number_served) -> None :
        self.number_served = number_served
    def increment_number_served(self, number) -> None :
        self.number_served += number


ristornate1 = Restaurant("la foresta", "cucina italiana")
ristornate1.describe_restaurant()
print(ristornate1.number_served) # quante persone ho servito
ristornate1.number_served = 10 #cambio direttamente il numero
print(ristornate1.number_served)

ristornate1.set_number_served(40)
print(ristornate1.number_served)

ristornate1.increment_number_served(5)
print(ristornate1.number_served)