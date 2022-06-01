def hanoi(n,start,by,end) :
    if n == 1 :
        print(start, end) #이동할 원반 수가 1개라면 start에서 end로 이동
        return
    hanoi(n-1, start, end, by) #n-1개의 블럭을 start에서 by로 이동
    print(start, end) #마지막 원반(n번째)을 start에서 end로 이동
    hanoi(n-1, by, start, end) #by로 이동했던 n-1개의 원반을 by에서 end로 이동

n = int(input())
print(2**n - 1) #최소 이동 횟수는 2^n - 1
hanoi(n,1,2,3)