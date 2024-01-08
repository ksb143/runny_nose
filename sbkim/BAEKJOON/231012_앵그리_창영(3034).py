from math import sqrt

N, W, H = map(int, input().split())

D = sqrt(W ** 2 + H ** 2)

max_l = max(W, H, D)

for _ in range(N):
    matches = int(input())
    if matches <= max_l:
        print('DA')
    else:
        print('NE')