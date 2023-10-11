from collections import deque

def BFS(i):
    global count
    visited[i] = 1
    queue.append(i)
    count += 1
    while queue:
        k = queue.popleft()
        for j in tree[k]:
            if not visited[j]:
                visited[j] = 1
                queue.append(j)

N, M = map(int, input().split())
# N은 정점 개수, M은 간선 개수

tree = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
# tree에 각 연결된 숫자들이 들어가 있을 것!

# 각 연결 노드들을 큐에 넣고(큐에 있는 거면 넣지 말기)
# 카운트 우선 세고 큐 요소 따라 가보다 끝날때까지 반복

# 비지티드, 큐, 카운트 필요
visited = [0] * (N+1)
queue = deque()
count = 0

for i in range(1, N):
    if not visited[i]:
        BFS(i)

print(count)
