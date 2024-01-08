N = int(input())
lst = list(map(int, input().split()))
lst.sort()
time = 0
temp = 0
for p in lst:
    time += p
    temp += time

print(temp)