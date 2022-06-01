def draw_star(n) :
    if n == 1 :
        return ['*']

    Stars = draw_star(n//3)
    L = []

    for star in Stars :
        L.append(star*3)
    for star in Stars :
        L.append(star + ' '*(n//3) + star)
    for star in Stars :
        L.append(star*3)

    return L

n = int(input())
print('\n'.join(draw_star(n))) #구분자.join() : 리스트 값과 값 사이에 구분자(\n) 넣어서 문자열로 합침
