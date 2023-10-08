# DFS로 풀기
def DFS(i):
    for j in graph[i]:
        if not visited[j]:
            visited[j] = 1
            DFS(j)

N, M = map(int, input().split())
# N 정점 개수, M 간선 개수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    # 어차피 쭉 다 가볼거고, 둘 다 연결된 거니까 하나만 넣어도 된다고 생각!
    # 근데 아님..!! 이거 관련 반례가 있었음(6 2/ 3 4/ 4 2)

visited = [1] + [0] * (N)
# 어차피 0번째는 안쓰니까
count = 0
# 처음 시작점에서 카운트하고 계속 가보고 끝나면 다음 차례로!

for i in range(N+1):
    if not visited[i]:
        visited[i] = 1
        count += 1
        DFS(i)
print(count)