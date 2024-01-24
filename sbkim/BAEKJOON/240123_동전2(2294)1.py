# n가지 동전
# k 가치 만들기
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [set() for _ in range(n+1)]

# 첫 번째 경우의 수 구함
for i in range(n):
    dp[1].add(coins[i])

# 두 번째 경우의 수 구함
for i in range(n):
    for j in range(i, n):
        dp[2].add(coins[i] + coins[j])

# 세 번째 경우의 수는 점화식으로 구함
for i in range(1, n+1):
    for j in range(i+1):
        for x in dp[j]:
            for y in dp[i-j]:
                dp[i].add(x+y)

    if k in dp[i]:
        answer = i
        break
else:
    answer = -1

print(answer)

