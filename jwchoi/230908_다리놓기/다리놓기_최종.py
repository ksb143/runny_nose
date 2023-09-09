T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # 초기화
    for i in range(M + 1):
        dp[1][i] = i

    # DP 계산
    for n in range(2, N + 1):
        for m in range(n, M + 1):
            dp[n][m] = dp[n][m-1] + dp[n-1][m-1]

    result = dp[N][M]
    print(result)

