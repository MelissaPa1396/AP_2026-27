import random
class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi
    def predstav_se(self):
        return f"Jmenuju se {self.jmeno}, moje HP je zrovna na {self.zdravi}HP."
    def utok(self):
        return "-0 HP"
    
class Rytir(Postava):
    def __init__(self, jmeno, brneni, zdravi):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni
    def predstav_se(self):
        return f"Jmenuji se {self.jmeno}, jsem nebojácný rytíř z říše králů, a jsem an {self.zdravi}HP."
    def utok(self):
        sila = (random.randint(10,20))
        return f"Sekl jsem mečem, způsobilo to na nepřítele zneškodnění -{sila}HP."
    def zablokuj(self):
        return f"Zablokoval jsem útok, na moje brnění to způsobilo zneškodnění -5HP."
        
class Mag(Postava):
    def __init__(self, jmeno, mana:int, zdravi):
        super().__init__(jmeno, zdravi)
        self.mana = mana 
    def predstav_se(self):
        return f"Jmenuju se {self.jmeno}, jsem mág z klanu Oustros a jsem na {self.zdravi}HP"
    def utok(self):
        mana_pwr = (random.randint(10,50))
        if mana_pwr >=10:
            return f"Použila jsem -10 many, zbylo mi {self.mana-10} many, vylepšila jsem si magii a způsobilo to na nepřítele zneškodnění -{(random.randint(20,45))}HP"
        else:
            return f"Nemám dost many, mohla jsem jenom využít slabý útok které způsobilo zneškodnění -5HP"
Oswaldo = Rytir("Oswaldo von Lustrel", 100, 200)
print(Oswaldo.predstav_se())
print(Oswaldo.utok())
print(Oswaldo.zablokuj())
        
Manasama = Mag("Manasama", 50, 100)
print(Manasama.predstav_se())
print(Manasama.utok())
