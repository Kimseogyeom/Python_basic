from tkinter import *
mycolor = "black"

def paint(event):
    x1, y1 = (event.x - 1), (event.y + 1)
    x2, y2 = (event.x - 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill = mycolor)

def change_red():
    global mycolor
    mycolor = "red"

def change_blue():
    global mycolor
    mycolor = "blue"

def change_yellow():
    global mycolor
    mycolor = "yellow"

window = Tk()
canvas = Canvas(window, width=500,height=500)
canvas.pack()
canvas.bind("<B1-Motion>", paint)
button1 = Button(window, text="빨간색", command=change_red)
button2 = Button(window, text="파랑색", command=change_blue)
button3 = Button(window, text="노랑색", command=change_yellow)
button1.pack(side="left",expand = "yes", anchor="se")
button2.pack(side="left",expand = "no", anchor="s")
button3.pack(side="left",expand = "yes", anchor="sw")
window.mainloop()
