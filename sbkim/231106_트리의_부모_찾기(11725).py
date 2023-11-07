from collections import deque

def bfs(tree):
    # 부모 담을 리스트
    parents = [0] * (N + 1)
    # 루트 노드의 자식 찾기
    queue = deque()
    for root_child in tree[1]:
        queue.append(root_child)
        parents[root_child] = 1
    # 나머지 노드의 자식 찾기
    while queue:
        # 큐에서 꺼내고 (LIFO)
        node = queue.popleft()
        # 해당 노드와 연결된 것 찾기
        for child in tree[node]:
            # 루트 노드인 1이 아니고 이미 부모를 찾은 노드가 아니라면...!
            if child != 1 and not parents[child]:
                queue.append(child)
                parents[child] = node
    return parents


N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    # 연결리스트에 노드 넣기
    tree[node1].append(node2)
    tree[node2].append(node1)

parents = bfs(tree)

for i in range(2, N + 1):
    print(parents[i])



