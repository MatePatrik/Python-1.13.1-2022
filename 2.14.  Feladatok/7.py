a=int(input("Hány óra van? "))
b=int(input("Hány órával később ébresszen az ébresztő? "))
c=a+b
while c>24:
    c=c-24
print(c,"órakor fog kelteni az ébresztő!")