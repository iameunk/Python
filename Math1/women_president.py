t = int(input())

for _ in range(t) :
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1,num+1)] #0층 리스트
    for k in range(floor) : #층 수만큼 반복
        for n in range(1, num) : #1부터 n-1까지
            f0[n] += f0[n-1] #층별 각 호실의 사람 수 변경
    print(f0[-1]) #마지막 값 출력