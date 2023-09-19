# 서쪽 N , 동쪽 M , 다리 N 개 짓기
# 다리는 겹쳐질 수 없음
def dp(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] * i
    return dp[n]


T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    answer = dp(M) // (dp(N) * dp(M-N))
    print(f'#{tc} {answer}')