from turtle import Turtle


class paddle(Turtle):

    def __init__(self,position):
            super().__init__()
            self.name = Turtle()
            self.color("white")
            self.shape("square")
            self.shapesize(stretch_wid=5, stretch_len=1)
            self.pu()
            self.goto(position)
        
    def Up_paddle(self):
        self.new_y=self.ycor()+20
        self.goto(self.xcor(), self.new_y)
        self.screen.update()
    def Down_paddle(self):

        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
        self.screen.update()