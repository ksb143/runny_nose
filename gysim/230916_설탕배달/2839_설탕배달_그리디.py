# N 킬로그램 배달, 설탕봉지는 3킬로그램과 5킬로그램 두 종류
# 최대한 적은 개수의 봉지를 들고 가려고 함

# 그리디
N = int(input())

sugar = 0
while N > 0:
    if N % 5 == 0:
        sugar += N//5
        break
    else:
        N -= 3
        sugar += 1

# N == 0 이 아닌 이유 : N % 5 == 0 조건문에 걸리면 N은 0 이상임
if N >= 0:
    print(sugar)
else:
    print(-1)
