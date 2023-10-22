# 사람 번호는 1~n까지 연속된 번호
n = int(input())
# 촌수를 계산해야하는 서로 다른 두 사람의 번호
A, B = map(int, input().split())
# 부모 자식들 간의 관계의 개수
m = int(input())
# 부모는 한 명만 주어진다
adj = {}
for i in range(1, n+1):
    adj[i] = []

for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

visited = [0] * (n+1)
stack = [A]
visited[A] = 1
ans = 0

while stack:
    now = stack.pop()

    if now == B:
        ans = visited[B]
        break

    for i in adj[now]:
        if not visited[i]:
            visited[i] = visited[now] + 1
            stack.append(i)

# 주어진 두 사람의 촌수 출력
# 촌수를 계산할 수 없으면 -1 출력
# print(adj)
print(ans-1)