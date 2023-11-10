# 루트 없는 트리가 주어진다
# 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하라
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())    # 노드의 개수
tree = defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0]*(N+1)


def dfs(start, parent):

    for node in tree[start]:
        if node != parent and not parents[node]:
            parents[node] = start
            dfs(node, start)


dfs(1, 0)

for i in range(2, N+1):
    print(parents[i])
