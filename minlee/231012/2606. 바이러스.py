N = int(input())
node = int(input())
computers = [[] for _ in range(N+1)]
for _ in range(node):
    x, y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)
# 이거 더 간단하게 담을 수 있는 방법 없나..??

# 매번 재귀를 통해 풀어서 이번에는 stack으로
stack = [1]
count = 0
visited = [0]*(N+1)
visited[1] = 1

while stack:
    X = stack.pop()
    for i in computers[X]:
        if not visited[i]:
            visited[i] = 1
            count += 1
            stack.append(i)
            # BFS처럼 되어버렸네..?
print(count)