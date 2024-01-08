def preorder(root, n):
    if root != '.':
        print(root, end='')
        if ch1[n] != '.':
            preorder(ch1[n], tree.index(ch1[n]))
        if ch2[n] != '.':
            preorder(ch2[n], tree.index(ch2[n]))

def inorder(root, n):
    if root != '.':
        if ch1[n] != '.':
            inorder(ch1[n], tree.index(ch1[n]))
        print(root, end='')
        if ch2[n] != '.':
            inorder(ch2[n], tree.index(ch2[n]))

def postorder(root, n):
    if root != '.':
        if ch1[n] != '.':
            postorder(ch1[n], tree.index(ch1[n]))
        if ch2[n] != '.':
            postorder(ch2[n], tree.index(ch2[n]))
        print(tree[n], end='')


N = int(input())

# 트리 내부에 있는 문자
tree = [0] * (N+1)
# 해당 트리의 자식 노드
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)

rm_set = {'.'}
for i in range(1, N+1):
    lst = input().split()
    tree[i] = lst.pop(0)
    if lst:
        ch1[i] = lst.pop(0)
    if lst:
        ch2[i] = lst.pop(0)
preorder('A', 1)
print()
inorder('A', 1)
print()
postorder('A', 1)