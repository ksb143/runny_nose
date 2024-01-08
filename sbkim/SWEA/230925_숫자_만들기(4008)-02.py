def permutation(idx, N, num):
    if idx == N-1:
        result.add(num)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            if i == 0:
                new_num = num + numbers[idx+1]
            elif i == 1:
                new_num = num - numbers[idx+1]
            elif i == 2:
                new_num = num * numbers[idx+1]
            else:
                new_num = int(num / numbers[idx+1])
            permutation(idx+1, N, new_num)
            # 초기화
            operators[i] += 1



T = int(input())

for tc in range(1, T+1):
    # 숫자 개수
    N = int(input())
    # 연산자 카드 개수 개수('+', '-', '*', '/') -> 항상 N-1 개
    operators = list(map(int, input().strip().split()))
    # 숫자
    numbers = list(map(int, input().strip().split()))
    # 최대 최소 값 구하기
    result = set()
    # 순열 함수
    permutation(0, N, numbers[0])
    ans = max(result) - min(result)
    print(f'#{tc} {ans}')
