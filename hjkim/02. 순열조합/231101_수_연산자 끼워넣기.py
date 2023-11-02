from collections import deque

# selected 의 idx 번째를 선택


def comb(idx, pick_num):
    if idx == pick_num:
        op_position.append(selected)
        # print(op_position)
        return

    for op in range(pick_num):
        if not visited[op]:
            selected[idx] = operators_full[op]
            visited[op] = 1
            comb(idx + 1, pick_num)
            visited[op] = 0


N = int(input())

numbers = deque(map(int, input().split()))

operators_num = deque(map(int, input().split()))

operators = ['+', '-', '*', '//']
operators_full = deque()
for el in range(4):
    if operators_num[el]:
        operators_full.append(operators[el] * operators_num[el])
# print(operators_full)

M = len(operators_full)
# print(M)

selected = [0] * M
op_position = []
visited = [0] * M
comb(0, M)


# print(visited)

results = []

val = numbers[0]
numbers.popleft()

while numbers:
    # 뽑을 게 없을 때까지
    if not numbers:
        # 끝났으면 반복을 끝내기
        break
    # 연산자 (operators_full) 에서 하나 뽑고
    op = operators_full.popleft()

    # 피연산자 (numbers) 에서 하나 뽑고
    num = numbers.popleft()

    # 연산자가 무엇인지에 따라서 계산해주고 (value)
    if op == '+':
        val += num
    elif op == '-':
        val -= num
    elif op == '*':
        val *= num
    elif op == '//':
        val //= num
    # 끝났으면 이번 턴 값을 results 에 저장
    results.append(val)

# 마지막에 돌면서 최대 최소 구하기
# print(results)
# print(max(results))
# print(min(results))