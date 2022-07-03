import math
import sys

def IsPrime(num) :
    if num == 1 :
        return False

    sq = int(math.sqrt(num))

    for i in range(2, sq+1) :
        if num % i == 0 :
            return False
    return True

m, n = map(int, input().split())
for i in range(m, n+1) :
    if isPrime(i) :
        print(i)