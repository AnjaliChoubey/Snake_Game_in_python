from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
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
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or \
            snake.head.ycor() < -285:
        is_game_on = False
        score.game_over()

    # detect colision with food
    if snake.head.distance(food) < 10:
        food.refersh()
        snake.extend()
        new_score = score.score+1
        score.check_score(new_score)

    #detect collision with tail
    for index in snake.segments[1:]:
        distance = snake.head.distance(index)
        if distance < 7:
            is_game_on = False
            score.game_over()

screen.exitonclick()
