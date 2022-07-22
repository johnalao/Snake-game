from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # CONSTANTS
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for positions in INITIAL_POSITIONS:
            self.add_body(positions)

    def add_body(self, positions):
        new_body = Turtle("square")
        new_body.color("black")
        new_body.penup()
        new_body.goto(positions)
        self.body.append(new_body)

    def extend(self):
        self.add_body(self.body[-1].position())

    def reset(self):
        for objects in self.body:
            objects.goto(900, 950)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def move(self):
        for parts in range(len(self.body) - 1, 0, -1):
            new_x = self.body[parts - 1].xcor()
            new_y = self.body[parts - 1].ycor()
            self.body[parts].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
