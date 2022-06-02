n = int(input())
numbers = map(int, input().split())
sosu = 0

for num in numbers :
    error = 0
    if num > 1 :
        for i in range(2,num) : # num을 1과 자기 자신을 제외한 나머지 숫자 (2~n-1)
            if num % i == 0 : #로 나누었을 때 나누어진다면 소수 아님
                error += 1
        if error == 0 :
            sosu += 1

print(sosu)

