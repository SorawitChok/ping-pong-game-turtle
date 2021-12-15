import turtle as t
import time
import random as r

# set up the background
t.bgcolor("black")
t.title("Ping Pong Game Python V.1")
c = ["silver","pink","violet","springgreen","lightskyblue","crimson","magenta","gold","lightcoral","cyan"]

# set up the pad 
t.hideturtle()
t.pu()
t.goto(0,-270)
t.showturtle()
t.shape("square")
t.shapesize(1,4)
pad_speed = 30
n = 0
i = r.randint(0,8)

#set up ball
ball = t.Turtle()
ball.pu()
ball.shape("circle")
bsx = 8
bsy = 10
bx = ball.xcor()
by = ball.ycor()

#set up game over
w = t.Turtle()
w.color("red")
w.hideturtle()

#set up score count
p = t.Turtle()
p.color("white")
p.hideturtle()
p.pu()
p.goto(0,300)

# defined function
def right():
    x = t.xcor()
    x += pad_speed
    t.setx(x)
    if x >= 300:
        t.setx(300)
    
def left():
    x = t.xcor()
    x -= pad_speed
    t.setx(x)
    if x <= -300:
        t.setx(-300)
        
# main body
t.listen()
t.onkey(right,"Right")
t.onkey(left,"Left")

ball.seth(60)

while True:
    t.color(c[i+1])
    ball.color(c[i])
    bx += bsx
    by += bsy
    ball.setpos(bx,by)
    if by == -250 and t.xcor() - 50 < bx < t.xcor() + 50 :
        bsy *= -1 ; n += 1 ; i += 1 
        if i > 8 : i=0
    if bx >= 300 or bx <= -300: bsx *= -1
    if by >= 300 : bsy *= -1
    if by <= -300 : t.bgcolor("red");time.sleep(0.1);t.bgcolor("black"); w.write("Game Over",move=False,align = "center",font=("Arial",64,"normal")); break
    t.tracer(0)
    p.clear()
    p.write("Point : %d" %n,False,align = "center",font=("Arial",16,"normal"))
    time.sleep(0.025)
    t.update()

    











    

