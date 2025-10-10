from turtle import Screen
from createpaddle import paddle
from ballmove import MoveBall
screen = Screen()
screen.tracer(0)
r_paddle = paddle((350, 0))
l_paddle = paddle((-350, 0))
d = MoveBall()
is_gameon=True
while is_gameon:
    d.move()
screen.listen()
screen.onkey(r_paddle.Up_paddle,"Up")
screen.onkey(r_paddle.Down_paddle,"Down")
screen.onkey(l_paddle.Up_paddle,"w")
screen.onkey(l_paddle.Down_paddle,"s")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.exitonclick()
