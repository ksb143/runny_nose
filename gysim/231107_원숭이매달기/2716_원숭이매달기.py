# 덩굴은 두개의 덩굴로 나눠질 수 있는데
# 끊어지지 않기 위해서는 나눠진 두 덩굴은 같은 수의 원숭이들이 매달려있어야한다
# 덩굴의 구조를 꺾쇠괄호로 표시할 수 있다
# 덩굴의 깊이는 25를 넘지 않는다
# 덩굴의 균형을 유지하면서 꼭대기에 도달할 수 있는 최소 원숭이 수를 알고 싶다
# 꼭대기에 도달하기 위해서 최소 한마리 원숭이가 필요
from collections import deque

tc = int(input())
for _ in range(tc):
    tree = input()

    if not tree:
        print(1)
        continue

    level = 0
    max_level = 0
    stack = deque()

    for t in tree:
        if t == '[':
            stack.append(t)
            level += 1
            max_level = max(level, max_level)
        else:
            stack.pop()
            level -= 1

    monkey = 1
    for j in range(max_level):
        monkey *= 2

    print(monkey)
