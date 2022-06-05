n = int(input())
result = 0

for i in range(1, n+1) :
    a = list(map(int, str(i))) #각 자리수의 숫자를 str형으로 list에 저장
    s = i + sum(a) # 해당 숫자(1~n 중 하나)와 각 자리수의 숫자의 합을 더함
    if(s == n) : # 그 값이 n과 같다면 생성자
        result = i
        break
    else : # 생성자가 없는 경우
        result = 0

print(result)
