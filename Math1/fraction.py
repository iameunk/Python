n = int(input())

line = 0 #사선 라인
end = 0 #라인의 마지막 인덱스(1,3,6,10...)
while n > end :
    line += 1
    end += line

gap = end - n

if line % 2 == 0 :
    top = line - gap
    under = gap + 1
else :
    top = gap + 1
    under = line - gap
print(f'{top}/{under}')