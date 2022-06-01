def draw_star(n) :
    if n == 1 :
        return ['*']

    Stars = draw_star(n//3)
    L = []

    for star in Stars : #위쪽 공간
        L.append(star*3)
    for star in Stars : #중간 공간
        L.append(star + ' '*(n//3) + star)
    for star in Stars : #아래쪽 공간
        L.append(star*3)

    return L

n = int(input())
print('\n'.join(draw_star(n))) #'구분자'.join(리스트) : 리스트 값과 값 사이에 구분자(\n) 넣어서 하나의 문자열로 합침