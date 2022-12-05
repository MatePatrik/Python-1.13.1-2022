import random

class Szere:
    def __init__(self,nev,fog,nem,szam):
        self.nev=nev
        self.fog=fog
        self.nem=nem
        self.szam=szam

    def FvN(nem):
        if nem=="f":
            return "férfi"
        elif nem=="n":
            return "nő"

t=[]
for i in range(3):
    a=input("Add meg a neved!")
    b=input("Add meg a foglalkozást! ")
    c=input("Add meg a nemed F/N! ")
    d=random.randint(1,50)
    t.append(Szere(a,b,c,d))
for i in range(3):
    print(t[i].nev,"")