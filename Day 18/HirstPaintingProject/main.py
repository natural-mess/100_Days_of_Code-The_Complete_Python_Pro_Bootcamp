import colorgram
import turtle as t
import random

def extract_color(image, num_of_color):
    colors = colorgram.extract('image.jpg', num_of_color)
    list = []
    for color in colors:
        list_element = []
        for i in range(3):
            list_element.append(color.rgb[i])
        list.append(tuple(list_element))
    return list

# print(extract_color('image.jpg', 30))
color_list = extract_color('image.jpg', 100)
# print(color_list)
color_list.pop(0)
color_list.pop(1)
color_list.pop(2)

pen = t.Turtle()
pen.speed('fastest')
pen.penup()
pen.setheading(0)
pen.hideturtle()
pen.setpos(-300,-300)
first_pos = pen.pos()
t.colormode(255)

for i in range(0, 650, 70):
    next_y = int(first_pos[1]+i)
    pen.setpos(int(first_pos[0]), next_y)
    for _ in range(10):
        # Using circle method
        # pen.pendown()
        # pen.fillcolor(random.choice(color_list))
        # pen.begin_fill()
        # pen.circle(10)
        # pen.end_fill()
        # pen.penup()

        # Using dot method
        pen.dot(20, random.choice(color_list))
        
        pen.setheading(0)
        pen.forward(70)

screen = t.Screen()
screen.exitonclick()