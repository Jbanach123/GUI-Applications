from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars_list = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def cars_move(self):
        for car in self.cars_list:
            car.backward(self.car_speed)
            if car.xcor() < -350:
                self.cars_list.pop(0)
                car.hideturtle()

    def create_car(self):
        self.clear()
        fate = random.randint(1, 5)
        if fate == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.cars_list.append(new_car)

    def next_level_speed(self):
        self.car_speed += MOVE_INCREMENT
