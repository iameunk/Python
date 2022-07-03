n = int(input())
num = []

for i in str(n) :
    num.append(int(i)) #문자열 각 자리를 정수형으로 바꿔 num에 저장

num.sort(reverse = True) #내림차순 정렬

for i in num :
    print(i, end = '') #end = '' : 한 줄로 출력