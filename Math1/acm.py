t = int(input())

for _ in range(t) :
    h, w, n = map(int, input().split())
    floor = n % h
    num = (n // h) + 1

    if floor == 0 : #나머지가 0일 때 꼭 고려하기
        floor = h
        num -= 1

    print(f'{floor*100+num}')