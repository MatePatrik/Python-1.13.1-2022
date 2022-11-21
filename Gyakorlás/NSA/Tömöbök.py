import random
#t = [0,1,2,3,4,5,6,7,8,9,10,"Feri"]
#print("t")


t = []
for i in range(5):
    t.append(random.randint(0,100))
print(t)


#Összeadás

#Összeg = 0
#for i in t:
#    Összeg = Összeg+i
#print(Összeg)


#átlag

#atlag = Összeg/len(t)
#print(atlag)


#Minimum

min = 101
for i in t:
    if min>i:
        min = i
print(min)


#Maximum
max = -1
for i in t:
    if max<i:
        max = i
print(max)