from collections import deque

def dfs(start):
    stack = deque()
    visited = deque()
    stack.append(start)

    while stack:
        now = stack.pop()
        if now not in visited:
            print(now, end=' ')
            visited.append(now)

        for i in range(len(adj[now])-1, -1, -1):
            if adj[now][i] not in visited:
                stack.append(adj[now][i])


def bfs(start):
    queue = deque()
    visited = deque()
    queue.append(start)
    visited.append(start)
    print(start, end=' ')

    while queue:
        now = queue.popleft()

        for i in adj[now]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                print(i, end=' ')

# 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문
# 정점 번호는 1번부터 N번까지

# 정점 개수, 간선 개수, 시작정점번호
N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)

for i in range(N+1):
    adj[i].sort()

# print(adj)
# [[], [2, 3, 4], [4], [4]]

# DFS 결과 출력
dfs(V)
print()
# BFS 결과 출력
bfs(V)