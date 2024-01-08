# 시간 초과가 자꾸나서 sys 및 deque 사용
import sys
from collections import deque

# dfs 재귀로 돌리기
def dfs(start, visited):
    # stack 만들기
    stack = deque([start])
    # visited 체크
    visited[start] = 1
    while stack:
        top = stack[-1]
        # 인접행렬 돌리는데,
        for i in range(1, N+1):
            # 방문하지 않았으면 방문 처리 및 스택에 넣기
            if link[top][i] == 1 and not visited[i]:
                visited[i] = 1
                stack.append(i)
                break
        # 해당 인접행렬에 있는 요소를 모두 방문했을 경우
        else:
            stack.pop()

N, M = map(int, sys.stdin.readline().split())

link = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    link[u][v] = 1
    link[v][u] = 1

visited = [0] * (N+1)
cnt = 0

# 0번째 요소는 없으니 1부터 돌린다!
for start in range(1, N+1):
    # 방문하지 않으면 함수 돌리기 :)
    if not visited[start]:
       dfs(start, visited)
       # 함수를 돌리고 cnt 증가
       cnt += 1

print(cnt)
