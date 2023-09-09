def bridge(N, M):
    global result
    if N == 1:
        result += M
        return
    else:
        if N == M:
            result += 1
        elif N < M:
            for i in range(1, M):
                bridge(N - 1, i)


T = int(input())
for tc in range(1, 1 + T):
    result = 0
    N, M = map(int, input().split())
    bridge(N, M)

    print(result)