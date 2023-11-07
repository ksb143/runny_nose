# 11725. 트리의 부모 찾기

from collections import deque

def bfs(tree):
    parents = [0] * (N+1)

    # 루트 자식 찾기
    queue = deque()
    for root in tree[1]:
        queue.append(root)
        parents[root] = 1

    # 자식 찾기
    while queue:
        c = queue.popleft()
        for child in tree[c]:
            if child != 1 and parents[child] == 0:
                queue.append(child)
                parents[child] = c
    return parents


N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    first, second = map(int, input().split())
    adj[first].append(second)
    adj[second].append(first)

parents = bfs(adj)
# print(parents)              # [0, 0, 4, 6, 1, 3, 1, 4]
for i in range(2, N+1):
    print(parents[i])