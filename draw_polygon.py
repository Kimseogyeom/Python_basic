import turtle as t
def change_blue():
    global color
    color = "blue"

def change_red():
    global color
    color = "red"

def change_green():
    global color
    color = "green"

def triangle():
    global poly
    poly = 3

def square():
    global poly
    poly = 4

def pentagon():
    global poly
    poly = 5

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

def drawit(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color(color)
    draw()
    t.end_fill()

s = t.Screen()
s.onkey(change_blue, "b")
s.onkey(change_red, "r")
s.onkey(change_green, "g")
s.onkey(triangle, "3")
s.onkey(square, "4")
s.onkey(pentagon, "5")
s.onscreenclick(drawit)
s.listen()
t.mainloop()
