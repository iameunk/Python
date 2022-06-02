n = int(input())

if n == 1 :
    print(' ')

for i in range(2, n+1) :
    if n % i == 0 : # n을 2부터 n까지의 숫자로 나눴을 때
        while n % i == 0 : # 해당 숫자로 나누어지면 그 숫자로 나눌 수 없을 때까지 나누기
            print(i)
            n = n / i # n은 해당 숫자로 나눈 값의 몫으로 바뀜
