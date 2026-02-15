# TODO
# 1. Create a snake body
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

list_segment = []

for i in range(3):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.goto(-i*20, 0)
    list_segment.append(new_turtle)

# 2. Move the snake
# 3. Control the snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

screen.exitonclick()