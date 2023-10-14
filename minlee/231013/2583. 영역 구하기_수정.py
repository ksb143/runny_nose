import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def DFS(x, y):
    global count
    nemo[x][y] = 1
    count += 1
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < M and 0 <= ny < N and not nemo[nx][ny]:
            DFS(nx, ny)


M, N, K = map(int, input().split())
# M이 행, N이 열, K개 직사각형
nemo = [[0]*N for _ in range(M)]
# 다른 숫자로 채워서 0인 곳만 찾아볼 수 있도록
# 0인 곳 개수 + 각 범위 찾기 문제
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    # 그래프 상 좌표이기에 행/열과는 반대!!
    for i in range(y1, y2):
        for j in range(x1, x2):
            nemo[i][j] = 1

answer = []
# 각 영역의 넓이 담기
part = 0
# 분리되어 나누어지는 영역 개수
d = [[-1, 0], [1, 0], [0, 1], [0, -1]]


for i in range(M):
    for j in range(N):
        count = 0
        if not nemo[i][j]:
            part += 1
            DFS(i, j)
            answer.append(count)

answer.sort()
print(part)
print(*answer)