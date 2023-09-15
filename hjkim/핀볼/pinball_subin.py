# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(sr, sc):
    max_score = 0
    for i in range(4):
        cr, cc = sr, sc
        score = 0
        while True:
            nr, nc = cr + dr[i], cc + dc[i]
            # 블록을 안 만났을 때
            if 0 <= nr < N and 0 <= nc < N and not board[nr][nc]:
                cr, cc = nr, nc
                # 추가된 nr, nc가 첫 위치와 같으면 break
                if nr == sr and nc == sc:
                    break
            # 블랙홀을 만났을 때 break
            elif 0 <= nr < N and 0 <= nc < N and board[nr][nc] == -1:
                break
            # 블록을 만났을 때
            elif 0 <= nr < N and 0 <= nc < N and 1 <= board[nr][nc] <= 5:
                cr, cc = nr, nc
                score += 1
                temp = board[nr][nc]
                # 위로 가고 되돌아가는 블록을 만났을 경우 방향 바꿔주기
                if i == 0:
                    if temp == 2:
                        i = 3
                    elif temp == 3:
                        i = 2
                    else:
                        i = 1
                # 밑으로 가고 되돌아가는 블록을 만났을 경우 방향 바꿔주기
                elif i == 1:
                    if temp == 1:
                        i = 3
                    elif temp == 4:
                        i = 2
                    else:
                        i = 0
                # 좌로 가고 되돌아가는 블록을 만났을 경우 방향 바꿔주기
                elif i == 2:
                    if temp == 1:
                        i = 0
                    elif temp == 2:
                        i = 1
                    else:
                        i = 3
                # 우로 가고 되돌아가는 블록을 만났을 경우 방향 바꿔주기
                else:
                    if temp == 3:
                        i = 1
                    elif temp == 4:
                        i = 0
                    else:
                        i = 2
            # 벽을 만났을 때
            elif -1 == nr or N == nr or -1 == nc or N == nc:
                cr, cc = nr, nc
                score += 1
                # 위로 간 경우 위치 변경
                if i == 0:
                    i = 1
                # 아래로 간 경우 위치 변경
                elif i == 1:
                    i = 0
                # 좌로 간 경우 위치 변경
                elif i == 2:
                    i = 3
                # 우로 간 경우 위치 변경
                else:
                    i = 2
            # 웜홀을 만났을 때
            elif 0 <= nr < N and 0 <= nc < N and 6 <= board[nr][nc] <= 10:
                cp = board[nr][nc]
                is_ok = False
                for r in range(N):
                    for c in range(N):
                        if board[r][c] == cp and r != nr and c != nc:
                            cr, cc = nr, nc
                            is_ok = True
                            break
                    if is_ok == True:
                        break

        # 최대값 구하기
        if max_score < score:
            max_score = score
    return max_score


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().strip().split())) for _ in range(N)]
    max_score = 0
    for r in range(N):
        for c in range(N):
            # 현재 위치
            sr, sc = r, c
            result = 0
            # 상하좌우 dfs 해보기(블럭이 없는 곳에서만 출발)
            if board[sr][sc] == 0:
                result = dfs(sr, sc)
            if max_score < result:
                max_score = result
    print(f'#{tc} {max_score}')
