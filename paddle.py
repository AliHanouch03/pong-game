from turtle import Turtle

DESIRED_WIDTH = 20 #pixels
DESIRED_HEIGHT = 100 #pixels
BASE_SIZE = 20 #pixels # that is the initial size of the turtle 20x20 pixels
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        self.stretch_wid = DESIRED_HEIGHT / BASE_SIZE
        self.stretch_len = DESIRED_WIDTH / BASE_SIZE
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=self.stretch_wid, stretch_len=self.stretch_len)

    def move_up(self):
        if self.ycor() < 245:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)






