from collections import defaultdict

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    clothes = [list(input().split()) for _ in range(N)]
    garments = defaultdict(list)

    for cloth in clothes:
        garments[cloth[1]].append(cloth[0])

    cnt = 1
    for key in garments:
        cnt *= (len(garments[key]) + 1)

    print(cnt - 1)