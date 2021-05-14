import turtle as t

def make_block(block):
    if block == "사각형":
        x = int(input("가로의 길이를 입력하세요:"))
        y = int(input("세로의 길이를 입력하세요:"))
        t.forward(x)
        t.left(90)
        t.forward(y)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(y)
    elif block == "삼각형":
        x = int(input("하나의 변의 길이를 입력해주세요:"))
        t.forward(x)
        t.left(120)
        t.forward(x)
        t.left(120)
        t.forward(x)
    elif block == "원":
        x = int(input("반지름을 입력해주세요:"))
        t.circle(x)
    t.mainloop()
t.shape("turtle")
input_block = input("도형을 입력하시오: ")
make_block(input_block)
