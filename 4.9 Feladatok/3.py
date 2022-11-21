import turtle
ablak = turtle.Screen()
Eszti = turtle.Turtle()
Eszti.pensize(3)
Eszti.color("blue")
ablak.bgcolor("lightgreen")
def sokszog_rajzolas(t, n, sz):
    for i in range(0,8):
        t.left(sz)
        t.forward(n)
sokszog_rajzolas(Eszti, 8, 50)
ablak.mainloop()

