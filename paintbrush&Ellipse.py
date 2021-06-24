import random
from tkinter import *
from tkinter.colorchooser import*
color = "white"

def click1(key):
    display1.delete(0, END)
    display1.insert(END, key)
def click2(key):
    display2.delete(0, END)
    display2.insert(END, key)

def paint(event):
    global x1, y1
    x1, y1 = (event.x - 1), (event.y + 1)
    x2, y2 = (event.x - 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill = color)
    click2("x="+str(x1)+","+"y="+str(y1))
def draw_circle():
    i = random.randint(10,100)
    z = random.randint(10,100)
    x2, y2 = (x1-i), (y1-z)
    canvas.create_oval(x1,y1,x2,y2,fill=color)
    click2("x="+str(x1)+","+"y="+str(y1))

def change_color():
    global color
    mycolor = askcolor()
    color = mycolor[1]
    key = "색상을 "+color+"로 변경"
    click1(key)

window = Tk()
window.title("Tk")
canvas = Canvas(window, width=500,height=500)
canvas.pack()
canvas.bind("<B1-Motion>", paint)
display1=Entry(window, width=33, bg = color)
display2=Entry(window, width=33, bg = "white")
button1 = Button(window, text="색상", command=change_color)
button2 = Button(window, text="타원그리기", command=draw_circle)
display1.pack(side="left",expand = "yes", anchor="se")
button1.pack(side="left",expand = "yes", anchor="se")
display2.pack(side="left",expand = "no", anchor="s")
button2.pack(side="left",expand = "no", anchor="s")
window.mainloop()
