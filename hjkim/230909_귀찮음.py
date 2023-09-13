N = int(input())
data = list(map(int, input().split()))
data.sort()
total = sum(data)
cost = 0
for i in range(N):
    total -= data[i]
    cost += data[i] * total
print(cost)