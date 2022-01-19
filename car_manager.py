import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 6:
            car = t.Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            car.goto(300,random_y)
            self.all_cars.append(car)
    
    def move_car(self):
        for car in self.all_cars:
            car.bk(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT