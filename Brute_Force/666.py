#1666,2666,3666,4666,5666 다음은 6666이 아니고, 6660

n = int(input())
cnt = 0
num = 1

while True : # num에 1씩 더해가며 비교
    if "666" in str(num) : #num에 666이라는 숫자가 있으면 카운트하기
        cnt += 1

    if cnt == n :
        print(num)
        break
    num += 1