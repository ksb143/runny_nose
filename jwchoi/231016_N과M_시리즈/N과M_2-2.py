from itertools import combinations

N, M = map(int, input().split())
result = list(combinations([i for i in range(1,1+N)],M))
for x in result:
    print(*x)