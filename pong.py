# Simple pong game

import turtle
import winsound
import sys
# The window of the game
win = turtle.Screen()
win.title("Pong made by Aichi")
win.bgcolor("black")
win.setup(width=800, height=600)

# Stops the window from refreshing
win.tracer(0)

# Score
scoreA = 0
scoreB = 0


# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0   Player B: 0", align="center",
          font=("Courier", 24, "normal"))


def paddleAUp():
    # A function to move the paddle
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleADown():
    # A function to move the paddle
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleBUp():
    # A function to move the paddle
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleBDown():
    # A function to move the paddle
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard binding
win.listen()
win.onkeypress(paddleAUp, "w")
win.onkeypress(paddleADown, "s")
win.onkeypress(paddleBUp, "Up")
win.onkeypress(paddleBDown, "Down")


# Main game loop
while True:
    # Update the screen
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # winsound.PlaySound('bounce.wav',winsound.SND_FILENAME)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A : {}   Player B: {}".format(scoreA, scoreB), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < - 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A : {}   Player B: {}".format(scoreA, scoreB), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # win.update()
