word = input().upper()      # word = baa
word_list = list(set(word)) # word_list = ['b','a'] (set : 중복 제거)
cnt = []

for i in word_list :        # i = b, a
    count = word.count(i)
    cnt.append(count)       # cnt = [1,3]

if cnt.count(max(cnt)) > 1 : # 최댓값이 1개보다 많으면
    print("?")
else :
    print(word_list[(cnt.index(max(cnt)))]) # index(x) : 리스트에 x값 있으면 x의 위치값 반환