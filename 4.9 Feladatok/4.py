import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()
Sanyi.pensize(4)
Sanyi.color("blue")
ablak.bgcolor("lightgreen")
def spiral(t,h):
    for i in range(5):
        t.forward(200)
        t.right(h)
meret = 0
for i in range(10):
    spiral(Sanyi,meret)
    meret = meret+36

