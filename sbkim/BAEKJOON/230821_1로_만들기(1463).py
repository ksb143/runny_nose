# 요정이 도와줌 근데 못찾아서 해답을 집어줌
N = int(input())

dp = [0] * (N+1)

for i in range(2, N+1):
    # 일단 d[i]를 다 만든다!
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        # 2 나눈 것 + 1과 만든 dp[i] 중에 최소를 구해서 dp[i]를 바꿔준다.
        dp[i] = min(dp[i], dp[i//2] + 1)
        # 3 나눈 것 + 1과 만든 dp[i] 중에 최소를 구해서 dp[i]를 바꿔준다.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

# 그렇게 해서 나온 값을 구한다.
print(dp[N])