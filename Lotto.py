import random

def input_Num(list):
    for i in range(0,6):
        if list[i] != 0:
            continue
        num = int(input("%d번째 자리의 번호를 입력해주세요(1~45):" %(i+1)))
        if num < 1 or num > 45:
            print("1번부터 45번까지만 입력해주세요")
            return input_Num(list)
        for j in list:
            if j == num:
                print("중복되는 번호입니다. 다시입력해주세요")
                return input_Num(list)
        list[i] = num
    return list
def lottery():
    result = 0
    choice_li = [0] * 6
    Num_li = []
    while len(Num_li) < 6:
        num_Random = random.randint(1,45)
        if num_Random not in Num_li:
            Num_li.append(num_Random)
    choice_li=input_Num(choice_li)
    Num_li.sort()
    choice_li.sort()
    for i in choice_li:
        for j in Num_li:
            if i == j:
                result+=1
    print("내가 선택한 번호:",choice_li)
    print("당첨된 번호:",Num_li)
    print("%d개의 번호가 당첨되었습니다."%result)

lottery()