n = input()
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0

for i in dial : # 다이얼 각 요소 분리 ABC/DEF/...
    for j in i : # A/B/C
        for x in n : # 입력받은 문자 분리
            if j == x :
                time += dial.index(i) + 3
print(time)
