T = int(input())
di = [0,-1,0,1,0]
dj = [0,0,1,0,-1]

for tc in range(1, T+1):
    M, A = map(int, input().split())
    a_move = list(map(int, input().split())) + [0]
    b_move = list(map(int, input().split())) + [0]
    arr = [[[0] for i in range(11)] for _ in range(11)]
    bc = [0]
    for b in range(A):
        x, y, c, p = map(int, input().split())
        bc.append(p)
        for i in range(x-c, x+c+1):
            for j in range(y-c, y+c+1):
                if 1 <= i <= 10 and 1 <= j <= 10:
                    if abs(i - x) + abs(j - y) <= c:
                        arr[j][i].append(b+1)

    x1, y1 = 1, 1
    x2, y2 = 10, 10
    sum_v = 0

    for i in range(M+1):
        a_now = arr[x1][y1]
        b_now = arr[x2][y2]
        max_v = 0
        for a in a_now:
            for b in b_now:
                if a == b:
                    if max_v < bc[a]:
                        max_v = bc[a]
                else:
                    if max_v < bc[a] + bc[b]:
                        max_v = bc[a] + bc[b]
        sum_v += max_v
        x1, y1 = x1 + di[a_move[i]], y1 + dj[a_move[i]]
        x2, y2 = x2 + di[b_move[i]], y2 + dj[b_move[i]]

    print(f'#{tc} {sum_v}')