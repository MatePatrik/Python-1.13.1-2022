a=input("Add meg a könyv címét! ")
b=int(input("Add meg az oldalainak számát! "))

while a!="":
    def könyv(b):
        if b>=150:
            return True
        else:
            return False
    könyv(b)
    if könyv(b):
        b="Hosszú"
    else:
        b="rövid"
    print(f"A {a} {b} terjedelmű könyv")
    a=input("Add meg a könyv címét! ")
    b=int(input("Add meg az oldalainak számát! "))