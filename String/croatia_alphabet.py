n = input()
alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0

for i in alphabet :
    n = n.replace(i, '*') # replace : 어떠한 값을 찾아 변경, 동일한 알파벳 찾아 *로 바꿈

print(len(n))
