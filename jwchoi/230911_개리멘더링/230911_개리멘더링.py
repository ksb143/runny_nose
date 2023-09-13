def dfs_iter(graph,start):
    global final
    # 방문 해야하는 노드목록을 빈 리스트로 생성해준다
    to_be_visited = [] # stack으로 사용예정
    diff_l = []
    # 시작: 시작점을 방문 --> 방문한 목록의 i번째를 True로 # 0번
    already_visited[start] = 1

    # 시작점과 인접한 노드를 --> 방문해야할 노드에 넣는다 # 2번,4번
    for i in range(graph[start][0]): # 0 ~ 1
        to_be_visited.append(graph[start][1+i]) # 1번째:2, 2번째:4

    # 만약, 아직 방문이 필요한 노드가 있다면?
    while to_be_visited: # 2,4
        # 그 중에서 가장 마지막 데이터를 추출(스택 자료구조 활용)
        node = to_be_visited.pop() # 4
        # 만약, 그 노드가 이미 방문한 목록에 없다면?
        if not already_visited[node]:
            # (방문했다고 가정하고) 이미 방문한 목록에 추가
            already_visited[node] = 1 # 4번 인덱스에 해당하는 값을 1 로 고정
            result = [already_visited[i] * popul[i] for i in range(N + 1)]
            sum_result = sum(result)
            diff = abs(total-2*sum_result)
            diff_l.append(diff)
            # print('기방문노드',already_visited)
            # print('result',result)
            # print('result의 합',sum_result)
            # print('diff',diff)
            # print()
            # 그 노드의 인접노드들을 방문해야할 목록에 append
            for i in range(graph[node][0]): # 0~0
                to_be_visited.append(graph[node][1+i])
    if already_visited != ([0] + [1]*N):
        final = -1
    final = min(diff_l)
    return

N = int(input()) # 정점의 갯수: 6
popul = [0]+ list(map(int,input().split())) #[0,5,2,3,4,1,2] <-- group1,2로 가르고 최종적으로 쓸지 or 중간에 바로 쓸지가 고민 지점
adj=[[]] # i번째 노드의 인접노드 갯수와, 인접노드 목록: [[],[2, 2, 4], [4, 1, 3, 6, 5], [2, 4, 2], [2, 1, 3], [1, 2], [1, 2]]
for _ in range(N):
    adj.append(list(map(int,input().split())))
# print(population)
# print(adj)
total = sum((popul))

result = []
already_visited = [0]*(N+1) # 이미 방문한 노드를 0,1로 표시한다 (인덱스와 노드순서를 일치시키기 위해 0번째는 버림)

start1 = 1
dfs_iter(adj,start1)
print(final)
# 시작점을 임의의 번호(예:1번)으로 잡은경우, Group1과 Group2로 분리하는게 쟁점이다
