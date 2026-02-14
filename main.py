
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("MediumSlateBlue")
# === Square ===
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# === Dashed Line ===
for i in range(20):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.setx(i * 20)


screen = Screen()
screen.exitonclick()