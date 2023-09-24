# 7576. 토마토

from collections import deque
# delta
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

def tomato():
    queue = []
    
    for row in range(N):
        for col in range(M):
            if data[row][col] == 1: # 익은 토마토 찾으면
                queue.append((row, col))
    
    while queue:
        i, j = queue.pop(0)
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if 0 <= ni < N and 0 <= nj < M and data[ni][nj] == 0:
                queue.append((ni, nj))
                data[ni][nj] = data[i][j] + 1

    date = 0
    for row in range(N):
        for col in range(M):
            if data[row][col] == 0:
                return -1
            if data[row][col] > date:
                date = data[row][col]
    return date - 1

M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
ans = tomato()
print(ans)