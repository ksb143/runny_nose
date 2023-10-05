# https://uni2237.tistory.com/116
# https://www.acmicpc.net/problem/2178
from collections import deque
d = deque()
d.append((0,0))

n,m = map(int,input().split())
maze = [list(map(int,input().rstrip())) for _ in range(n)]

vi = [[-1]*m for _ in range(n)]
vi[0][0] = 1

dir_idx = [[-1,0],[0,1],[1,0],[0,-1]]

while d: # deque 가 비지 않은 동안 작동
    x,y = d.popleft() # (0,0)에서
    for k in range(4):
        nx = x + dir_idx[k][0]
        ny = y + dir_idx[k][1]
        if 0<=nx<n and 0<=ny<m and vi[nx][ny]==-1: # 4방향에 방문안한 1이 있다면
            if maze[nx][ny] ==1:
                d.append((nx,ny))
                vi[nx][ny] = vi[x][y]+1
                # vi
print(vi[n-1][m-1])