def group_maker(data,N): # 그래프 정점 N개를 넣으면, 최대 N개를 선택해 반환하는 조합함수
    for i in range(1<<N): # 2진수로 나타낸 모든 경우의수
        chosen = []
        for j in range(N): # 고를 원소의 갯수
            if i & (1<<j):
                chosen.append(data[j]) # 해당하는경우만 chosen에 담기
        print(chosen)
        return

def is_connected(data,v): # DFS 형태로, 그래프가 연결되어 있는지 확인하여 틀리면 -1을 반환, 맞으면 1을 반환
    should_visit=[] # 스택구조로 사용할예정
    top = -1 # 스택의 가장 위쪽 인덱스
    visited = [0]*(N+1)
    # 노드v를 방문하면, visited[v]를 1로 변경하고, v 인접 노드를 should_visit에 넣는다
    visited[v] = 1
    for i in range(1,N+1):
        for j in range(1,data[i][0]+1):
            should_visit.append(data[i][j])
            print(should_visit)
            print(visited)
            print()
    return

N = int(input())
popul = [0]+list(map(int,input().split())) # [0, 5, 2, 3, 4, 1, 2]
adj = [[]] # [[], [2, 2, 4], [3, 1, 3, 6], [2, 2, 4], [2, 1, 3], [1, 1], [1, 2]]
for _ in range(N):
    adj.append(list(map(int,input().split())))
print(popul)
print(adj) # input 종료
# 2개의 연결된 지역구로 나눌수 있는가? # 없다면 -1을 반환
if [0] in adj:
    result = -1
# 2개의 지역구로 나눈다->지역구 그룹간 인구차가 가장 적은가? # 아니라면 가장작은 케이스를 더 탐색하라
else:
    is_connected(adj,1)

# ->두 지역구는 연결된 형태로 존재하는가? # 아니라면 -1을 반환
# ->맞다면 정답을 반환
# 주의할점: 인구차 계산 과정은 좀더 뒤로 미뤄야함.