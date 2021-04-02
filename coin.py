import turtle as t
import random
screen = t.Screen()
image1= "front.gif"
image2= "back.gif"
screen.addshape(image1)
screen.addshape(image2)

while(True):
    x = input("계속해서 동전을 뒤집을려면 space 나가고 싶으면 cltr+z를 눌러주세요: ")
    if 32 == ord(x):
        coin = random.randint(0,1)
        if coin == 0:
            t.shape(image1)
            t.stamp()
        else:
            t.shape(image2)
            t.stamp()
    else:
        break