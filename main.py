a = int( input("초 입력:"))
hour = a // 3600
min = (a % 3600) // 60
sec = a % 60
print(a,'초는', hour,'시간', min, '분', sec, '초 입니다.')
