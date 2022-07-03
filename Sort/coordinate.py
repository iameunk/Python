n = int(input())
nums = []

for _ in range(n) :
    nums.append(list(map(int,input().split())))

nums.sort(key = lambda x: (x[0], x[1])) #lambda 이용해서 튜플로 우선순위 정해줌, x[0]인 x줄부터 정렬하고 x[1]인 y줄 정렬

for i in nums :
    print(i[0], i[1])