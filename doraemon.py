from turtle import *

setup(500,500)

speed(10)
bgcolor("black")
shape("turtle")
colormode(255)

def round(size,filled):
    pendown()
    if filled==True:
        begin_fill()
    setheading(180)
    circle(size,360)
    if filled==True:
        end_fill()

def rect(length,width,filled):
    setheading(0)
    pendown()
    if filled==True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled==True:
        end_fill()

def head():
    color("blue","blue")
    penup()
    goto(0,100)
    round(75,True)

    color("white","white")
    penup()
    goto(0,72)
    round(60,True)

def eyes():
    #left eye
    color("black","white")
    penup()
    goto(-15,80)
    round(17,True)

    #right eye
    color("black","white")
    penup()
    goto(19,80)
    round(17,True)

    #left eyeball
    color("black","black")
    penup()
    goto(-8,70)
    round(6,True)
    color("white","white")
    penup()
    goto(-8,66)
    round(2,True)

    #right eyeball
    color("black","black")
    penup()
    goto(12,70)
    round(6,True)
    color("white","white")
    penup()
    goto(12,66)
    round(2,True)

def nose():
    color("red","red")
    penup()
    goto(0,40)
    round(7,True)

def mouth():
    color("black","black")
    penup()
    goto(-30,-20)
    pendown()
    setheading(-27)
    circle(70,55)

    penup()
    goto(0,26)
    pendown()
    goto(0,-25)

def whiskers():
    color("black","black")
    penup()
    goto(10,5)
    pendown()
    goto(-40,5)
    
    penup()
    goto(10,5)
    pendown()
    goto(40,5)

    penup()
    goto(-10,15)
    pendown()
    goto(-40,20)

    penup()
    goto(10,15)
    pendown()
    goto(40,20)

    penup()
    goto(-10,-5)
    pendown()
    goto(-40,-10)

    penup()
    goto(10,-5)
    pendown()
    goto(40,-10)

def body():
    color("blue","blue")
    penup()
    goto(-50,-40)
    rect(100,80,True)

    color("white","white")
    penup()
    goto(0,-30)
    round(40,True)
    
    color("red","red")
    penup()
    goto(-60,-35)
    rect(120,10,True)

    color("white","white")
    penup()
    goto(15,-127)
    pendown()
    setheading(90)
    begin_fill()
    circle(14,180)
    end_fill()

def feet():
    #left foot
    color("black","white")
    penup()
    goto(-30,-110)
    round(20,True)
    #right foot
    color("black","white")
    penup()
    goto(30,-110)
    round(20,True)
    
def arms():
    #left arm
    color("blue","blue")
    penup()
    begin_fill()
    goto(-51,-50)
    pendown()
    goto(-51,-75)
    left(70)
    goto(-76,-85)
    left(70)
    goto(-86,-70)
    left(70)
    goto(-51,-50)
    end_fill()
    #right arm
    color("blue","blue")
    penup()
    begin_fill()
    goto(49,-50)
    pendown()
    goto(49,-75)
    left(70)
    goto(74,-85)
    left(70)
    goto(84,-70)
    left(70)
    goto(49,-50)
    end_fill()

def hands():
    #left hand
    color("black","white")
    penup()
    goto(-90,-71)
    round(15,True)
    #right hand
    color("black","white")
    penup()
    goto(90,-71)
    round(15,True)

def bell():
    color("yellow","yellow")
    penup()
    goto(0,-41)
    round(8,True)

    color("black","black")
    penup()
    goto(-10,-47)
    rect(20,4,True)

    color("black","black")
    penup()
    goto(0,-53)
    round(2,True)

def package():
    color("black","black")
    penup()
    goto(-25,-70)
    pendown()
    setheading(-90)
    circle(25,100)
    goto(-25,-70)
    hideturtle()


#####MAIN PROGRAM#####

head()
eyes()
nose()
mouth()
whiskers()
body()
feet()
arms()
hands()
bell()
package()