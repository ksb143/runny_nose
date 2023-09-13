dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    stack = [(r, c)]
    visited = [[0]*M for _ in range(N)]
    
    while stack:
        cr, cc = stack[-1]
        visited[cr][cc] = 1
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 1 and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                # 연결된 배추면 넣기
                check.append((nr, nc))
                break
        else:
            stack.pop()
    return 1



T = int(input())

for tc in range(T):
    # M 가로, N 세로, K 배추 위치 개수
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    for k in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    # 배추면 넣기
    check = []
    earthworm = 0
    for r in range(N):
        for c in range(M):
           if field[r][c] == 1 and (r, c) not in check:
               check.append((r, c))
               earthworm += dfs(r, c)
    print(earthworm)