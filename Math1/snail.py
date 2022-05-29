import math

a, b, v = map(int, input().split())
day = (v - b) / (a - b)
print(math.ceil(day)) #math.ceil() : 소수점 올림 함수