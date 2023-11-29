import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# 안하면 런타임 에러 난다

# 1번 칸에 2개 들어있는거 한쪽씩 보기(DFS)
# 한 번호는 그거 칸대로 연결
def DFS(node):
    for i in tree[node]:
        if not visited[i]:
            visited[i] = 1
            parents[i] = node
            # 계속 내려가게 되니까 부모만 들어가게 되는 것!
            DFS(i)


N = int(input())
tree = [[] for _ in range(N+1)]
# N개의 리스트 만들어진다.
# 1은 트리의 루트다
parents = [0 for i in range(N+1)]
# 부모 구하는 문제니까
for _ in range(N-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)
# 연결된 거 전부 리스트 넣어주기
visited = [1] + [0 for i in range(N)]
# DFS 돌릴거니까 visited 만들기

DFS(1)
# 1부터 시작해야지 에러나 숫자 오류 안난다

for i in range(2, N+1):
    print(parents[i])
