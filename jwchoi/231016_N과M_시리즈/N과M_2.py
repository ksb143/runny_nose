def comb(idx, start, M):
    # 종료 조건
    if idx == M:
        print(*ch)
        return
    # 진행 조건
    for i in range(start, N+1):
        ch[idx] = i

        comb(idx+1, i+1, M)

# N,M
N, M = map(int, input().split())
# 수열 썼는지 체크할 ch
ch = [0] * M

comb(0, 1, M)
