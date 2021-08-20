from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()

    def keep_score(self):
        self.write(f"Current score: {self.score} ", align="center", font=("Courier", 12, "normal"))
        self.penup()
        self.goto(0, 280)
        self.color("white")

    def update(self):
        self.score += 1

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"Game over! Your score was: {self.score} ", align="center", font=("Courier", 20, "normal"))


