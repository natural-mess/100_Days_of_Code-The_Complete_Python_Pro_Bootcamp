import turtle as t
import random

tim = t.Turtle()
# tim.shape("turtle")

# TODO: Draw triangle
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# TODO: Draw dashline
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# TODO: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# CIRCLE = 360
# for i in range(3, 11):
#     tim.pencolor(random.random(), random.random(), random.random())
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(CIRCLE/i)

# TODO: Generate a Random Walk
# tim.width(10)
# tim.speed('fastest')
# while 1:
#     tim.pencolor(random.random(), random.random(), random.random())
#     tim.forward(30)
#     tim.setheading(random.randrange(0, 360, 90))

# TODO: Generate random RGB colors
# tim.width(10)
# tim.speed('fastest')
# t.colormode(255)
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r,g,b)

# for _ in range(200):
#     tim.color(random_colour())
#     tim.forward(30)
#     tim.setheading(random.randrange(0, 360, 90))

# TODO: Draw a Spirograph
tim.speed('fastest')
t.colormode(255)
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

for i in range(0,361,6):
    tim.color(random_colour())
    tim.circle(radius=100)
    tim.setheading(i)

screen = t.Screen()
screen.exitonclick()
