n = int(input())

for _ in range(n) :
    R, S = input().split()
    R = int(R)
    S = str(S)
    for i in range(len(S)) :
        print(R*S[i], end='') # end='' : 공백 없애기
    print() #줄바꿈