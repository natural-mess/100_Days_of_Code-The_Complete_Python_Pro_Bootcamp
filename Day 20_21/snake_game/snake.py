from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # This game has a bug that when snake is moving to the right,
        # if user presses left+down at the same time, the snake will move to the left right away
        # This look will avoid that issue
        self.position_locked = False
        # self.pause_game = False

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # This actually adds a new segment at the same coordinate as the last element of segments list
        # But thanks to the move method which is called all the time in while loop,
        # all the old segments will move forward, leaving the newly added segment alone in the coordinate of the last element
        # This makes us see that the snake gets longer
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_segment_position = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_segment_position)
        self.head.forward(MOVE_DISTANCE)
        self.position_locked = False

    def up(self):
        if self.head.heading() != DOWN and not self.position_locked:
            self.head.setheading(UP)
            self.position_locked = True

    def down(self):
        if self.head.heading() != UP and not self.position_locked:
            self.head.setheading(DOWN)
            self.position_locked = True

    def left(self):
        if self.head.heading() != RIGHT and not self.position_locked:
            self.head.setheading(LEFT)
            self.position_locked = True

    def right(self):
        if self.head.heading() != LEFT and not self.position_locked:
            self.head.setheading(RIGHT)
            self.position_locked = True
