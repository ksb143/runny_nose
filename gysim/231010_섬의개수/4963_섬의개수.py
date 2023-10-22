from collections import deque

# 가로, 세로, 대각선 연결되면 걸어갈 수 있음
def dfs(start):
    stack = deque()
    r, c = start
    stack.append(start)
    visited[r][c] = 1

    while stack:
        r, c = stack.pop()

        for d in range(8):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and maps[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1


delta = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
        # 1은 땅, 0은 바다
    maps = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    visited = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j]:
                dfs((i,j))
                cnt += 1

    # 섬의 개수 출력
    print(cnt)