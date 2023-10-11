def dfs_iter(r0,c0):
    vi = [[0] * r for _ in range(c)]
    stack = []
    if vi[r0][c0] == 0:
        stack.append((r0,c0))
        while stack:
            rr, cc = stack.pop()
            for k in range(8):
                nr, nc = dr[k]+rr, dc[k]+cc
                if 0<= nr < r and 0<= nc < c:
                    if vi[nr][nc] == 0:
                        vi[nr][nc] =1
                        stack.append((nr,nc))
    return

r,c = map(int, input().split())
# print(r,c)
data = []
for _ in range(c):
    data.append(list(map(int, input().split())))
# print(data)
# 상하좌우+대각선:
dr,dc = [-1,1,0,0,-1,1,-1,1],[0,0,-1,1,-1,-1,1,1]
dfs_iter(0,0)
