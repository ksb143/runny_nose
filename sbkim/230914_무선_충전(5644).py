move = {
    0: (0, 0),
    1: (-1, 0),
    2: (0, 1),
    3: (1, 0),
    4: (0, -1),
}

T = int(input())

for tc in range(1, T + 1):
    maps = [[[]] * 11 for _ in range(11)]
    # 이동시간 time, BC 개수 cnt
    time, cnt = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(1, 0)
    B = list(map(int, input().split()))
    B.insert(1, 0)
    for bc in range(1, cnt + 1):
        # BC 좌표 (X, Y), 충전 범위(C), 처리량(P)
        X, Y, C, P = map(int, input().split())
        # 충전기 범위만큼 정보 넣기 (충전기 번호, 처리량)
        AC = (bc, P)
        maps[X][Y].append(AC)
        for r in range(1, 11):
            for c in range(1, 11):
                d = abs(X - c) + abs(Y - r)
                if d <= C:
                    maps[r][c].append(AC)
    a_power = 0
    b_power = 0
    ar, ac = 1, 1
    br, bc = 10, 10
    output = 0
    for t in range(time):
        ar, ac = ar + move[A[t]][0], ac + move[A[t]][1]
        br, bc = br + move[B[t]][0], bc + move[B[t]][1]
        a_lst = maps[ar][ac]
        a_num_lst = []
        for i, j in a_lst:
            a_num_lst.append(i)
        b_lst = maps[br][bc]
        b_num_lst = []
        for i, j in b_lst:
            b_num_lst.append(i)
        ab_lst = list(set(a_lst + b_lst))
        tmax_v1 = 0
        tmax_v2 = 0
        tmax_n1 = None
        tmax_n1 = None
        for num, power in ab_lst:
            if tmax_v1 < power and num in a_num_lst:
                tmax_v1 = power
                tmax_n1 = num
            if tmax_v2 < power and num in b_num_lst:
                tmax_v2 = power
                tmax_n2 = num
        if tmax_n1 == tmax_n2:
            if len(a_lst) == len(b_lst) == 1:
                tmax_v1 //= 2
                tmax_v2 //= 2
            elif len(a_lst) > 1 or len(b_lst) > 1:
                nmax_v1 = 0
                nmax_v2 = 0
                a_num_lst.remove(tmax_n1)
                b_num_lst.remove(tmax_n2)
                for num, power in ab_lst:
                    if nmax_v1 < power and num in a_num_lst:
                        nmax_v1 = power
                        nmax_n1 = num
                    if nmax_v2 < power and num in b_num_lst:
                        nmax_v2 = power
                        nmax_n2 = num
                if nmax_v1 > nmax_v2:
                    tmax_v1 = nmax_v1
                else:
                    tmax_v2 = nmax_v2
        output += tmax_v1 + tmax_v2
    print(f'#{tc} {output}')




