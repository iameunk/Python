from itertools import combinations

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
sum_list = []

for i in combinations(num_list, 3) :
    if sum(i) > m :
        continue
    else :
        sum_list.append(sum(i))

print(max(sum_list))