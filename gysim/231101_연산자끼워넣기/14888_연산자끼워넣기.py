# N개의 수로 이루어진 수열이 주어진다
# 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다
# 연산자는 덧셈, 뺄셈, 곱셈, 나눗셈으로 이루어져 있다
# 수와 수 사이에 연산자를 하나씩 넣어서 수식을 만든다
# 주어진 수의 순서를 바꾸면 안된다
# 계산은 우선순위를 무시하고 앞에서부터 진행해야한다
# 나눗셈은 몫만 취한다
# 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
# 계산 결과가 최대인 것과 최소인 것을 구하기

N = int(input())   # 수의 개수
numbers = list(map(int, input().split()))       # N 개의 수
operators = list(map(int, input().split()))     # 연산자 개수, (+, -, *, //) 순서

max_v = -0xffffffff
min_v = 0xffffffff


def cal(idx, result):   # idx : 수열의 인덱스, result : 계산 결과
    global max_v, min_v

    if idx == N:    # 수열의 마지막 숫자까지 갔으면
        # 최대, 최소값 찾기
        max_v = max(max_v, result)
        min_v = min(min_v, result)
        return

    for i in range(4):  # 연산자 배열 순회
        if operators[i] > 0:    # 연산자가 남아있으면
            operators[i] -= 1   # 해당 연산자 사용
            
            # 연산자 배열 인덱스에 따라 재귀 인자에 계산 결과 넣어주기
            if i == 0:
                cal(idx+1, result+numbers[idx])

            elif i == 1:
                cal(idx+1, result-numbers[idx])

            elif i == 2:
                cal(idx+1, result*numbers[idx])

            elif i == 3:
                # 나눠지는 수가 음수이면
                if result < 0:
                    # 양수로 만들어서 나눈 후 마이너스를 붙인다
                    result = -(abs(result)//numbers[idx])
                else:
                    result //= numbers[idx]
                cal(idx+1, result)
            operators[i] += 1   # 해당 연산자 사용끝


cal(1, numbers[0])  # 숫자의 0을 초기값으로 설정해서 1부터 인덱스 출발
print(max_v)
print(min_v)
