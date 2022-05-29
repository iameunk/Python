n = int(input())
honeycomb = 1 #벌집의 개수
cnt = 1 #최소 경로
while n > honeycomb :
    honeycomb += cnt * 6
    cnt += 1
print(cnt)