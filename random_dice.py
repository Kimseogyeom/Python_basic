import random

def dice():
    a = random.randint(1,6)
    b = random.randint(1,6)
    print("첫번째 주사위: %d 두번째 주사위: %d" %(a,b))


dice()