from turtle import Screen, Turtle
from paddle import Paddle
from ff import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
turtle = Turtle()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong Game')
# y = 0
# for r in range(0,5):
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

# screen.tracer(0)

screen.listen()


screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

screen.onkey(r_paddle.go_up1, 'Up')
screen.onkey(r_paddle.go_down1, 'Down')
# screen.onkey(go_down, 'down')


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce1()
    if ball.xcor() > 380:
        score.score1()
        ball.ball_back()
    if ball.xcor() < -380:
        ball.ball_back()
        score.score2()


screen.exitonclick()