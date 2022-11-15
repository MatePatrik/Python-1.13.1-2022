import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()
Sanyi.pensize(4)
Sanyi.color("hotpink")
ablak.bgcolor("lightgreen")

def negyzet(t,h):
    for i in range(5):
        if meret == 20:
            t.forward(h)
            t.left(90)
        elif meret == 40:
            t.forward(h)
            t.right(90)
        elif meret == 60:
            t.forward(h)
            t.left(90)
        elif meret == 80:
            t.forward(h)
            t.right(90)
        elif meret == 100:
            t.forward(h)
            t.left(90)
meret = 20
for i in range(5):
    negyzet(Sanyi,meret)
    meret = meret+20
    Sanyi.right(135)
    Sanyi.penup()
    Sanyi.forward(15)
    Sanyi.right(135)
    Sanyi.pendown()
ablak.mainloop()