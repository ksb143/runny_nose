def DFS(x, y, setset, cnt):
    global max_num
    if max_num < cnt:
        max_num = cnt
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < R and 0 <= ny < C and word[nx][ny] not in setset:
            setset.add(word[nx][ny])
            DFS(nx, ny, setset, cnt + 1)
            setset.remove(word[nx][ny])


R, C = map(int, input().split())
word = [list(input()) for _ in range(R)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
alphabet = {word[0][0]}
max_num = 0
DFS(0, 0, alphabet, 1)
print(max_num)