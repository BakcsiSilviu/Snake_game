from turtle import Turtle

class PlaySide(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-290,-290)
        self.pendown()
        self.draw_playside()

    def draw_playside(self):
        for _ in range(4):
            self.forward(580)
            self.left(90)