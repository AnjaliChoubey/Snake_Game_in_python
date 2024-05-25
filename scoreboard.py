from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align='center', font=('Courier', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align='center', font=('Courier', 15, 'normal'))

    def check_score(self, new_score):
        self.score = new_score
        self.clear()
        self.update_scoreboard()
