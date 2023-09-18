# N 킬로그램 배달, 설탕봉지는 3킬로그램과 5킬로그램 두 종류
# 최대한 적은 개수의 봉지를 들고 가려고 함

N = int(input())

# N 번까지 구해야해서 N+1개 만들어줌
# 정확하게 만들수 없다면 -1 출력
sum_v = []

for a in range(N//2+1):
    for b in range(N//2+1):
        if (5 * a + 3 * b) == N:
            sum_v.append(a+b)

if len(sum_v) == 0:
    print(-1)
else:
    print(min(sum_v))
