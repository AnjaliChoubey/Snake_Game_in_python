from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
