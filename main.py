
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("MediumSlateBlue")
# === Square ===
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# === Dashed Line ===
# for i in range(20):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.setx(i * 20)

# === Different Shapes ===
import random

colours = ["Indigo", "Purple", "MediumPurple", "DarkSlateBlue", "SlateBlue", "MediumSlateBlue", "Plum"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for i in range(3, 11):
    timmy_the_turtle.color(random.choice(colours))
    draw_shape(i)

screen = Screen()
screen.exitonclick()