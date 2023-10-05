def DFS(count, x, y):
    if x == N-1 and y == M-1:
        answer.append(count)
        return
    # 종점에 도착하면 종료하기
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            DFS(count+1, nx, ny)
            visited[nx][ny] = 0


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
DFS(1, 0, 0)
print(min(answer))