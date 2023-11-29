R, C = map(int, input().split())
alphabets = [input().strip() for _ in range(R)]

max_v = 0
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(r, c, used, cnt):
    global max_v

    if cnt > max_v:
        max_v = cnt

    for d in range(4):
        nr, nc = r + delta[d][0], c + delta[d][1]
        if 0 <= nr < R and 0 <= nc < C and alphabets[nr][nc] not in used:
            dfs(nr, nc, used+alphabets[nr][nc], cnt+1)


dfs(0, 0, alphabets[0][0], 1)

print(max_v)
