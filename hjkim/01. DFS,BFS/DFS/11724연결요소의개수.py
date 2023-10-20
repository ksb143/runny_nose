from collections import deque


def dfs(node):
    # 시작 노드 방문 표시하고 스택에 넣기
    visited[node] = 1
    path = deque()
    path.append(node)
    # 갈곳이 남아 있는 동안 반복하기
    while path:
        # 제일 최근에 넣은 노드 꺼내고 방문 표시
        now = path.pop()

        # 모든 인접 리스트 돌아보면서
        # 갈 수 있는 노드 있는지 보고 있으면 방문할 곳에 추가
        for edge in range(edges*2):
            if adj[edge][0] == now:
                next = adj[edge][1]
                if not visited[next]:
                    visited[now] = 1
                    path.append(next)

# DFS
nodes,edges = map(int, input().split())
# 인접리스트 adj 만들기
adj = [list(map(int, input().split())) for _ in range(edges)]
for i in range(edges):
    adj.append([adj[i][1], adj[i][0]])
# 연결 요소의 개수 구하기
# 시작 노드 1번으로 해서 DFS 하기
# 전체 다 돌 때까지 dfs 하는데 몇 번 들어가기 시작하는지 보기
visited = [0] * (nodes+1)
ans = 0
for node in range(1,nodes+1):
    if not visited[node]:
        dfs(node)
        ans += 1
print(ans)