import turtle

turtle.setup(startx=-150, starty=-150)
turtle.pendown()
sides = 12
for i in range(sides):
    turtle.fd(50)
    turtle.lt(360/sides)


