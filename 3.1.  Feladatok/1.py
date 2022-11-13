import turtle
bg=input("Add meg a háttérszint ANGOLUL!!!: ")

ablak = turtle.Screen()
Sanyi = turtle.Turtle()
ablak.bgcolor(bg)
pc=input("add meg a ceruza szinét ANGOLUL!!!: ")
pw=int(input("add meg a ceruza vastagságát ANGOLUL!!!: "))
Sanyi.color(pc)
Sanyi.pensize(pw)
Sanyi.forward(50)
Sanyi.left(90)
Sanyi.forward(30)
ablak.mainloop()