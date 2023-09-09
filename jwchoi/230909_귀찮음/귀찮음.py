N = int(input())
data = list(map(int,input().split())) # [3,5,4,2]

result = 0
data0 = data[:]

for i in range(N-1): # 0 1 2
    sum0 = 0
    for j in data[i+1:]:
        sum0 += j
    result += (data[i] * sum0)
print(result)