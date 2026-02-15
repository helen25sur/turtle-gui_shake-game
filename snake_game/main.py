# TODO
# 1. Create a snake body
from turtle import Turtle, Screen
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
# 3. Control the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 2. Move the snake
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move_snake()

    # if list_segment[0].position() == (300, 0):
    #         game_is_on = False

# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

screen.exitonclick()