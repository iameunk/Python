n = int(input())
for i in range(n) :
    cnt = 0
    sum = 0
    a = list(input())
    for i in a :
        if i == 'O' :
            cnt += 1
            sum += cnt
        else :
            cnt = 0
    print(sum)
