szam1=int(input("Adj meg egy számot: "))
szam2=int(input("Adj meg egy másik számot: "))

if szam1 < 0 and szam2 < 0:
    print("Mindkettő szám negatív")
elif szam1 > 0 and szam2 > 0:
    print("Mindkettő szám pzitív")
elif szam1 < 0:
    print("A első szám negatív")
elif szam2 < 0:
    print("A második szám negatív")
