import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()
Sanyi.pensize(4)
Sanyi.color("hotpink")
ablak.bgcolor("lightgreen")
def negyzet(t,h):
    for i in range(5):
        t.forward(h)
        t.left(90)
meret = 20
for i in range(5):
    negyzet(Sanyi,meret)
    Sanyi.right(90)
    Sanyi.penup()
    Sanyi.forward(15)
    Sanyi.pendown()
ablak.mainloop()