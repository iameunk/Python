N = int(input())
M = list(map(int, input().split()))
_max_ = max(M)
for i in range(N) :
    M[i] = M[i] / _max_ * 100
print("%.2f" %(sum(M)/N))
