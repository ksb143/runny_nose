N = int(input())

dp = [0] * 5001

dp[1] = 0xffffffff
dp[2] = 0xffffffff
dp[3] = 1
dp[4] = 0xffffffff
dp[5] = 1


for i in range(6, 5001):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[N] >= 0xffffffff:
    print(-1)
else:
    print(dp[N])