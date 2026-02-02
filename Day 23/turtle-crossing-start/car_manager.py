from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
LANES = list(range(-230, 250 + 10, 50))
MIN_CARS_DISTANCE = 110
COOLDOWN_SPAWN = 0.5

class CarManager():

    def __init__(self):
        self.car_active = []
        self.car_recycled = []

        # Cooldown time, time gap 
        self.cooldown = COOLDOWN_SPAWN
        self.last_spawn = time.time()

        # Min distance between 2 cars
        self.min_cars_distance = MIN_CARS_DISTANCE

        self.car_speed = STARTING_MOVE_DISTANCE

    def _car_create(self, y_pos):
        """Create car"""
        car = Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=3)
        car.penup()
        car.setheading(180)
        car.goto((300, y_pos))
        return car
    
    def _cooldown_time(self):
        """Check if time is long enough to spawn new car"""
        now = time.time()
        if now - self.last_spawn < self.cooldown:
            return False
        else:
            self.last_spawn = now
            return True

    def _car_distance(self, y_pos):
        """Check on the same y lane if the distance of the active car is far enough to spawn new car"""
        for car in self.car_active:
            if car.ycor() == y_pos and (300 - car.xcor()) < self.min_cars_distance:
                return False
        return True

    def _recycle_car(self, car):
        self.car_recycled.append(car)
        car.hideturtle()
        car.goto(1000, 1000)

    def car_spawn(self):
        """Generate new car or reuse recycled car"""
        # Return when cooldown time is not reached
        if not self._cooldown_time():
            return
        
        # Return when distance between old and new car in the same line is not reached
        y_pos = random.choice(LANES)
        if not self._car_distance(y_pos):
            return

        # If cooldown and distance conditions are satisfy
        # Check if we have any recycle car, if not create one, else, reuse from recycle
        if not self.car_recycled:
            self.car_active.append(self._car_create(y_pos))
        else:
            car = self.car_recycled.pop()
            car.goto(340, y_pos)
            car.showturtle()
            self.car_active.append(car)

    def car_move_reuse(self):
        """Move car forward. Put cars in recycle if it moves out of left frame"""
        car_active_copy = []
        for car in self.car_active:
            car.forward(self.car_speed)
            if car.xcor() < -340:
                self._recycle_car(car)
            else:
                car_active_copy.append(car)
        self.car_active = car_active_copy

    def car_reset_level(self):
        """Increase difficulty when a level is completed"""
        # for car in self.car_active:
        #     self._recycle_car(car)
        # self.car_active.clear()
        self.car_speed += MOVE_INCREMENT
        self.cooldown *= 0.9

