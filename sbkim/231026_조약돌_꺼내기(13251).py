M = int(input())
colors = list(map(int, input().split()))
N = sum(colors)
K = int(input())

per = 0

for color in colors:
    n = N
    color_per = color / n
    color -= 1
    n -= 1
    for i in range(K-1):
        color_per *= color/ n
        color -= 1
        n -= 1
    per += color_per

print(per)