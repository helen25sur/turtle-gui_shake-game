from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)