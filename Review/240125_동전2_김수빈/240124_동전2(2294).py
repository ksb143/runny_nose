n, k = map(int, input().split())
# 중복 제거하기 위해 set에 넣음
coins = list({int(input()) for _ in range(n)})

# 순서대로 계산하기 위해 정렬해주기
coins.sort()

# 초기값 크게 넣어주기
dp = [0xffffffff] * (k+1)

# 0원을 만드는데 필요한 동전 개수
dp[0] = 0
# 이미 가지고 있는 동전의 가치를 만들기 위해 필요한 동전 개수
for coin in coins:
    # 해당 동전이 k가치 안에 들면 넣기
    if coin <= k:
        dp[coin] = 1

for coin in coins:
    for num in range(1, k+1):
        # 범위 내의 것만 구하기
        if 0 <= num - coin <= k:
            # 현재 값에서 업데이트 해주기
            # num 가치를 만들 기 위해서는 내 coin 개수 1개랑 num - coin 가치를 더하면 되는 것
            # 기존 값이 더 작을 수도 있으므로 거기서 min 값을 구함
            dp[num] = min(dp[num], dp[num-coin] + 1)

if dp[k] == 0xffffffff:
    print(-1)
else:
    print(dp[k])

