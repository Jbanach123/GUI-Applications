import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create objects
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Keyboard control
screen.listen()
screen.onkeypress(player.player_move, "Up")

# Course of the game
game_is_on = True
level = 0
while game_is_on:

    time.sleep(0.1)
    cars.cars_move()
    screen.update()
    cars.create_car()

# TO MAKE IT HARDER
#    if level >= 1:
#       cars.create_car()
#    if level >= 2:
#       cars.create_car()

    # Turtle finish the level
    if player.ycor() > 280:
        scoreboard.update_scoreboard()
        player.reset_player()
        cars.next_level_speed()
        level += 1
    # Car collides player
    for car in cars.cars_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
