T = int(input())
for _ in range(T):
    # 11보다 작은 양수
    n = int(input())
    dp = [0] * 11

    # n을 1, 2, 3의 합으로 나타내는 방법의 수 출력
    # 합을 나타낼 때는 수를 1개 이상 사용해야한다 -> 공집합을 제외?
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[n])
    