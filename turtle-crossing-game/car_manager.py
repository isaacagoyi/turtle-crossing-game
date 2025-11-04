from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_speed = random.randint(1, 6)
        if random_speed == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1, 2)
            y_location = random.randint(-250, 250)
            car.goto(300, y_location)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
