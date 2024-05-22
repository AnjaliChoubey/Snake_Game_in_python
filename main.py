from turtle import Turtle, Screen
import time

screen = Screen()

screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in STARTING_POSITION:
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)




screen.exitonclick()
