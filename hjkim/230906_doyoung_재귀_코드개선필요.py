def solve1(i, N, mul):
    if i == N:
        return mul
    mul_lst.append(solve1(i + 1, N, mul * sour[i]))
    mul_lst.append(solve1(i + 1, N, mul * 1))

def solve2(i, N, my_sum):
    if i == N:
        return my_sum
    my_sum_lst.append(solve2(i + 1, N, my_sum + bitter[i]))
    my_sum_lst.append(solve2(i + 1, N, my_sum + 0))

N = int(input())   # N 재료 개수
taste = [list(map(int, input().split())) for _ in range(N)]

sour = [taste[s][0] for s in range(N)]  # S 곱
bitter = [taste[b][1] for b in range(N)]  # B 합

mul = 1
mul_lst = []
my_sum = 0
my_sum_lst = []

solve1(0,N,1)
solve2(0,N,0)

diff = []

for i in range(len(mul_lst)):
    if mul_lst[i] != None and my_sum_lst[i] != None and mul_lst[i] != 0 and my_sum_lst[i] != 0:
        diff.append(abs(mul_lst[i] - my_sum_lst[i]))

ans = min(diff)

print(ans)