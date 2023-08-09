from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.highscore = 0
        self.obtain_highscore()
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, ALIGNMENT, FONT )

    def point_obtained(self):
        self.clear()
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as highscore:
                highscore.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def obtain_highscore(self):
        with open("highscore.txt", mode="r") as highscore:
            self.highscore = int(highscore.read())
