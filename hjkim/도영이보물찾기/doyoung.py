'''
문제
도영이는 짜파구리 요리사로 명성을 날렸었다. 이번에는 이전에 없었던 새로운 요리에 도전을 해보려고 한다.

지금 도영이의 앞에는 재료가 N개 있다. 도영이는 각 재료의 신맛 S와 쓴맛 B를 알고 있다.

여러 재료를 이용해서 요리할 때, 그 음식의 신맛은 사용한 재료의 신맛의 곱이고, 쓴맛은 합이다.

시거나 쓴 음식을 좋아하는 사람은 많지 않다.

도영이는 재료를 적절히 섞어서 요리의 신맛과 쓴맛의 차이를 작게 만들려고 한다.

또, 물을 요리라고 할 수는 없기 때문에, 재료는 적어도 하나 사용해야 한다.

재료의 신맛과 쓴맛이 주어졌을 때, 신맛과 쓴맛의 차이가 가장 작은 요리를 만드는 프로그램을 작성하시오.

1
3 10

7

2
3 8
5 8

1
'''

def solve1(i, N, mul):    # 신맛 곱 구하는 함수
    if i == N:
        return mul
    mul_lst.append(solve1(i + 1, N, mul * sour[i]))
    mul_lst.append(solve1(i + 1, N, mul * 1))

def solve2(i, N, my_sum):  # 쓴맛 합 구하는 함수
    if i == N:
        return my_sum
    my_sum_lst.append(solve2(i + 1, N, my_sum + bitter[i]))
    my_sum_lst.append(solve2(i + 1, N, my_sum + 0))

N = int(input())   # N 재료 개수
taste = [list(map(int, input().split())) for _ in range(N)]

sour = [taste[s][0] for s in range(N)]  # S 곱
bitter = [taste[b][1] for b in range(N)]  # B 합


mul_lst = []

my_sum_lst = []

solve1(0,N,1)
solve2(0,N,0)

diff = []

for i in range(len(mul_lst)):
    if mul_lst[i] != None and my_sum_lst[i] != None and mul_lst[i] != 0 and my_sum_lst[i] != 0:
        diff.append(abs(mul_lst[i] - my_sum_lst[i]))

ans = min(diff)

print(ans)