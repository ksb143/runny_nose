from collections import deque

N = int(input())                              # 수의 개수
# N = 2
numbers = deque(map(int, input().split()))     # 수열
# numbers = [5, 6]
operators_num = deque(map(int, input().split()))
# calc_num = [0,0,1,0]
operators = ['+', '-', '*', '//']
operators_full = deque()
for el in range(4):
    if operators_num[el]:
        operators_full.append(operators[el] * operators_num[el])
# operators = ['*']
M = len(operators) # 1
visited = [0] * M # [0]
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
print(max(results))
print(min(results))