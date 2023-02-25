from turtle import Turtle

class Paddle(Turtle):
    def __init__(self , taple_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(taple_position)


    def go_up(self):
        new_y_position = self.ycor() + 20
        self.goto(self.xcor(), new_y_position)


    def go_down(self):
        new_y_position = self.ycor() - 20
        self.goto(self.xcor(), new_y_position)

