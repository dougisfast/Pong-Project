# Simple pong game
# Doug snow
# Part 1

import turtle
import time

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len= 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len= 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = -0.1
ball.dy = 0.1

# Score
p1_score = 0
p2_score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,280)
pen.write(f"Player 1: {p1_score}    Player 2: {p2_score}", align="center", font=("Courier New",11,"normal"))

# End Game
end_game = turtle.Turtle()
end_game.hideturtle()
end_game.color("white")
end_game.penup()
end_game.goto(0,0)
end_game.write(" ")

# Functions!
def paddle_a_up():
    if(paddle_a.ycor() < 250):
        y = paddle_a.ycor()
        y += 20 #adds 20 pixel to y coordinate
        paddle_a.sety(y)

def paddle_a_down():
    if (paddle_a.ycor() > -240):
        y = paddle_a.ycor()
        y -= 20 # subtracts 20 pixels from y coordinate
        paddle_a.sety(y)
    
def paddle_b_up():
    if (paddle_b.ycor() < 250):
         y = paddle_b.ycor()
         y += 20 #adds 20 pixel to y coordinate
         paddle_b.sety(y)

def paddle_b_down():
    if (paddle_b.ycor() > -240):
        y = paddle_b.ycor()
        y -= 20 # subtracts 20 pixels from y coordinate
        paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
game_over = False
while game_over == False:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        p1_score += 1 
        pen.clear()
        pen.write(f"Player 1: {p1_score}    Player 2: {p2_score}", align="center", font=("Courier New",11,"normal"))
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor() < -390:
        p2_score += 1 
        pen.clear()
        pen.write(f"Player 1: {p1_score}    Player 2: {p2_score}", align="center", font=("Courier New",11,"normal"))
        ball.goto(0,0)
        ball.dx *= -1

    # Paddle & Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        ball.dx *= -1

    # End Game Condition
    if p1_score > 4:
        end_game.clear()
        end_game.write(f"Congratulations Player 1, you won!", align= "center", font=("Courier New",11,"normal"))


    if p2_score > 4:
        end_game.clear()
        end_game.write(f"Congratulations Player 2, you won!", align= "center", font=("Courier New",11,"normal"))


 



