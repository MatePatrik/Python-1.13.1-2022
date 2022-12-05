def magassag(mag):
    if mag>170:
        return True
    else:
        return False

nev=input("Ird be a neved: ")
while nev!="":
    m=int(input("Ird be a magasságod: "))
    if magassag(m):
        print(nev,"magasabb mint az átlag")
    else:
        print(nev,"kisebb mint az átlag")
    nev=input("Ird be a neved: ")