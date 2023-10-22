import collections

# 해야 할 일 :
# 자식을 인덱스로 놓고
# 부모를 그거에 딸린 리스트로 놓고..
# 하면 된다..

total_human = int(input())
start, end = map(int, input().split())
edges = int(input())
trees = [list(map(int, input().split())) for _ in range(edges)]

# family_trees 순회하면서 start 에서 출발해서 end 도착할 때까지 cnt 올리기
# family_trees  = {1 : [2,3],
#                  2 : [7,8,9],
#                  4 : [5,6]}

family_trees = collections.defaultdict(list)

for edge in range(edges):
    parent = trees[edge][0]
    child = trees[edge][1]
    family_trees[parent].append(child)

cnt = 0
# start 있으면 그 부모를 찾고
for key, value in family_trees.items():
    if start == value:
        # 딕셔너리의 value 가 start 일 때
        # key 값을 불러오기..
        key = parent
        cnt += 1
# 그 부모가 자식으로 존재하는 걸 찾고
        if key in value:
# 그 자식의 부모를 찾고
            if
# 반복하다가
# 부모가 end 면 멈추기
# 루트노드까지 갔는데도 end 가 안 나오면
# -1 출력하기