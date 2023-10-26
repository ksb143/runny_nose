def DFS(x, y):
    global count, max_house, house
    if house > max_house:
        max_house = house
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and jido[nx][ny]:
            visited[nx][ny] = count
            house += 1
            DFS(nx, ny)


N = int(input())
jido = [list(map(int, input())) for _ in range(N)]

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[0]*N for _ in range(N)]

count = 1
answer = []

for i in range(N):
    for j in range(N):
        if jido[i][j] and not visited[i][j]:
            max_house = 0
            house = 0
            DFS(i, j)
            if max_house == 0:
                max_house = 1
            count += 1
            answer.append(max_house)

answer.sort()
print(len(answer))
for i in answer:
    print(i)