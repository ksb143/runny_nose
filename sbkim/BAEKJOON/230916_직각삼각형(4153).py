while True:
    lst = list(map(int, input().split()))
    # 마지막 테스트일 경우 while 문 멈추기
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    # 주어진 input 값에서 최대 값 및 해당 인덱스 찾기
    max_num = 0
    max_idx = 0
    for i in range(3):
        if lst[i] > max_num:
            max_num = lst[i]
            max_idx = i
    # 최대 값에 해당하는 인덱스 분리해서 제곱하기
    heru = 0
    rest = 0
    for j in range(3):
        if j == max_idx:
            heru = lst[i] ** 2
        else:
            rest += lst[i] ** 2
    # 직각 삼각형 검사
    if heru == rest:
        print('rignt')
    else:
        print('wrong')


while True:
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        print('right')
    else:
        print('wrong')




