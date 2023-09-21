from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs():
    global cnt
    queue = deque(ripe_tomatoes)

    minimum_date = 0
    while queue:
        cr, cc = queue.popleft()

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            # 범위 안에 있고, 익지 않았으며, 과일이 있는 경우만...
            if 0 <= nr < N and 0 <= nc < M and boxes[nr][nc] != -1 and not ripened[nr][nc]:
                # 큐에 삽엡
                queue.append((nr, nc))
                # 방문 표시
                ripened[nr][nc] += ripened[cr][cc] + 1
                # 덜 익은 사과 익혔으니 덜 익은 사과 개수 cnt 빼기
                cnt -= 1
                # 최소 날짜 세기
                if minimum_date < ripened[nr][nc]:
                    minimum_date = ripened[nr][nc]

    return minimum_date


# 가로 칸 수 M, 세로 칸 수 N
M, N = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]
# 안 익은 토마토 세는 변수
cnt = 0
# 익은 토마토 위치 기억하는 리스트
ripe_tomatoes = []
# 익었는지 판단하는 리스트 (1 익음, 0 안익음 혹은 토마토 없음)
ripened = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 0:
            cnt += 1
        elif boxes[i][j] == 1:
            ripe_tomatoes.append((i, j))
            ripened[i][j] = 1
# 이미 모든 토마토가 익은 경우면 익힐 필요가 없음
if cnt == 0:
    print(0)
# 익지 않은 토마토가 있다면 bfs 돌리기
else:
    result = bfs()
    if cnt != 0:
        print(-1)
    else:
        print(result - 1)



