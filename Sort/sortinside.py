n = int(input())
num = []

for _ in str(n) :
    num = list(map(int,str(n))) #문자열 n을 정수형으로 바꾸고 list에 각각 저장하기

num.sort(reverse = True) #내림차순 정렬

for i in num :
    print(i, end = '') #end = '' : 한 줄로 출력