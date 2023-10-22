def dfs(start):
    stack = [start]
    visited = [0] * (N+1)
    visited[start] = 1
    cnt = 0

    while stack:
        now = stack.pop()

        for i in adj[now]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                cnt += 1

    return cnt

# 컴퓨터의 수, 100이하인 양의 정수, 컴퓨터 번호는 1번부터 N번까지
N = int(input())
# 직접 연결되어 있는 컴퓨터 쌍의 수
M = int(input())
adj = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

cnt = dfs(1)

# 1번 컴퓨터가 바이러스에 걸렸을 때,
# 바이러스에 걸리게 되는 컴퓨터의 수를 출력
print(cnt)