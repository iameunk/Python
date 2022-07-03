n = int(input())
word = []

for i in range(n) :
    word.append(input())

set_word = list(set(word)) #set()으로 중복값 제거, 집합 자료형은 {}로 묶이므로 list()해서 []로 묶기
set_word.sort()
set_word.sort(key = len)

for i in set_word :
    print(i)