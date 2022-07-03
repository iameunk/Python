n = int(input())

body_list = []
rank_list = []

for _ in range(n) :
    w, h = map(int, input().split())
    body_list.append((w,h)) #키와 몸무게를 튜플로 묶어서 append 해줌

for i in range(n) :
    rank = 0
    for j in range(n) :
        if body_list[i][0] < body_list[j][0] and body_list[i][1] < body_list[j][1] : #몸무게와 키가 모두 자신보다 큰 사람 수 세기
            rank += 1
    rank_list.append(rank + 1)

for i in rank_list :
    print(i, end= " ")
