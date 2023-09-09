n = int(input())
lst = list(map(int, input().split()))
lst.sort()
left = sum(lst)             # lst를 다 더한 수
cost = 0                    # 최소 비용을 저장할 변수
for i in range(n):
    left -= lst[i]
    cost += lst[i]*left     # 가장 작은 수 * 나머지 더한 값
print(cost)