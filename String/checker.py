n = int(input())
cnt = n
for i in range(0,n) :
    word = input()
    for j in range(0,len(word)-1) : #마지막 글자는 비교할 필요 없음
        if word[j] == word[j+1] :
            pass
        elif word[j] in word[j+1:] :
            cnt -= 1
            break
print(cnt)
