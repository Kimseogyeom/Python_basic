import random

def create_practice():
    ra_li=[random.randint(1, 100) for i in range(2)]
    if ra_li[0] >= ra_li[1]:
        print("문제: %d - %d = "%(ra_li[0],ra_li[1]))
        check_result(ra_li[0]-ra_li[1])
    else:
        print("문제: %d - %d = ??" %(ra_li[1],ra_li[0]))
        check_result(ra_li[1]-ra_li[0])

def check_result(result):
    x = int(input("정답을 입력해주세요: "))
    if(result == x):
        print("정답입니다.")
    else:
        print("틀렸습니다.")
        return check_result(result)

create_practice()