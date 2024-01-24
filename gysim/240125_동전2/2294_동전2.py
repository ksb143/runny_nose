def coin_cnt(N, K, coins):
    dp = [0xffffff] * (K + 1)  # 1원부터 K원까지 -> K+1

    # 초기값 설정
    dp[0] = 0

    # coins 순회
    for i in range(N):
        # coins[i] ~ coins[i+1] 범위의 숫자 계산
        for j in range(i, coins[i + 1]):
            # 점화식 모르겠다!!!!!!!!!!!
            dp[i] = dp[i+1]

    if dp[K + 1] == 0xffffff:
        print(-1)
    else:
        print(dp[K + 1])


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()

coin_cnt(N, K, coins)


# gpt 코드
# def min_coin_count(n, k, coin_values):
#     # dp[i]: 금액 i를 만들 때의 최소 동전 개수
#     dp = [float('inf')] * (k + 1)
#     dp[0] = 0  # 초기값: 0원을 만들 때의 동전 개수는 0
#
#     for coin in coin_values:
#         for i in range(coin, k + 1):
#             dp[i] = min(dp[i], dp[i - coin] + 1)
#
#     return dp[k] if dp[k] != float('inf') else -1
#
#
# # 입력 받기
# n, k = map(int, input().split())
# coin_values = [int(input()) for _ in range(n)]
#
# # 결과 출력
# result = min_coin_count(n, k, coin_values)
# print(result)
