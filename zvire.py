import random

class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass 
    def zvuk(self):
        return "???"
    def predstav_se(self):
        return f"Jmenuju se {self.jmeno} a je mi {self.vek} let."
    def kde_jsi(self):
        return f"jsem na místě zvaném {self.misto}."
    def jdi_na(self, n_misto:str):
        self.misto = n_misto
        return f"šel jsem na místo {n_misto}"
    
class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno
    def zvuk(self):
        return "Haf haf!"
    def aport(self):
        return f"{self.jmeno} přinesl míček!"
    def vycesat(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} utekl před kartáčem!"
        else:
            return f"{self.jmeno} se nechal vyčesat!"
    
    def predstav_se(self):
        return f"{super().predstav_se()} jsem {self.plemeno}."
    
class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.barva = barva
    def zvuk(self):
        return "Mňau! Mňau! vrr vrr..."
    def utok(self):
        return f"{self.jmeno} tě škrábla!"
    def pohladit(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} se nechala pohladit! Vrní!"
        else:
            return f"{self.jmeno} tě poškrábala a utekla!"
    def predstav_se(self):
        return f"{super().predstav_se()} jsem {self.barva}."
    
class Had(Zvire):
    def __init__(self, jmeno, vek, delkaM: int, jed: bool, misto = "terárium"):
        super().__init__(jmeno, vek, misto)
        self.delkaM = delkaM
        self.jed = jed
    def zvuk(self):
        return "Ssssss"
    def predstav_se(self):
        if self.jed:
            typ = "jedovatý"
        else:
            typ = "škrtič"
        return f"Ssss...Já jsssem {self.jmeno}, měřím {self.delkaM} metrů a jssssem typ {typ}"
    
        
Hadice = Had("Hadice", 3, 12, False)
print(Hadice.predstav_se)

Gambrinus = Pes("Gambrinus", 3, "Corgi", "gauč")

print(Gambrinus.jmeno)
print(Gambrinus.plemeno)

print(Gambrinus.predstav_se())

print(Gambrinus.kde_jsi())

print(Gambrinus.zvuk())

print(Gambrinus.aport())

print(Gambrinus.vycesat())
print("-" * 50)

Susenka = Kocka("Sušenka", 3, "Zrzavá", "gauč")

print(Susenka.jmeno)
print(Susenka.barva)

print(Susenka.predstav_se())

print(Susenka.zvuk())

print(Susenka.utok())

print(Susenka.pohladit())
print("-" * 50)


zvire = Zvire("Šoral", 50)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)

print(zvire.zvuk())

print(zvire.predstav_se())

print(zvire.kde_jsi())

print(zvire.jdi_na("Les"))

print(zvire.kde_jsi())

zvire2 = Zvire("Wolfram", 32, "Prasečák")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)

print(zvire2.predstav_se())

print(zvire2.kde_jsi())

print(zvire2.jdi_na("Autobus"))

print(zvire2.kde_jsi())

zoo = [Gambrinus, Susenka, Hadice]

for obyvatel in zoo:
    print(obyvatel.predstav_se())
    print(obyvatel.zvuk())
    print("-" * 20)