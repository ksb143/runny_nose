N = int(input())

for i in range(N):
    star = '*' * (i + 1)
    print(star.rjust(N))