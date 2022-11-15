from random import randrange
import turtle
xs=[0,1,2,3,4,5,6,7,8,9,10]
ablak = turtle.Screen()
Turtle = turtle.Turtle()
for i in range(0,20):
    random = randrange(xs)
    if random < 0:
        Turtle.left(random)
        Turtle.forward(100)
        b = (random)
        print(b)
    elif random > 0:
        Turtle.right(random)
        Turtle.forward(100)
        a = (random)
        print(a)
print(a,"ebbe az irányba néz")
ablak.mainloop()