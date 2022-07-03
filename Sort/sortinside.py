n = int(input())
nums = []

for _ in str(n) :
    nums = list(map(int,str(n))) #문자열 n을 정수형으로 바꾸고 list에 각각 저장하기

nums.sort(reverse = True) #내림차순 정렬

for i in nums :
    print(i, end = '') #end = '' : 한 줄로 출력