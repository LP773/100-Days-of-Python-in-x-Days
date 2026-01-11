from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

player1_paddle = Paddle(x_cor=-360, y_cor=0)
player2_paddle = Paddle(x_cor=350, y_cor=0)
pong = Ball()

screen.listen()
screen.onkey(player1_paddle.move_w, "w")
screen.onkey(player1_paddle.move_s, "s")
screen.onkey(player2_paddle.move_up, "Up")
screen.onkey(player2_paddle.move_down, "Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    pong.move()

    # Detect Ball Collision
    if pong.ycor() > 280 or pong.ycor() < -275:
        # Bounce
        pong.bounce_y()

    # Detect Collision with Paddles
    if pong.distance(player2_paddle) < 50 and pong.xcor() > 325 or pong.distance(player1_paddle) < 50 and pong.xcor() < -335:
        pong.bounce_x()

screen.exitonclick()
