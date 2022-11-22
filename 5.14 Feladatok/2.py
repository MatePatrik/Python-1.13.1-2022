T=[0,1,2,3,4,5,6]
Indulás=int(input("Hanyas számú napon indulsz?: "))
Maradás=int(input("Hány napot alszol ott?: "))
while Maradás>7:
    Maradás=Maradás-7
Maradás=Maradás+Indulás
for i in T:
    if Maradás==0:
        Maradás="hétfő"
    elif Maradás==1:
        Maradás="kedd"
    elif Maradás==2:
        Maradás="szerda"
    elif Maradás==3:
        Maradás="csütörtök"
    elif Maradás==4:
        Maradás="péntek"
    elif Maradás==5:
        Maradás="szombat"
    elif Maradás==6:
        Maradás="vasárnap"
print("Ezen a napon térsz haza: ", Maradás)