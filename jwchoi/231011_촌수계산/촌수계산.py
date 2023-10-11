ans = 0
n = int(input())
print('사람수=',n) # 사람 수(정점 수)
p1,p2 = map(int,input().split())
print('타겟인간1,2=',p1,p2) # 타겟인간1, 타겟인간2
e = int(input())
print('관계수=',e) # 관계 수(간선 수)
reversed_graph = {}
for _ in range(e):
    parent, child = map(int,input().split())
    # if parent not in graph:
    #     graph[parent] = set([child])
    # else:
    #     graph[parent].add(child)
    if child not in reversed_graph:
        reversed_graph[child] = set([parent])
    else:
        reversed_graph[child].add(parent)
print('부모-자식 간 그래프',reversed_graph)
if p1 == p2:
    ans = 0
else:
    while asc1 != asc2:
        asc1 = reversed_graph[p1]

