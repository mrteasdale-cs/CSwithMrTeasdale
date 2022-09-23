import turtle
turtle.pendown()

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.penup()
turtle.forward(120)
turtle.pendown()

for i in range(3):
    turtle.forward(100)
    turtle.right(120)

turtle.penup()
turtle.forward(120)
turtle.pendown()

for i in range(5):
    turtle.forward(100)
    turtle.right(360/5)
