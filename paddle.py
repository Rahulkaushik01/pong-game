from turtle import Turtle, Screen
screen = Screen()
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pads = []

        self.shape('square')
        self.color('white')
        self.penup()
        self.screen.tracer(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)




    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def go_up1(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down1(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)