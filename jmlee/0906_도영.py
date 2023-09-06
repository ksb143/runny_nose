def ans(idx):
    global min_v

    if idx == N:
        sour = 1
        bitter = 0
        cnt = 0
        for i in range(N):
            if used[i]:
                sour *= vegetables[i][0]
                bitter += vegetables[i][1]
            else:
                cnt += 1

        if cnt != N and abs(sour-bitter) < min_v:
            min_v = abs(sour-bitter)

        return
    
    used[idx] = 1
    ans(idx+1)
    used[idx] = 0
    ans(idx+1)



# N : 재료의 갯수
N = int(input())
vegetables = [list(map(int, input().split())) for _ in range(N)]

min_v = 0xffffffffff

used = [0] * N

ans(0)

print(min_v)