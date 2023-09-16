def solve():
    global min_v
    for i in range(a,-1,-1):
        for j in range(b,-1,-1):
            all.append((i,j))
    M = len(all)
    for i in range(M):
        if all[i][0]*5 + all[i][1]*3 == N:
            candidates.append((all[i][0],all[i][1]))
    if not candidates:
        return -1
    else:
        cnt = candidates[0][0] + candidates[0][1]
        return cnt


N = int(input())
a = N // 5
b = N // 3
all = []
candidates = []
min_v = 0xffff
print(solve())