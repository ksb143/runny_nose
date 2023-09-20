def f(n0):
    # 만약 n0가 1,2,3이라면?
    if n0 ==1:
        return 1
    if n0 ==2:
        return 2
    if n0 ==3:
        return 4
    dp = [0]*(max(4,n0+1))
    # 만약 n0가 4이상이라면?
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4,n0+1):
        dp[i] = dp[i-3] + dp[i-2] +dp[i-1]
    return dp[n0]

T = int(input())
for tc in range(1,1+T):
    n = int(input())
    print(f(n))

