def d(n) :                                  # n = 75
    return n + sum(list(map(int,str(n))))   # return : 75 + 7 + 5

Range_num = set(range(1,10001))
Non_self_num = set()
for i in Range_num :
    Non_self_num.add(d(i))
Self_num = Range_num - Non_self_num
for i in sorted(Self_num) :
    print(i)