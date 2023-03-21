from kecske import Ember
import random
T=[]

for i in range(3):
    nev=input("Add meg a nevet! ")
    foglalkozas=input("Add meg a foglalkozását! ")
    nem=input("Add meg a nemét (f/n)! ")
    szam=random.randint(0,50)
    asd=T.append(nev,foglalkozas,nem,szam)

for i in range(3):
    print(T)