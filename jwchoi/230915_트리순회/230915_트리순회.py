def int1(): return int(input())


def strs(): return input().split()


n = int1()
xs = [strs() for _ in range(n)]


def build_graph(xs):
    d = {}
    for root, L, R in xs:
        L = None if L == '.' else L
        R = None if R == '.' else R
        d[root] = [L, R]
    return d


g = build_graph(xs)

preorder_result = []
inorder_result = []
postorder_result = []


def order_search(g, start='A'):
    if start == None: return

    preorder_result.append(start)
    order_search(g, g[start][0])
    inorder_result.append(start)
    order_search(g, g[start][1])
    postorder_result.append(start)


order_search(g)

for trace in [preorder_result, inorder_result, postorder_result]:
    print(''.join(trace))