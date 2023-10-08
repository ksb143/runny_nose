from collections import deque

N, M = map(int, input().split())
# N은 정점 개수, M은 간선 개수
tree = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
# tree에 각 연결된 숫자들이 들어가 있을 것!

# 비지티드, 큐, 카운트 필요
visited = [0] * (N+1)
queue = deque()
count = 0

# 각 연결 노드들을 큐에 넣고(큐에 있는 거면 넣지 말기)
# 따라 가보다가
# 끝나면 연결된 거 카운트 세기
for i in range(1, N):
    for j in tree[i]:
        if not visited[j] and j not in queue:
            visited[j] = 1
            queue.append(j)
            while queue:
                k = queue.popleft()
                for m in tree[k]:
                    if not visited[m] and m not in queue:
                        visited[m] = 1
                        queue.append(m)
            count += 1
print(count)