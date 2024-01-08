# 조상 찾기
def searching_anc(value, ancestor):

    if value == 1:
        return

    for i in range(1, V+1):
        for j in tree[i]:
            if value == j:
                value = i
                ancestor.append(value)
                return searching_anc(value, ancestor)


# 공통 조상 찾기
def searching_canc():
    for i in range(len(a_parents)):
        for j in range(len(b_parents)):
            if a_parents[i] == b_parents[j]:
                return a_parents[i]


# 서브트리 세기
def preorder(root):
    global cnt
    cnt += 1
    if tree[root]:
        if tree[root][0]:
            preorder(tree[root][0])
    if len(tree[root]) == 2:
        if tree[root][1]:
            preorder(tree[root][1])

T = int(input())

for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    edges = list(map(int, input().strip().split()))
    tree = {}
    for i in range(1, V+1):
        tree[i] = []

    for i in range(0, E*2, 2):
        tree[edges[i]].append(edges[i+1])


    a_parents = []
    b_parents = []

    searching_anc(A, a_parents)
    searching_anc(B, b_parents)

    cc_anc = searching_canc()

    cnt = 0

    preorder(cc_anc)

    print(f'#{tc} {cc_anc} {cnt}')
