import turtle as t
from tkinter.colorchooser import*

def change_color():
    global color
    color = askcolor()
    color = color[1]

def triangle():
    global poly
    poly = 3

def square():
    global poly
    poly = 4

def pentagon():
    global poly
    poly = 5

def hexagon():
    global poly
    poly = 6

def draw():
    if poly == 3:
        for i in range(3):
            t.forward(100)
            t.left(120)
    elif poly == 4:
        for i in range(4):
            t.forward(100)
            t.left(90)
    elif poly == 5:
        for i in range(5):
            t.forward(100)
            t.left(72)
    elif poly == 6:
        for i in range(6):
            t.forward(100)
            t.left(60)

def drawit(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color(color)
    draw()
    t.end_fill()

def nofill():
    t.undo()

def reset():
    t.reset()

s = t.Screen()
s.onkey(change_color, "c")
s.onkey(triangle, "3")
s.onkey(square, "4")
s.onkey(pentagon, "5")
s.onkey(hexagon, "6")
s.onkey(nofill, "d")
s.onkey(reset, "r")
s.onscreenclick(drawit)
s.listen()
t.mainloop()
