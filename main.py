from turtle import Screen
from paddle import Paddle
import time
from ball import Ball

R_PADDLE_INITIAL_POSITION = (350, 0)
L_PADDLE_INITIAL_POSITION = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.tracer(0)

# create paddles
r_paddle = Paddle(R_PADDLE_INITIAL_POSITION)
l_paddle = Paddle(L_PADDLE_INITIAL_POSITION)

# create a ball object
ball = Ball()

# control paddles
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')



game_is_on = True
while game_is_on:
    time.sleep(0.1)  # makes the screen slows down before updating
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()
