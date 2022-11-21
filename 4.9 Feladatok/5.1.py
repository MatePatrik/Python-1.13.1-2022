import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()
ablak.bgcolor("lightgreen")
Sanyi.color("hotpink")
Sanyi.pensize(4)
Sanyi.color("blue")
ablak.bgcolor("lightgreen")
def spiral(t,h):
    t.forward(h)
    t.right(89)
meret = 20
for i in range(0,200):
    spiral(Sanyi,meret)
    meret = meret+5
