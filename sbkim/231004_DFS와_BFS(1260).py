# # for 문
# def dfs(v):
#     visited = [0] * (N+1)
#
#     stack = [v]
#     visited[v] = 1
#
#     while stack:
#         top = stack[-1]
#         print(top, end=' ')
#         for i in adj[top]:
#             if not visited[i]:
#                 stack.append(i)
#                 visited[i] = 1
#                 break
#         else:
#             stack.pop()
#     print()

# 재귀
def dfs_recur(v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in adj[v]:
        if not visited[i]:
            dfs_recur(i, visited)

def bfs(v):
    visited = [0] * (N+1)

    queue = [v]
    visited[v] = 1

    while queue:
        front = queue.pop(0)
        print(front, end=' ')
        for i in adj[front]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)

# 작은 것부터 해야해서 정렬
for i in range(N+1):
    adj[i].sort()

visited = [0]*(N+1)

dfs_recur(V, visited)
print()
bfs(V)
print()


