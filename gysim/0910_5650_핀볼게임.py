def pinball(start, d):
    global max_v

    cnt = 0  # 점수
    r, c = start

    while True:
        r, c = r + delta[d][0], c + delta[d][1]

        if 0 <= r < N and 0 <= c < N:
            # 핀볼이 출발위치로 돌아오거나, 블랙홀에 빠질 때 끝남
            if (r, c) == start or board[r][c] == -1:
                if cnt > max_v:
                    max_v = cnt
                return

            # 점수는 벽이나 블록에 부딪힌 횟수 (웜홀 제외)
            if 1 <= board[r][c] <= 5:
                cnt += 1
                d = direc[board[r][c]][d]

            # 웜홀에 빠지면 같은 번호를 가진 웜홀로 빠져나오고 진행방향 유지
            elif 6 <= board[r][c] <= 10:
                r, c = wormhole_info[(r, c)]
                # for k in range(len(wormhole)):
                #     if board[r][c] == wormhole[k][0] and (r, c) != (wormhole[k][1], wormhole[k][2]):
                #         r, c = wormhole[k][1], wormhole[k][2]

        else:   # 벽을 만나면 반대방향으로 돌아온다
            cnt += 1
            d = direc[5][d]


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 게임판 크기, 5 <= N <= 100
    # 블록은 1~5, 웜홀은 6~10, 블랙홀은 -1
    board = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0

    # 상하좌우 델타
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 블록을 만난 후 진행하는 방향의 델타 배열 인덱스
    direc = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2]]

    # wormhole = []
    # for i in range(N):
    #     for j in range(N):
    #         if 6 <= board[i][j] <= 10:
    #             wormhole.append([board[i][j], i, j])

    wormhole_check = [0] * 11
    wormhole_info = dict()  # 웜홀 쌍 정보
    for i in range(N):
        for j in range(N):
            if 6 <= board[i][j] <= 10:
                num = board[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else:  # 같은 번호 웜홀끼리 위치 정보 저장
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]

    for i in range(N):
        for j in range(N):
            if not board[i][j]:  # 출발점은 0인 곳만 가능
                for d in range(4):  # 핀볼은 상하좌우 중 한방향으로 움직임
                    start = i, j
                    pinball(start, d)

    print(f'#{tc} {max_v}')
