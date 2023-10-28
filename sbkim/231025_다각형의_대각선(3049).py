N = int(input())

check = [0] * N

ans = 0

def comb(idx, cnt, N, check):
    global ans
    # 4개를 뽑은 경우
    if cnt == 4:
        ans += 1
        return
    # 다 돌았지만 나오지 않는 경우
    if idx == N:
        return

    # 뽑기
    check[idx] = 1
    comb(idx+1, cnt+1, N, check)
    # 안뽑기
    check[idx] = 0
    comb(idx+1, cnt, N, check)

comb(0, 0, N, check)

print(ans)
