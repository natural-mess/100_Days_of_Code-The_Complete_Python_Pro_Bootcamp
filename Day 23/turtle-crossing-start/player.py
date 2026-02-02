from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Class to manage player"""
    def __init__(self):
        super().__init__(shape="turtle")
        self._create_player()

    def _create_player(self):
        """Initialize player"""
        self.penup()
        self.start_position()
        self.setheading(90)

    def move(self):
        """Move player forward"""
        self.forward(MOVE_DISTANCE)

    def start_position(self):
        """When a level is completed, move the turtle back to starting position"""
        self.goto((STARTING_POSITION))
