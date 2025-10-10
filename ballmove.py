from turtle import Turtle
class MoveBall(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
    def move(self):
        self.pu()
        self.left(45)
        self.fd(20)
        # if self.xcor()>=330 and self.ycor()>=280:
        #     self.pu()
        #     self.setheading(45)
        #     self.fd(20)
        # else:
        #     self.fd(20)
