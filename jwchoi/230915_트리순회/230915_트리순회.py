# 트리순회 1. 딕셔너리로 풀기
v = int(input())
r_l_r = {}
for _ in range(v):
    root, left, right = input().split()
    r_l_r[root]= [left, right]
print(r_l_r)