from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]

STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.list_segments = []
        self.create_snake()
        self.head = self.list_segments[0]

    def create_snake(self):
        for coord in COORDINATES:
            self.add_segment(coord)

    def add_segment(self, coord):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(coord)
        self.list_segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.list_segments[-1].position())

    def move_snake(self):
        for num_seg in range(len(self.list_segments) - 1, 0, -1):
            new_x = self.list_segments[num_seg - 1].xcor()
            new_y = self.list_segments[num_seg - 1].ycor()
            self.list_segments[num_seg].goto(new_x, new_y)

        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
