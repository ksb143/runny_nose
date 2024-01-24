# 값 k 를 동전 n가지로 최소 개수로 만들기
# 그 최소 개수를 출력하기


# 입력
n, k = list(map(int, input().split()))

coins = []

for _ in range(n):
    coins.append(int(input()))


# dp 배열 선언. dp[k] 가 정답.
# 초기에 매우 큰 값으로 아직 계산되지 않은 배열을 초기화.
dp = [float('inf')] * (k+1)

# 0은 만들 수 없으므로 0으로 초기화.
dp[0] = 0

# 모든 금액 'i'에 대해 가능한 모든 동전 'coin'을 고려
for i in range(k+1):
    for coin in coins:
        if i - coin >= 0:
            # dp[i] = i원을 만드는 데 필요한 최소 동전 개수
            dp[i] = min(dp[i], dp[i - coin] + 1)

# 만약 초기 값 그대로라면 만들 수 없으므로 -1 출력
if dp[k] == float('inf'):
    dp[k] = -1

print(dp[k])