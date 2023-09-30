def change_dir(ci,cj,cd):   # cd : 현재 방향
    # 상 우 하 좌   ( 0 1 2 3 )
    if cd == 0:
        if data[ci][cj] == 1 or 4 or 5:
            cd = 2
            return cd
        elif data[ci][cj] == 2:
            cd = 1
            return cd
        elif data[ci][cj] == 3:
            cd = 3
            return cd
    elif cd == 1:
        if data[ci][cj] == 1 or 2 or 5:
            cd = 3
            return cd
        elif data[ci][cj] == 3:
            cd = 2
            return cd
        elif data[ci][cj] == 4:
            cd = 0
            return cd
    elif cd == 2:
        if data[ci][cj] == 1:
            cd = 1
            return cd
        elif data[ci][cj] == 2 or 3 or 5:
            cd = 0
            return cd
        elif data[ci][cj] == 4:
            cd = 3
            return cd
    else:
        if data[ci][cj] == 1:
            cd = 0
            return cd
        elif data[ci][cj] == 2:
            cd = 2
            return cd
        elif data[ci][cj] == 3 or 4 or 5:
            cd = 1
            return cd
def pinball():
    # 점수 초기화
    max_v = 0
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 시작점에서 네 방향으로 출발해보는 방향 구현하기
    for i in range(M):
        # (start[i][0], start[i][1]) --- 시작점 좌표 (si, sj)
        si, sj = start[i][0], start[i][1]
        score = 0
        # 탐색하는 지점이 블록인지 벽인지 웜홀인지 블랙홀인지 시작점인지 확인하기
        for i in range(N):
            for j in range(N):
                # 네 방향 탐색하기
                ci, cj , cd = si, sj, 0
                ni, nj = ci + dir[cd][0], cj + dir[cd][1]
                if 0 <= ni < N and 0 <= nj < N and data[ni][nj] == -1:  # 블랙홀일 경우 탐색 종료
                    return score
                elif 0 <= ni < N and 0 <= nj < N and (ni,nj) == (si,sj):  # 시작위치로 돌아올 경우 탐색 종료
                    return score
                elif 0<= ni < N and 0<= nj < N and not data[ni][nj]:   # 탐색방향이 빈 공간일 경우 그대로 가기
                    ni, nj = ci, cj
                    cd = cd
                elif 0<= ni < N and 0<=nj<N and data[ni][nj] == 1 or 2 or 3 or 4 or 5:   # 블럭일 경우 방향 바꾸기
                    score += 1
                    cd = change_dir(ni,nj,cd)
                    ci, cj = ni + dir[cd][0], nj + dir[cd][1]
                else:   # 웜홀일 경우




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = []
    start = []
    wormhole = [[0]*4 for _ in range(5)]
    visited_hole = [0] * 5
    for i in range(N):
        for j in range(N):
            # 시작점 찾기
            if data[i][j] == 0:
                start.append((i,j))
            # 웜홀 위치 찾기
            elif data[i][j] == 6:
                if not visited_hole[0]:
                    wormhole[0][0] = i
                    wormhole[0][1] = j
                    visited_hole[0] += 1
                else:
                    wormhole[0][2] = i
                    wormhole[0][3] = j
            elif data[i][j] == 7:
                if not visited_hole[1]:
                    wormhole[1][0] = i
                    wormhole[1][1] = j
                    visited_hole[1] += 1
                else:
                    wormhole[1][2] = i
                    wormhole[1][3] = j
            elif data[i][j] == 8:
                if not visited_hole[2]:
                    wormhole[2][0] = i
                    wormhole[2][1] = j
                    visited_hole[2] += 1
                else:
                    wormhole[2][2] = i
                    wormhole[2][3] = j
            elif data[i][j] == 9:
                if not visited_hole[3]:
                    wormhole[3][0] = i
                    wormhole[3][1] = j
                    visited_hole[3] += 1
                else:
                    wormhole[3][2] = i
                    wormhole[3][3] = j
            elif data[i][j] == 10:
                if not visited_hole[4]:
                    wormhole[4][0] = i
                    wormhole[4][1] = j
                    visited_hole[4] += 1
                else:
                    wormhole[4][2] = i
                    wormhole[4][3] = j


    M = len(start)
