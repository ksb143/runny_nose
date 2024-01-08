import sys

N = int(sys.stdin.readline())

stack = [0] * 10000

top = -1

# N개 만큼 명령어처리
for _ in range(N):
    lst = list(sys.stdin.readline().split())
    # push
    if lst[0] == 'push':
        top += 1
        stack[top] = int(lst[1])
    # pop
    elif lst[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    # size
    elif lst[0] == 'size':
        print(top + 1)
    # empty
    elif lst[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    # top
    elif lst[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])

