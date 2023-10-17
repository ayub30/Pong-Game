import turtle

wn = turtle.Screen()
wn.title("Pong by @Ayub Macalim")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.shapesize(stretch_wid=5, stretch_len=1)

#Paddle
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.penup()
paddle2.goto(350, 0)
paddle2.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.shapesize()
ball.dx = 2.5  # How many pixels the ball moves by 
ball.dy = 2.5

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1 : 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))
score1 = 0
score2 = 0


#Moving up Function for paddle1
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

#Moving down Function for paddle1
def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)



#Moving up Function for paddle2
def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

#Moving down Function for paddle2
def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")


while True:
    wn.update()

    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player 1 : {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player 1 : {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))    
    
    if ball.xcor() > 340 and ((ball.ycor() < paddle2.ycor() + 50.0) and (ball.ycor() > paddle2.ycor() - 50.0)):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    