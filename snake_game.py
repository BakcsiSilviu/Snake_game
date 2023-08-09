from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from playside import PlaySide

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

playside = PlaySide()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_body_movement()

    if snake.snake_head.distance(food) < 15:
        food.spawn_food()
        scoreboard.point_obtained()
        snake.extend()
    
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.snake_length[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    
screen.exitonclick()