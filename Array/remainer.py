# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
N = []
for i in range(10) :
    n = int(input())
    N.append(n % 42) #입력 값의 나머지를 배열에 저장
N = set(N) #set() : 중복 제거
print(len(N))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
