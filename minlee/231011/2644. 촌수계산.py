def DFS(A, B, count):
    global answer
    if A == B:
        answer = count
        return
    for i in family[A]:
        if not visited[i]:
            visited[i] = 1
            DFS(i, B, count+1)

N = int(input())
# 사람 수
A, B = map(int, input().split())
# 두 사람 번호
m = int(input())
# 부모 자식 간 관계 개수

family = [[] for _ in range(N+1)]
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
# 직계 가족끼리 표시하기

answer = -1
visited = [1] + [0]*(N)
DFS(A, B, 0)

print(answer)