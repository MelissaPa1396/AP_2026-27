import random
from datetime import datetime

class Car:
    def __init__(self, brand:str, model:str, year:int, stk:int, fuel:int = 100):
        self.brand = brand
        self.model = model
        self.year = year
        self.stk = stk
        self.fuel = fuel
    def __str__(self):
        return f"{self.brand}: {self.model}, ({self.year}) - palivo: {self.fuel} l. "
    
    def move(self):
        usage = random.randint(5, 20)
        if self.fuel >= usage:
            self.fuel -= usage
            return f"{self.brand} {self.model} spotřeboval {usage} l paliva, zbívá mu {self.fuel}"
        else:
            return f"{self.brand} {self.model} neměl dostatek paliva, a tak nikam nedorazil. Natankuj si."
        
    def fill(self):
        filled = 100 - self.fuel
        self.fuel = 100
        return f"{self.brand} {self.model} natankoval {filled} l paliva."
    
    def STK(self):
        if self.stk < datetime.now().year:
            return f"{self.brand} {self.model} musí na technickou - technická skončila v roce {self.stk}!"
        else:
            return f"{self.brand} {self.model} má technickou v pořádku. Na technickou bude muset za {self.stk - datetime.now().year} let"
    
car1 = Car("Škoda", "Octavia 3", 2016, 2026, 85)
car2 = Car("Volkswagen", "Golf 7", 2018, 2022, 10)
car3 = Car("Toyota", "Hilux", 2014, 2028, 3)

print(car1)
print(car2)
print(car3)
print("="*40)
print(car1.move())
print(car1.move())
print(car2.move())
print(car2.move())
print(car3.move())
print("="*40)
print(car3.fill())
print(car3.move())
print("="*40)
print(car1.STK())
print("="*40)

class Garage:
    def __init__(self, name):
        self.name = name 
        self.cars = []
    
    def addCar(self, car:Car):
        self.cars.append(car)
        return f"Do garáže {self.name} bylo přidáno auto: {car.brand} {car.model}"
    
    def showCars(self):
        if len(self.cars) == 0:
            print(f"Garáž {self.name} je prázdná!")
        else:
            print(f"Auta v garáži {self.name}: ")
            for car in self.cars:
                print("-->", car)

    def oldestCar(self):
        if len(self.cars) == 0:
            return None
        else:
            the_oldest = min(self.cars, key = lambda car: car.year)
            return the_oldest    
    
    def avgFuel(self):
        if len(self.cars) == 0:
            return 0
        else:
            return sum(car.fuel for car in self.cars) / len(self.cars)


garage = Garage("Humplolec")

print(garage.addCar(car1))
print(garage.addCar(car2))
print(garage.addCar(car3))
print("="*40)
print(garage.showCars())

oldest = garage.oldestCar()
if oldest:
    print(f"Nejstarší auto v garáži je {oldest.brand} { oldest.model} ({oldest.year})")

print(f"{garage.avgFuel(): .1f} l")

print(garage.cars[2].move())

for brambora in garage.cars:
    print(brambora.STK())