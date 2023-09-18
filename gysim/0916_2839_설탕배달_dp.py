# N 킬로그램 배달, 설탕봉지는 3킬로그램과 5킬로그램 두 종류
# 최대한 적은 개수의 봉지를 들고 가려고 함

# dp, 메모이제이션
N = int(input())

# 초기값을 dp[3], dp[5] 두개 할당하는데,
# 배열 크기를 N+1로 하면 3, 4 일 때 index out of range 가 뜸
dp = [5001] * (N+3)

dp[3] = 1
dp[5] = 1

# 6부터 N까지 설탕의 최소값은 dp 배열에서 -3, -5 한 값을 활용할 수 있다
for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

# 정확하게 만들수 없다면 -1 출력, '==' 반례는 7
if dp[N] >= 5001:
    print(-1)
else:
    print(dp[N])
