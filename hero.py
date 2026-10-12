class Hero:
    def __init__(self, jmeno:str, LVL:int, lokace:str = "louka"):
        self.jmeno = jmeno
        self.LVL = LVL
        self.lokace = lokace

    def pokrik(self):
        return "TOHLE TI NEPROJDE!"
    
    def predstav_se(self):
        return f"Jmenuju se {self.jmeno} a jsem na levelu {self.LVL}. Boj se mě."
    
    def kde_jsi(self):
        return f"Zrovna se nacházím na místě zvaném {self.lokace}. Přibližuju se."
    
    def presun_se(self, n_misto:str = "Posvátné katakomby plzeňského pivovaru"):
        self.misto = n_misto
        return f"Přesunul jsem se na místo zvané {n_misto}"
    
self = Hero("Arcibiskup Tichošlápek z Brna", 67)
print(self.jmeno)
print(self.LVL)
print(self.lokace)

print(self.predstav_se())
print(self.kde_jsi())
print(self.presun_se())

class Robot:
    def __init__(stroj, oznaceni:str, baterie:int, ukol:str = "výměna žárovek na palubní lodi"):
        stroj.oznaceni = oznaceni
        stroj.baterie = baterie
        stroj.ukol = ukol

    def zvuk(stroj):
        return "Beep boop"
    
    def diagnostika(stroj):
        return f"Moje označení je {stroj.oznaceni} a moje baterie je na {stroj.baterie} %. Beep."
    
    def akt_ukol(stroj):
        return f"Můj aktuální úkol je {stroj.ukol}. Boop."
    
    def zadej_ukol(stroj, z_ukol:str = "atentát na Arcibiskupa Tichošlápka z Brna"):
        stroj.ukol = z_ukol
        return f"Můj nový úkol je {z_ukol}. Beep Boop jeho smrt bude televizována. Beep."
    
stroj = Robot("Admirál Ortho verze XI0824-182269", 99)
print(stroj.oznaceni)
print(stroj.baterie)
print(stroj.ukol)

print(stroj.akt_ukol())
print(stroj.diagnostika())
print(stroj.zadej_ukol())

class Motorka:
    def __init__(motor, znacka:str, kategorie:str, stav_nadrze:int, stav_stojanku:str = "vyklopený"):
        motor.znacka = znacka
        motor.kategorie = kategorie
        motor.stav_nadrze = stav_nadrze
        motor.stav_stojanku = stav_stojanku

    def zatoc_plyn(motor):
        return "Vruuuum"
