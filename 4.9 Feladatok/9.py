import turtle
kép=turtle.Screen()
Sanyi=turtle.Turtle()
kép.bgcolor("lightgreen")
Sanyi.color("hotpink")
Sanyi.pensize(4)
def szabalyos_haromszog_rajzolas(t,h):
    for i in range(5):
        t.right(144)
        t.forward(h)
szabalyos_haromszog_rajzolas(Sanyi,100)
kép.mainloop()