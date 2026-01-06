import turtle as t

pen = t.Turtle()
screen = t.Screen()

def move_forward():
    pen.forward(10)

def move_backward():
    pen.backward(10)

def rotate_counter_clockwise():
    pen.left(10)

def rotate_clockwise():
    pen.right(10)

def clear():
    pen.reset()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)
screen.listen()
screen.exitonclick()
