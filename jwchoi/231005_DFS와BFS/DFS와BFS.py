from collections import deque
# vi = visited = []
def dfs_iter(graph0,root0):
    vi0 = []
    stack = [root0]

    while stack:
        node0 = stack.pop()
        if node0 not in vi0:
            vi0.append(node0)
            stack.extend(graph0[node0])
    return vi0

def bfs_iter(graph1,root1):
    vi1 = []
    dq = deque([root1])

    while dq:
        node1 = dq.popleft()
        if node1 not in vi1:
            vi1.append(node1)
            dq.extend(graph1[node1])
    return vi1

v, e, st = map(int,input().split())
# 정점 간 관계는 인접행렬 or 인접리스트로 표시 가능함
# 딕셔너리의 value를 인접리스트로 해보자
# 딕셔너리의 특정 키에 해당하는 밸류에 기존 밸류는 놔두면서, 거기에 뭔가 추가하고 싶으면
# 처음에 밸류를 할당할 때, set으로 넣고, 이후에 다른 값을 넣을때,
# graph[key].add(추가로붙일값) 식으로 넣어야함.
graph = {}
for _ in range(e):
    parent, child =map(int,input().split())
    if parent not in graph:
        graph[parent] = set([child])
    else:
        graph[parent].add(child)
    if child not in graph:
        graph[child] = set([parent])
    else:
        graph[child].add(parent)
# print(graph) # {1: {2, 3, 4}, 2: {1, 4}, 3: {1, 4}, 4: {1, 2, 3}}
print(*dfs_iter(graph,st))
print(*bfs_iter(graph,st))
