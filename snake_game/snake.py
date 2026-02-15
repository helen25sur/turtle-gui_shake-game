from turtle import Turtle

STEP = 20

class Snake:

    def __init__(self):
        self.list_segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(-i * STEP, 0)
            self.list_segments.append(new_turtle)

    def move_snake(self):
        for num_seg in range(len(self.list_segments) - 1, 0, -1):
            new_x = self.list_segments[num_seg - 1].xcor()
            new_y = self.list_segments[num_seg - 1].ycor()
            self.list_segments[num_seg].goto(new_x, new_y)

        self.list_segments[0].forward(STEP)