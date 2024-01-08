dr = [-1, 1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, -1, 1, 1, -1, -1, 1]

import sys
from collections import deque


def dfs(i, j):
    stack = deque()
    stack.append((i, j))

    while stack:
        r, c = stack[-1]
        maps[r][c] = 0      # 방문 표시
        for k in range(8):
            nr, nc = r + dr[k], c + dc[k]
            # 범위 안에 들고 섬이면 스택안에 넣고 break
            if 0 <= nr < h and 0 <= nc < w and maps[nr][nc] == 1:
                stack.append((nr, nc))
                break
        else:
            stack.pop()


while True:
    # 너비와 높이
    w, h = map(int, sys.stdin.readline().split())

    # 종료 조건
    if w == 0 and h == 0:
        break

    # 지도
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

    # 섬의 개수 세는 cnt
    cnt = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
