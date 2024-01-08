from collections import deque

def permutation(idx, N, ans, calculation):
    # 기저 조건 (모두 선택된 경우)
    if idx == N-1:
        total_cal.add(ans)
        return

    for i in range(N-1):
        if not checked[i]:
            lst_cal[idx] = calculation[i]
            temp = ans
            checked[i] = 1
            if lst_cal[idx] == '+':
                ans = ans + numbers[idx+1]
            elif lst_cal[idx] == '-':
                ans = ans - numbers[idx+1]
            elif lst_cal[idx] == '*':
                ans = ans * numbers[idx+1]
            else:
                ans = ans / numbers[idx+1]
            # 재귀 함수
            permutation(idx+1, N, ans, calculation)
            # 초기화
            ans = temp
            checked[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    add, subtract, multiply, divide = map(int, input().split())
    calculation = ['+'] * add + ['-'] * subtract + ['*'] * multiply + ['/'] * divide
    numbers = deque(map(int, input().split()))
    # 연산자 순열
    lst_cal = [None] * (N-1)
    # 연산자 사용 표시 리스트
    checked = [0] * (N-1)
    # 완성된 연산자 순열 담을 세트
    total_cal = set()

    permutation(0, N, numbers[0], calculation)

    max_v, min_v = max(total_cal), min(total_cal)

    print(f'#{tc} {max_v - min_v}')


