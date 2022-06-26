import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []

for _ in range(n) :
    nums.append(int(sys.stdin.readline()))

#산술평균 : 모든 숫자의 합 / n
print(round(sum(nums)/n))

#중앙값 : 오름차순으로 정렬 후 중간값
nums.sort()
print(nums[n//2])

#최빈값
cnt_nums = Counter(nums).most_common()
if len(cnt_nums) > 1 and cnt_nums[0][1] == cnt_nums[1][1] :
    #cnt_nums[0][1]은 가장 앞에 있는 최빈값의 빈도수. [1][1]은 그 다음 최빈값의 빈도수
    #이 값이 같다면 최빈값이 2개 이상
    print(cnt_nums[1][0]) #두 번째로 작은값 출력
else :
    print(cnt_nums[0][0])

#범위 : 최댓값 - 최솟값
print(max(nums)-min(nums))