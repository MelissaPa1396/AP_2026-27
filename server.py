import random
from datetime import datetime

class Server():
    def __init__(self, hostname:str, os:str, deployYear:int, warrantyYear:int = 0, storageFree:int = 100):
        self.hostname = hostname
        self.os = os 
        self.deployYear = deployYear
        self.warrantyYear = warrantyYear
        self.storageFree = storageFree

    def __str__(self):
        return f"{self.hostname} ({self.os}, {self.deployYear}) - volné místo: {self.storageFree} %"
    
    def saveData(self):
        storage = random.randint(5, 20)
        if self.storageFree >= storage:
            self.storageFree -= storage
            return f"Na server {self.hostname} se uložila data (zabráno {storage} %). Zbývá {self.storageFree} % volného místa." 
        else:
            return f"Na serveru {self.hostname} není dostatek místa! Je potřeba {storage} %, ale k dispozici je jenom {self.storageFree} %."
        
    def cleanDisk(self):
        clean = 100 - self.storageFree
        self.storageFree = 100
        return f"Disky na serveru {self.hostname} byly pročištěny. Uvolnilo se {clean} % místa."
    
    def warrantyCheck(self):
        if self.warrantyYear < datetime.now().year:
            return f"Už je po záruce! Záruka trvala do roku {self.warrantyYear}."
        else:
            return f"Záruka je v pořádku, zbývá: {self.warrantyYear - datetime.now().year} let."




server1 = Server("Web-Main", "Ubuntu Linux", 2018, 2023, 80)
server2 = Server("DB-Cluster", "Windows Server", 2021, 2026,)
server3 = Server("Backup-NAS", "Debian Linux", 2015, 2020, 15)

#print(server1)
#print(server2)
#print(server3)
#print(server1.cleanDisk())
#print(server2.cleanDisk())
#print(server3.cleanDisk())
#print(server1.warrantyCheck())
#print(server2.warrantyCheck())
#print(server3.warrantyCheck())










        
class ServerRoom:
    def __init__(self,name):
        self.name = name
        self.servers = []
    
    def addServer(self, server:Server):
        self.servers.append(server)
        return f"Do serverovny {self.name} byl přidán server {server.hostname}."
    
    def showServers(self):
        if len(self.servers) == 0:
            return f"V serverovně {self.name} nejsou žádné servery! Zkus nějaké přidat."
        else:
            print(f"Servery v serverovně {self.name}: ")
            for server in self.servers:
                print("-->", server)
        
    def oldestServer(self):
        if len(self.servers) == 0:
            return None
        else:
            oldest = min(self.servers, key = lambda server: server.deployYear)
            return f"Nejstarší server je {oldest}."
        
    def avgStorage(self):
        if len(self.servers) == 0:
            return 0
        else:
            return sum(server.storageFree for server in self.servers) / len(self.servers)
        

serverovna = ServerRoom("SOUEPL Datacentrum")

print("="*40)
print(serverovna.addServer(server1))
print(serverovna.addServer(server2))
print(serverovna.addServer(server3))
print("="*40)
print(serverovna.showServers())
print("="*40)
print(server1.saveData())
print(server1.saveData())
print(server2.saveData())
print(server2.saveData())
print(server3.saveData())
print(server3.saveData())
print("="*40)
print(serverovna.showServers())
print("="*40)
print("Průměrné volné místo: ")
print(f"{serverovna.avgStorage(): .1f} %")
print("="*40)
print(serverovna.oldestServer())
print("="*40)
print("Kontroly záruky:")
print(server1.warrantyCheck())
print(server2.warrantyCheck())
print(server3.warrantyCheck())
