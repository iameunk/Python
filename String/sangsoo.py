num1, num2 = input().split()
num1 = num1[::-1] # [::-1] : 문자를 역순으로 재배치
num2 = num2[::-1]

if num1 > num2 :
    print(num1)
else :
    print(num2)