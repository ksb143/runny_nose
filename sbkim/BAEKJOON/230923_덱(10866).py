from collections import deque
import sys

dq = deque()

N = int(input())

for _ in range(N):
    lst = sys.stdin.readline().split()
    if len(lst) == 2:
        command, num = lst[0], lst[1]
    else:
        command = lst[0]

    if command == 'push_front':
        dq.appendleft(num)
    elif command == 'push_back':
        dq.append(num)
    elif command == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif command == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif command == 'size':
        print(len(dq))
    elif command == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])

