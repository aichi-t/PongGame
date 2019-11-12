# Simple pong game

import turtle

# The window of the game
win = turtle.Screen()
win.title("Pong made by Aichi")
win.bgcolor("black")
win.setup(width=800, height=600)

# Stops the window from refreshing
win.tracer(0)

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
ball.dx = 0.5
ball.dy = -0.5


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

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
