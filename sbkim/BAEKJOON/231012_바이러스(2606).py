num = int(input())
network = int(input())

graph = [[] for _ in range(num+1)]
check = [0] * (num + 1)

# 인접리스트에 수를 집어넣는 반복문
for i in range(network):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 재귀형식 (DFS)
def virus(first):
    check[first] = 1
    for n in graph[first]:
        if check[n] == 0:
            virus(n)

virus(1)
print(sum(check)-1)