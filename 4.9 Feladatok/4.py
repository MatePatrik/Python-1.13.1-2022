import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()
Sanyi.pensize(4)
Sanyi.color("blue")
ablak.bgcolor("lightgreen")
for i in range(5):    
    for i in range(4):
        Sanyi.forward(100)
        Sanyi.left(90)
        Sanyi.forward(100)
        Sanyi.backward(200)
        Sanyi.forward(100)
        Sanyi.right(90)
        Sanyi.backward(100)
        Sanyi.left(90)
    Sanyi.left(36)
ablak.mainloop()

