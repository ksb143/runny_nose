# 어떤 배추에 지렁이가 한마리 살고 있으면 인접한 다른 배추로 이동 가능
# 상하좌우 네 방향에 다른 배추가 위치한 경우 인접해있는 것

# 상 하 좌 우
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T = int(input())
for tc in range(T):
    # M:가로, N:세로, K:배추 위치 개수
    M, N, K = map(int, input().split())
    # K행, 배추의 x좌표, y좌표 
    baechu = [list(map(int, input().split())) for _ in range(K)]

    queue = []
    visited = [[0] * N for _ in range(M)]

    cnt = 0
    for i in range(K):
        x = baechu[i][0]
        y = baechu[i][1]

        if not visited[x][y]:
            queue.append((x, y))
            visited[x][y] = 1
            cnt += 1

            while queue:
                r, c = queue.pop(0)

                for d in range(4):
                    nr = r + delta[d][0]
                    nc = c + delta[d][1]
                    if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and [nr, nc] in baechu:
                        queue.append((nr, nc))
                        visited[nr][nc] = 1

    # 최소의 지렁이 마리 수 출력
    print(cnt)


# bfs는 append 할 때 방문 표시를 해줘야 중복방문이 일어나지 않아 시간을 줄일 수 있다.

# def bfs():
#
#     queue = []
#     visited = [[0] * N for _ in range(M)]
#
#     cnt = 0
#     for i in range(K):
#         x = baechu[i][0]
#         y = baechu[i][1]
#
#         if not visited[x][y]:
#             queue.append((x, y))
#             cnt += 1
#
#         while queue:
#             r, c = queue.pop(0)
#             visited[r][c] = 1
#
#             for d in range(4):
#                 nr = r + delta[d][0]
#                 nc = c + delta[d][1]
#                 if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and [nr, nc] in baechu:
#                     queue.append((nr, nc))
#
#     return cnt
