import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing game")
screen.tracer(0)
timmy = Player()
game_on = True
cars_control = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(timmy.move_upwards, "Up")

while game_on:

    time.sleep(0.1)
    screen.update()
    cars_control.create_cars()
    cars_control.move_cars()

#     Detect car collision
    for cars in cars_control.all_cars:
        if timmy.distance(cars) < 20 :
            scoreboard.game_over()
            game_on = False

#     Cross finish line
    if timmy.cross_finish_line():
        timmy.start_position()
        cars_control.level_up()
        scoreboard.add_score()






screen.exitonclick()