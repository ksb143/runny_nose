def comb(idx, cnt, k, check):
    # 6개 뽑은 경우 리턴
    if cnt == 6:
        for i in range(k):
            if check[i] == 1:
                print(S[i], end=' ')
        print()
        return
    # 다 뽑은 경우에도 리턴
    if idx == k:
        return
    # 해당 idx 번호 뽑기
    check[idx] = 1
    comb(idx+1, cnt+1, k, check)
    # 해당 idx 번호 안뽑기
    check[idx] = 0
    comb(idx+1, cnt, k, check)


while True:
    S = list(map(int, input().split()))
    k = S.pop(0)

    if k == 0:
        break

    check = [0] * k

    comb(0, 0, k, check)
    print()

