from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("deep sky blue")
screen.title("My Snake Game")
screen.tracer(0)

# Choose difficulty
difficult = screen.textinput(title="Snake Game", prompt="Choose difficulty level. Type 'eazy' or 'hard' : ")

# Creating objets
snake = Snake()
food = Food()
scoreboard = Scoreboard(difficult)

# Keyboard control
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Course of the game
game_is_on = True
time_sleep = 0.15
while game_is_on:
    time.sleep(time_sleep)
    snake.move()
    screen.update()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        # Getting faster (level hard)
        if difficult == "hard":
            time_sleep -= 0.005

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290: # 280
        time_sleep = 0.15
        scoreboard.reset()
        snake.reset()
        # Comment these 2 lines to auto-restart after lost
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            time_sleep = 0.15
            scoreboard.reset()
            snake.reset()
            # Comment these 2 lines to auto-restart after lost
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
