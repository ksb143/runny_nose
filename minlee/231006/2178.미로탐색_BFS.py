from collections import deque

N, M = map(int, input().split())
# N이 행, M이 열
miro = [list(map(int, input())) for _ in range(N)]
# 1은 이동할 수 있다, 0은 이동할 수 없다
# (0,0)에서 출발해서 (N-1,M-1)에 도착
answer = []
# 총 몇 칸 움직였는지 확인하기
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# 이동범위
visited = [[0]*M for _ in range(N)]
# 방문여부 안간곳만 가자
visited[0][0] = 1
# 출발점 표시

x=y=0
queue = deque()
# 디큐를 통해서 앞에서 빼보기
queue.append((x, y, 1))

while x != N - 1 or y != M - 1:
    # or인 거 까먹지말기!!!!실수하지말기!
    x, y, count = queue.popleft()
    # 변화하는 것들 큐에 넣어놓고 계속 변화시키면 되니까!
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            queue.append((nx,ny,count+1))
            # 다른 건 DFS랑 똑같아

print(count)