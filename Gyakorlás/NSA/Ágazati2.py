def Hosszúság(a):
    b = False
    if a > 150:
        b = True
    return b

cím = input("Cím: ")
while cím !="":
    Oldal = int(input("Oldalak száma: "))
    oldalak = Hosszúság(Oldal)
    if oldalak:
        print("A könyv hosszú")
    else:
        print("A könyv rövid")
    cím = input("Cím: ")