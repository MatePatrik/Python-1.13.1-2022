T=[0,1,2,3,4,5,6]
Maradás=int(input("Hány napot alszol ott?: "))
def napok(Maradás):
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
    print("A kiválasztott napod: ",Maradás)
napok(Maradás)