from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with wall
    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -285 or snake.segments[0].ycor() > 285 or \
            snake.segments[0].ycor() < -285:
        is_game_on = False
        score.game_over()

    # detect colision with food
    if snake.segments[0].distance(food) < 10:
        food.refersh()
        snake.extend()
        new_score = score.score+1
        score.check_score(new_score)

    #detect collision with tail
    for index in snake.segments[1:]:
        if snake.segments[0].distance(index) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
