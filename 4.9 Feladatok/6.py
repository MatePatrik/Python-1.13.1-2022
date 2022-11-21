import turtle
kép=turtle.Screen()
Sanyi=turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("hotpink")
Sanyi.pensize(4)
def szabalyos_haromszog_rajzolas(t, sz):
    for i in range(3):
        t.left(120)
        t.forward(sz)
szabalyos_haromszog_rajzolas(Sanyi,200)
kép.mainloop()