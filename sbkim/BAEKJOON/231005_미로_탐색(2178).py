dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def navigation(N, M, sr, sc):
    queue = [(sr, sc)]
    visited = [[0]*M for _ in range(N)]
    visited[sr][sc] = 1
    while queue:
        r, c = queue.pop(0)
        # 리스트가 0부터 시작하므로 N-1, M-1로 마무리
        if r == N-1 and c == M-1:
            return visited[r][c]
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 범위 내이고 갈 수 있는 길이며 방문하지 않았다면...
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1 and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1


N, M = map(int, input().split())

maze = [[] for _ in range(N)]

for i in range(N):
    maze[i] = list(map(int, input()))

print(navigation(N, M, 0, 0))
