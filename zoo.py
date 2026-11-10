import random
from datetime import datetime

class Animal():
    def __init__(self, species:str, name:str, birth_year:int = 0, checkup_year:int = 0, energy:int = 100):
        self.species = species
        self.name = name
        self.birth_year = birth_year
        self.checkup_year = checkup_year
        self.energy = energy
    
    def __str__(self):
        return f"{self.name} ({self.birth_year}), energie: {self.energy}%."
    
    def play(self):
        usage = random.randint(5, 20)
        if self.energy >= usage:
            self.energy -= usage
            return f"{self.species} {self.name} si při hraní spotřebovalo {usage} % energie! Zbývá: {self.energy} % energie!"
        else:
            return f"{self.species} {self.name} je unavené. Potřebuje si jít odpočinout... Energie: {self.energy}."
        
    def feed(self):
        filled = 100 - self.energy
        self.energy = 100
        return f"{self.species} {self.name} bylo nakrmeno a doplnilo si {filled} % energie!"
    
    def vetCheck(self):
        if self.checkup_year < datetime.now().year:
            return f"{self.species} {self.name} musí jít k veterináři! Platnost předešlé prohlídky skončila v roce {self.checkup_year}!"
        else:
            return f"{self.species} {self.name} má prohlídky v pořádku. Příští kontrola bude za {self.checkup_year - datetime.now().year} let."
        

class Zoo:
    def __init__(self, name):
        self.name = name

animal1 = Animal("Hyrax", "Caline", 2023, 2023, 85)
animal2 = Animal("Snow leopard", "Snowy", 2020, 2022)
animal3 = Animal("Fruit bat", "Shadow", 2021, 2028, 10)
animal4 = Animal("Ground squirrel", "Niko", 2025, 2027, 40)

print(animal1)
print(animal1.play())
print(animal1.play())
print(animal1.play())
print(animal1.feed())
print(animal1.vetCheck())

print("="*40)

print(animal2)
print(animal2.play())
print(animal2.play())
print(animal2.play())
print(animal2.feed())
print(animal2.vetCheck())

print("="*40)

print(animal3)
print(animal3.play())
print(animal3.play())
print(animal3.play())
print(animal3.feed())
print(animal3.vetCheck())

print("="*40)

print(animal4)
print(animal4.play())
print(animal4.play())
print(animal4.play())
print(animal4.feed())
print(animal4.vetCheck())
