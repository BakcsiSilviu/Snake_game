from turtle import Turtle

STARTING_POINTS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE_MOVED = 20

class Snake:
# Initialise the snake spawn point and the snakes body.
    def __init__(self):
        self.snake_length = []
        self.create_snake()
        self.snake_head = self.snake_length[0]

    def create_snake(self):
        for position in STARTING_POINTS:
            self.add_segment(position)

    def snake_body_movement(self):
        for segment in range(len(self.snake_length) -1, 0, -1):
            new_x = self.snake_length[segment - 1].xcor()
            new_y = self.snake_length[segment - 1].ycor()
            self.snake_length[segment].goto(new_x, new_y)
        self.snake_head.forward(DISTANCE_MOVED)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)
    
    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def add_segment(self, position):
        self.segment = Turtle("square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.goto(position)
        self.snake_length.append(self.segment)

    def extend(self):
        self.add_segment(self.snake_length[-1].position())
        
    def reset(self):
        for segment in self.snake_length:
            segment.goto(1000, 100)
        self.snake_length.clear()
        self.create_snake()
        self.snake_head = self.snake_length[0]