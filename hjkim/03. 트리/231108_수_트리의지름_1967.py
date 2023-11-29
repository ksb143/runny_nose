# 트리의 지름 = 두 노드 사이의 경로의 길이들 중에서 가장 긴 것의 길이

n = int(input())  # n : 노드의 개수

# 부모 - 자식 - 간선의 가중치
tree = [list(map(int, input().split())) for _ in range(n-1)]
for node in tree:
    parent, child, length = node[0], node[1], node[2]

# 모든 노드들 중에 2개 고르기 - 중복 없는 조합이랑 동일함
nodes = [i for i in range(1, n + 1)]
selected = [] # nC2 개의 pair 가 나올 수 있음
# 노드가 총 3개일 경우
# 1 2 / 1 3 / 2 3  -- 3C2 = 3


# 2개 노드 간 경로의 길이 구하기 - 이 때 parent, child 등 관계 고려하기


# 모든 노드 pair 의 경로의 길이 중 최댓값 구하기