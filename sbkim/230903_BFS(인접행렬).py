# BFS 너비 우선 탐색
# 자신과 가까운 노드부터 탐색하는 방법으로 그렇기 때문에 큐를 활용하여 많이 탐색한다.
# 7 8 1
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

# 반복문 활용 1 (인접행렬)
def bfs(S, V):
    # 방문할 정점의 목록을 저장하는 queue를 만들어주기
    queue = []
    queue.append(S)
    # 방문 여부 표시하기 위한 visited 만들기
    visited = [0] * (V+1)
    while queue:
        # 정점에서 방문해서 길 찾고 길 찾으면 좀 있다가 방문할거니까 방문목록에 추가
        # 나머지 길 계속 찾기
        front = queue.pop(0)
        visited[front] = 1
        print(front, end=' ')
        # 인접행렬에서 연결된 정점 찾기
        for i in range(1, V+1):
            # i번 노드가 현재 정점과 연결되어 있고 방문하지 않았으면
            if adj[front][i] and not visited[i]:
                # 큐에 추가
                queue.append(i)
                # 방문 여부 표시
                visited[i] = 1
    print()

# V는 노드 개수, E는 연결된 정점 개수, S 시작할 노드
V, E, S = map(int, input().split())
# 연결된 정점
edges = list(map(int, input().split()))
# 인접행렬
adj = [[0] * (V+1) for _ in range(V+1)]
for i in range(0, E*2, 2):
    adj[edges[i]][edges[i+1]] = 1
    adj[edges[i+1]][edges[i]] = 1

bfs(S, V)