import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
        print(msg)

#1. feladat
n = input("Irj be egy égtáj kezdő betűjét NAGY BETŰVEL: ")
def fordulj_orajarasi_iranyba(n):
    teszt(fordulj_orajarasi_iranyba("É") == "K")
    teszt(fordulj_orajarasi_iranyba("Ny") == "É")
    if n == "É":
        print("K")
    elif n == "K":
        print("D")
    elif n == "D":
        print("Ny")
    elif n == "Ny":
        print("É")
        return "É"
    
#2. feladat
a=int(input("Irj be egy számot 1-től 6-ig: "))
def nap_nev(a):
    if a==0:
        a="hétfő"
        return a
    elif a==1:
        a="kedd"
    elif a==2:
        a="szerda"
    elif a==3:
        a="csütörtök"
    elif a==4:
        a="péntek"
    elif a==5:
        a="szombat"
    elif a==6:
        a="vasárnap"
print("Ezt a napot választottad: ", a)
if a==0:
    teszt(nap_nev(a) == "hétfő")
elif a==1:
    teszt(nap_nev(a) == "kedd")
elif a==2:
    teszt(nap_nev(a) == "szerda")
elif a==3:
    teszt(nap_nev(a) == "csütörtök")
elif a==4:
    teszt(nap_nev(a) == "péntek")
elif a==5:
    teszt(nap_nev(a) == "szombat")
elif a==6:
    teszt(nap_nev(a) == "vasárnap")
elif a>6:
    teszt(nap_nev(a) == None)