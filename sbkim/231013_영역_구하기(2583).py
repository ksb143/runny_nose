dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, paper, area):

    stack = [(r, c)]
    paper[r][c] = 1
    area += 1

    while stack:
        cr, cc = stack[-1]
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < M and 0 <= nc < N and not paper[nr][nc]:
                stack.append((nr, nc))
                paper[nr][nc] = 1
                area += 1
                break
        else:
            stack.pop()

    return area


# 눈금의 간격 M(세로) * N(가로), 직사각형 개수 K
M, N, K = map(int, input().split())

paper = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    y1, y2 = M - y2, M - y1
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1


cnt = 0
areas = []


for r in range(M):
    for c in range(N):
        if paper[r][c] == 0:
            cnt += 1
            result = dfs(r, c, paper, 0)
            areas.append(result)


areas.sort()

print(cnt)
print(*areas)
