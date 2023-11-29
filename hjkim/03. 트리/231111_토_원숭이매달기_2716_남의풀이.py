# https://deveun.tistory.com/entry/Python%EB%B0%B1%EC%A4%80-2716%EC%9B%90%EC%88%AD%EC%9D%B4-%EB%A7%A4%EB%8B%AC%EA%B8%B0

import sys

tc = int(sys.stdin.readline().strip())

for _ in range(tc):
    op = sys.stdin.readline()

    maxDepth = 0
    tree = list()
    for o in op:
        if o == ']':
            maxDepth = max(len(tree), maxDepth)
            tree.pop()
        else:
            tree.append('[')

    print(2**maxDepth)