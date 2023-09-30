# 전위순회 : 루트 -> 왼쪽 자식 -> 오른쪽 자식
# i번째 노드의 값을 출력하기 -> 왼쪽 자식 함수 호출 -> 오른쪽 자식 함수 호출
N = int(input())
tree = {}

for n in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]


def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right


def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root


preorder('A')
print()
inorder('A')
print()
postorder('A')