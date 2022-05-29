a, b, c = map(int, input().split())
if b >= c :
    print(-1)
else :
    print(a//(c-b)+1) #손익분기점 : C*N(수입) = A + B*N(지출)