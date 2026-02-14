# import colorgram
#
# count_of_color = 30
# colors = colorgram.extract('image.jpg', count_of_color)
# ready_colors = []
#
# for i in range(count_of_color):
#     color = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
#     ready_colors.append(color)
#
# print(ready_colors)

from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

screen = Screen()
screen.colormode(255)

color_list = [(228, 227, 226), (246, 237, 243), (243, 244, 246), (234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117), (225, 76, 115), (163, 166, 35), (28, 35, 84), (227, 86, 43), (42, 166, 208), (120, 172, 116), (119, 102, 158), (215, 64, 33), (237, 244, 241), (39, 52, 100), (76, 21, 45), (229, 169, 188), (14, 99, 71), (31, 61, 56), (8, 92, 107), (222, 177, 169), (181, 188, 208), (171, 203, 193)]

timmy_the_turtle.setheading(225)
timmy_the_turtle.penup()
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy_the_turtle.pendown()
    timmy_the_turtle.dot(20, random.choice(color_list))
    timmy_the_turtle.penup()
    timmy_the_turtle.hideturtle()
    timmy_the_turtle.forward(50)

    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)

screen.tracer(0)

screen.exitonclick()

