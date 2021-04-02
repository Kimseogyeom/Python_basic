#돈을 넣고 물건값을 입력하고 거스름돈을 주는 프로그램
def checkmoney(money, price):
    while(True):
        money2=int(input("돈이 부족합니다. 돈을 더 넣어주세요:"))
        money += money2
        if(money < price):
            return checkmoney(money, price)
        else:
            return money, price
while(True):
    money=int(input("돈을 넣어주세요:"))
    if(money >9):
        price=int(input("물건값을 입력해주세요:"))
        if(price <=0):
            print("물건 값이 옳지 않습니다. 처음부터 다시 시작하겠습니다.")
        elif(price > money):
            money, price=checkmoney(money, price)
            break;
        else:
            break;
    else:
        print("돈을 넣지 않으셨습니다. 10원 이상의 돈을 넣어주세요")
change = money - price
a = change/500
b = (change%500) / 100
c = (change%100) /50
d = (change%50) / 10
print("잔돈은 500원:%d개, 100원:%d개, 50원:%d개, 10원:%d개"%(a,b,c,d))