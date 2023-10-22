def preorder(idx):
    global pre_tmp

    if len(pre_tmp) == N:
        return pre_tmp

    # 루트노드더하기
    pre_tmp += parent[idx]

    # 왼쪽 자식이 있으면
    if left[idx] != '.':
        for i in range(N):
            if left[idx] == parent[i]:
                preorder(i)

    if right[idx] != '.':
        for i in range(N):
            if right[idx] == parent[i]:
                preorder(i)


def inorder(idx):
    global in_tmp

    if len(in_tmp) == N:
        return in_tmp

    # 왼쪽 자식이 있으면
    if left[idx] != '.':
        for i in range(N):
            if left[idx] == parent[i]:
                inorder(i)

    # 루트노드더하기
    in_tmp += parent[idx]

    if right[idx] != '.':
        for i in range(N):
            if right[idx] == parent[i]:
                inorder(i)


def postorder(idx):
    global post_tmp

    if len(post_tmp) == N:
        return post_tmp

    # 왼쪽 자식이 있으면
    if left[idx] != '.':
        for i in range(N):
            if left[idx] == parent[i]:
                postorder(i)

    if right[idx] != '.':
        for i in range(N):
            if right[idx] == parent[i]:
                postorder(i)

    # 루트노드더하기
    post_tmp += parent[idx]


# 이진트리의 노드의 개수
N = int(input())

parent = [None] * N
left = [None] * N
right = [None] * N

for i in range(N):
    # 노드이름, 왼쪽자식노드, 오른쪽자식노드
    tmp = input().split()
    parent[i] = tmp[0]
    left[i] = tmp[1]
    right[i] = tmp[2]

pre_tmp = ''
preorder(0)
print(pre_tmp)

in_tmp = ''
inorder(0)
print(in_tmp)

post_tmp = ''
postorder(0)
print(post_tmp)
