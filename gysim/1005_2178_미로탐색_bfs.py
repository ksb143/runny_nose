# N*M 크기 배열, 1은 이동가능, 0은 이동불가능
# (1,1)에서 출발, (N,M)으로 이동할 때 지나야하는 최소의 칸수 출력
# 서로 인접한 칸으로만 이동가능, 시작점,도착점도 칸수에 포함

from collections import deque


def bfs():
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maze[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

    return visited[N-1][M-1]


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
min_v = bfs()
print(min_v)
