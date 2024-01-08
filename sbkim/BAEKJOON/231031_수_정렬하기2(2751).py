import sys

N = int(input())

numbers = [0] * N

for i in range(N):
    numbers[i] = int(sys.stdin.readline())

max_v = max(numbers)

# 최대값 K까지 활용
counts = [0] * (max_v + 1)

for i in range(N):
    counts[numbers[i]] += 1

for i in range(1, max_v+1):
    counts[i] += counts[i-1]

sorted_numbers = [0] * N
for i in range(N-1, -1, -1):
    counts[numbers[i]] -= 1
    sorted_numbers[counts[numbers[i]]] = numbers[i]

print(*sorted_numbers, sep='\n')

# numbers.sort()
#
# print(*numbers, sep='\n')

