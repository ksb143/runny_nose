def dfs(adj, district, N, P):
    visited = [0] * (N + 1)
    start = district[0]
    stack = [start]
    diff = P[start]
    district.remove(start)
    while stack:
        top = stack[-1]
        visited[top] = 1
        for i in range(1, N+1):
            if i in district and adj[top][i] == 1 and not visited[i]:
                stack.append(i)
                diff += P[i]
                district.remove(i)
                break

        else:
            stack.pop()
    if not district:
        return diff


# 구역의 개수
N = int(input())
# 인구 수
P = [0] + list(map(int, input().split()))
sum_P = sum(P)
# 인접 매트릭스 만들기
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    vertex = list(map(int, input().split()))
    vertex.pop(0)
    for v in vertex:
        adj[i][v] = 1
        adj[v][i] = 1

min_v = 0xffffffff

# powerset 만들기
for i in range(1, (1<<N)//2):
    d1 = []
    d2 = []
    total = 0
    for j in range(N):
        if i&(1<<j):
            d1.append(j+1)
        else:
            d2.append(j+1)
    A, B = dfs(adj, d1, N, P), dfs(adj, d2, N, P)
    if type(A) == int and type(B) == int:
        if min_v > abs(A - B):
            min_v = abs(A - B)
if min_v == 0xffffffff:
    print(-1)
else:
    print(min_v)



