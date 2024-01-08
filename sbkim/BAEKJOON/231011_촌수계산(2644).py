import sys
from collections import deque

def dfs(p1, p2, cnt):
    stack = [(p1, cnt)]
    check = [0]*(n+1)
    check[p1] = 1
    while stack:
        top, c = stack[-1]
        if top == p2:
            return c
        for i in kinship[top]:
            if not check[i]:
                # 해당 cnt에다가 1을 더해줘야 함
                stack.append((i, c+1))
                check[i] = 1
                break
        else:
            stack.pop()
    return -1



# 전체 사람 수
n = int(sys.stdin.readline())
kinship = {}
for i in range(1, n+1):
    kinship[i] = deque()

# 촌수 계산해야 하는 서로 다른 두 사람 번호
p1, p2 = map(int, sys.stdin.readline().split())
# 부모 자식들 간의 관계의 개수
m = int(input())

# 부모 자식 관계
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    kinship[x].append(y)
    kinship[y].append(x)

if p1 == p2:
    result = 0
else:
    result = dfs(p1, p2, 0)

print(result)
