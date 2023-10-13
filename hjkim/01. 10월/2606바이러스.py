def bfs(node):

    global result

    path = list()
    path.append(node)
    visited[node] = 1

    while path:
        current = path.pop(0)
        for link in range(links * 2):
            start = computers[link][0]
            end = computers[link][1]
            if current == start and not visited[end]:
                path.append(end)
                visited[end] = 1
                result += 1


computer = int(input())
links = int(input())
computers = [list(map(int, input().split())) for _ in range(links)]
visited = [0] * computer
for idx in range(links):
    computers.append([computers[idx][1], computers[idx][0]])
result = 0
bfs(1)
print(result)