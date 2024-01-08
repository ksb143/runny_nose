def cal_dis(t_range, tx, ty, x, y):
    if abs(tx - x) + abs(ty - y) <= t_range:
        return True

    return False

directions = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]

T = int(input())

for test_case in range(1, T + 1):
    answer = 0
    m, a = map(int, input().split())
    a_track = [0] + list(map(int, input().split()))
    b_track = [0] + list(map(int, input().split()))

    aps = [list(map(int, input().split())) for _ in range(a)]

    ax = ay = 1
    bx = by = 10

    for i in range(m + 1):
        ax += directions[a_track[i]][0]
        ay += directions[a_track[i]][1]
        bx += directions[b_track[i]][0]
        by += directions[b_track[i]][1]

        sum_add = 0

        a_list = []
        b_list = []

        for ap_i in range(a):
            a_possible = cal_dis(aps[ap_i][2], aps[ap_i][0], aps[ap_i][1], ax, ay)
            b_possible = cal_dis(aps[ap_i][2], aps[ap_i][0], aps[ap_i][1], bx, by)

            if a_possible:
                a_list.append(ap_i)
                sum_add = max(sum_add, aps[ap_i][3])
                for bb in b_list:
                    sum_add = max(sum_add, aps[ap_i][3] + aps[bb][3])

            if b_possible:
                b_list.append(ap_i)
                sum_add = max(sum_add, aps[ap_i][3])
                for aa in a_list:
                    if aa == ap_i:
                        sum_add = max(sum_add, aps[ap_i][3])
                    else:
                        sum_add = max(sum_add, aps[ap_i][3] + aps[aa][3])

        answer += sum_add

    print(f'#{test_case} {answer}')