from collections import deque


def bfs(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 1
    cnt = 1

    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr, nc = r + delta[d][0], c + delta[d][1]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and house[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = 1
                cnt += 1

    counts.append(cnt)
    

N = int(input())
house = [list(map(int, input())) for _ in range(N)]

counts = []
visited = [[0] * N for _ in range(N)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 배열 순회하면서 1을 만나면 bfs 시작
# bfs가 끝나고 counts.append(cnt)
for i in range(N):
    for j in range(N):
        if house[i][j] and not visited[i][j]:
            bfs(i, j)

# 총 단지수 출력
print(len(counts))
# 단지 내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력
counts.sort()
for i in counts:
    print(i)