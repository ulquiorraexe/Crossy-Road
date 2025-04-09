import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:  # 1 in 6 chance to create a car
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Rectangle shape for car
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))  # Random height on the screen
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.setx(car.xcor() - self.car_speed)
            if car.xcor() < -300:  # Reset car position if it moves off the screen
                car.goto(300, random.randint(-250, 250))

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT  # Increase the car speed for harder game progression
