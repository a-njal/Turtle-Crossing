from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NO_CAR = 1

class CarManager():
    def __init__(self):
        self.car = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def cars(self):
        random_choice = random.randint(1,6)
        if random_choice == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.car.append(new_car)

    def move_car(self):
        for car in self.car:
            car.backward(self.car_speed)

    def car_level_up(self):
        self.car_speed += MOVE_INCREMENT