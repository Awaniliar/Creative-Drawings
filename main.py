from turtle import *

t = Turtle()
t.color('black')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(0)

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

#colors_functions
def setCrimson():
    t.color('red')

def setViolet():
    t.color('violet')

def setBlack():
    t.color('black')

def setLime():
    t.color('lime')

def setPink():
    t.color('pink')
    
def setAqua():
    t.color('aqua')

def setDarkRed():
    t.color('darkred')

#straight.lines_funtions
def setRight():
    t.goto(t.xcor() + 20, t.ycor())

def setLeft():
    t.goto(t.xcor() - 20, t.ycor())

def setUp():
    t.goto(t.xcor(), t.ycor() + 20)

def setDown():
    t.goto(t.xcor(), t.ycor() - 20)

#fill_funtions
def setBegin_fill():
    t.begin_fill()

def setEnd_fill():
    t.end_fill()

scr = t.getscreen()
scr.listen()

#colors
scr.onkey(setCrimson, 'c')
scr.onkey(setViolet, 'v')
scr.onkey(setBlack, 'b')
scr.onkey(setPink, 'p')
scr.onkey(setLime, 'l')
scr.onkey(setAqua, 'a')
scr.onkey(setDarkRed, 'd')

#move
scr.onkey(setRight, 'Right')
scr.onkey(setLeft, 'Left')
scr.onkey(setUp, 'Up')
scr.onkey(setDown, 'Down')

#fill
scr.onkey(setBegin_fill, 'e')
scr.onkey(setEnd_fill, 'r')

#click
scr.onscreenclick(move)
t.ondrag(draw)
