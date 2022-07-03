n = int(input())
member = []

for i in range(n) :
    age, name = map(str, input().split()) #나이와 이름을 각각 입력받기
    age = int(age)
    member.append((age,name)) #(age, name) 형태로 member에 저장

member.sort(key = lambda x : x[0])

for i in member :
    print(i[0], i[1])

#파이썬은 안정(stable) 정렬. 안정 정렬 : 입력 받은 값들 중에 같은 값이 있는 경우 해당 값의 순서를 그대로 유지
# [1, 2, 3(X), 4, 5, 3(Y)] -> [1, 2, 3(X), 3(Y), 4, 5] (o) [1, 2, 3(Y), 3(X), 4, 5] (x)