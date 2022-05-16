n = int(input())
m = list(map(int, input().split()))
_max_ = max(m)
for i in range(n) :
    m[i] = m[i] / _max_ * 100
print("%.2f" %(sum(m)/n))
