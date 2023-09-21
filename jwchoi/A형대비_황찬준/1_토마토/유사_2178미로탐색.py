# https://uni2237.tistory.com/116
# https://www.acmicpc.net/problem/2178
from collections import deque
n,m = map(int,input().split())
data = [] # ['101111', '101010', '101011', '111011']
for _ in range(n+1):
    data.append(['0'] + list(input()))
vi = [['0']*(m+1) for _ in range(n+1)]
dir_idx = [[-1,0],[0,1],[1,0],[0,-1]]
d = deque()
print(data)
print(d)
print(vi)
while d:
    for i in range(1,n+1):
        for j in range(1,m+1):
            # data[i][j]
            for k in range(4):
                ni = i + dir_idx[k][0]
                nj = j + dir_idx[k][1]
                if 0<= ni <n+1 and 0 <= nj < m+1:
                    if data[ni][nj] == '1':
                        pass