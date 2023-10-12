def DFS(X, count):
    if not visited[X]:
        visited[X] = count
        for i in computers[X]:
            DFS(i, count + 1)

N = int(input())
node = int(input())
computers = [[] for _ in range(N+1)]
for _ in range(node):
    x, y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)

visited = [0]*(N+1)

DFS(1, 1)
print(max(visited))