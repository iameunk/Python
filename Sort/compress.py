#Xi>Xj를 만족하는 서로 다른 좌표의 개수와 같아야된다 -> Xi의 리스트 안에서의 크기 순서 출력
import sys

n = int(input())
dic = {}

num = list(map(int, sys.stdin.readline().split()))
snum = list(sorted(set(num))) #set으로 중복값 제거하고 오름차순으로 정렬 후 list로 저장

for i in range(len(snum)) :
    dic[snum[i]] = i

for j in num :
    print(dic[j], end = ' ')