import turtle
turtle.pendown()
distance = 10
for i in range(1,8):
    for j in range(1,3):
        turtle.forward(distance)
        turtle.right(90)
    distance = distance + 10

