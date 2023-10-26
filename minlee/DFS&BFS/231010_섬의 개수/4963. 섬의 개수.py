import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 진짜 신기한 건..pypy로 하면 런타임 에러 혹은 메모리초과가 나는데
# python3으로 돌리면 바로 통과..

def DFS(x, y):
    visited[x][y] = 1
    for k in range(8):
        nx = x+d[k][0]
        ny = y+d[k][1]
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and island[nx][ny] == 1:
            DFS(nx, ny)

# w가 가로(열), h가 세로(행)
w, h = map(int, input().split())
while w or h:
    island = [list(map(int,input().split())) for _ in range(h)]
    d = [[-1, 0],[1, 0], [0, 1],[0, -1], [1, 1],[-1, -1], [1, -1],[-1, 1]]
    visited = [[0] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and island[i][j] == 1:
                DFS(i, j)
                count += 1
    print(count)

    w, h = map(int, input().split())