def dfs_iter(start):
    vi = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in vi:
            vi.add(node)
            stack.extend(graph[node])
    return vi

v, e = map(int,input().split())
graph = {}
for _ in range(e):
    parent, child = map(int,input().split())
    if parent not in graph:
        graph[parent] = set([child])
    else:
        graph[parent].add(child)
    if child not in graph:
        graph[child] = set([parent])
    else:
        graph[child].add(parent)
# print(graph)
ans = set()
for i in range(1,6+1):
    ans.add(frozenset(dfs_iter(i)))

print(len(ans))