import turtle

def rajzolj_oszlopot(t, magassag):
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    t.right(90)
    if magassag>0:
        t.write("  "+str(magassag))
    if magassag<0:
        t.penup()
        t.backward(15)
        t.write(" "+str(magassag))
        t.forward(15)
        t.pendown()
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.color("blue", "red")
Eszti.pensize(3)
xs = [-48,-117,200,-240,160,260,-220]
for m in xs:
    if m>=200:
        Eszti.color("blue", "red")
    elif m>=100 and m<200:
        Eszti.color("blue", "yellow")
    elif m<100:
        Eszti.color("blue", "green")
    rajzolj_oszlopot(Eszti, m)
ablak.mainloop()

# Ahol negatív az érték ott fejjellefelé rajzolja meg a diagrammot