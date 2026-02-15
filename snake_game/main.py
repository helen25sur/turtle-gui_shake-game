# TODO
# 1. Create a snake body
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

list_segment = []

for i in range(3):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(-i*20, 0)
    list_segment.append(new_turtle)

# 2. Move the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)
    for num_seg in range(len(list_segment) - 1, 0, -1):
        new_x = list_segment[num_seg - 1].xcor()
        new_y = list_segment[num_seg - 1].ycor()
        list_segment[num_seg].goto(new_x, new_y)

    list_segment[0].forward(20)

    if list_segment[0].position() == (300, 0):
            game_is_on = False

# 3. Control the snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

screen.exitonclick()