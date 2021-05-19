items ={ "우유":1, "종이컵":2, "책":5, "커피음료":7, "콜라":4, "펜":3}

while(True):
    flag = 0
    print("=======================")
    print("       물품 목록")
    print("=======================")
    for i in items:
        print(i,":",items[i])
    print("=======================")
    print("물품 목록 구매나 보충 선택 ---> 구매:1, 보충:2, quit:0")
    Num=input("원하는 번호를 선택하세요 -->")
    if Num == '1':
        Item=str(input("구매할 물품의 이름을 입력하세요: "))
        for i in items:
            if Item == i:
                flag = 1
                Count=int(input("구매 수량을 입력하세요: "))
                if items[Item] < Count:
                    print(Item,"--> 재고량이 부족해서 ",items[Item],"개만 구매함")
                    items[Item] = 0
                elif items[Item] >= Count:
                    print(Item,"-->",Count,"개 구매완료")
                    items[Item]-= Count
        if flag == 0:
            print("물품이 없습니다.")
    elif Num == '2':
        Item = str(input("보충할 물품의 이름을 입력하세요: "))
        for i in items:
            if Item == i:
                flag = 1
                Count = int(input("보충 수량을 입력하세요: "))
                items[Item] += Count
        if flag == 0:
            print("물품이 없습니다.")
    elif Num == 'quit':
        break
    else:
        print("잘못입력하셨습니다 다시 입력해주세요.")