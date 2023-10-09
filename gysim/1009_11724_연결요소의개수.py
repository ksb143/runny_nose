from collections import deque


def dfs(start):
    stack = deque()
    stack.append(start)
    visited[start] = 1

    while stack:
        now = stack.pop()

        for i in adj[now]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [0] * (N+1)
cnt = 0
for i in range(1, N+1):
    # if adj[i] and not visited[i]:
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
