def check_division(num):
    if num%6==0:
        print("2와 3으로 나누어 떨어집니다.")
    elif num%2==0 and num%3!=0:
        print("2로는 나누어 떨어지나 3으로는 안나누어 떨어집니다.")
    elif num%2!=0 and num%3==0:
        print("3으로 나누어 떨어지나 2로는 안나누어 떨어집니다.")
    else:
        print("2 와 3으로 안나누어 떨어집니다.")

check_division(int(input("정수 하나를 입력해주세요: ")))