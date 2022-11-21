Jelszo = "nagy"
Felhasznalo = "kicsi"
jelszo = input("Ird be a jelszót: ")
felhasznalo = input("Ird be a felhasználó nevet: ")
lehetőségek = 6
while Jelszo != jelszo or Felhasznalo != felhasznalo:
    print("Rossz jelszó vagy felhasználó név!!!",lehetőségek-1,"lehetőség maradt")
    jelszo = input("Ird be a jelszót: ")
    felhasznalo = input("Ird be a felhasználó nevet: ")





if Jelszo == jelszo and Felhasznalo == felhasznalo:
    print("Kaki vagy :(")
