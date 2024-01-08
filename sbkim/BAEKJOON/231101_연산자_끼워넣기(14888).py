# 수의 개수
N = int(input())

# 수 리스트
numbers = list(map(int, input().split()))
val = numbers[0]

# 덧셈, 뺄셈, 곱셈, 나눗셈 딕셔너리 구성
operators = {}

temp = list(map(int, input().split()))
for i in range(4):
    operators[i] = temp[i]

max_v = -1000000000
min_v = 1000000000


def cal(idx, N, numbers, operators, val):
    global max_v, min_v
    # 종료 조건
    if idx == N:
        if val > max_v:
            max_v = val
        if val < min_v:
            min_v = val
        return
    # 종료되지 않았으면 연산자 넣어주고 계산
    for key in operators.keys():
        # 해당 연산자가 없으면 continue
        if not operators[key]:
            continue
        # 값을 변형시킬 임시 값
        temp = val
        # 연산자가 있으면 각 연산자별로 계산하기
        if key == 0:    # 덧셈
            val += numbers[idx]
        elif key == 1:  # 뺄셈
            val -= numbers[idx]
        elif key == 2:  # 곱셈
            val *= numbers[idx]
        else:   # 나눗셈
            # 양수일 때
            if val >= 0:
                val //= numbers[idx]
            # 음수일 때
            else:
                val = -(abs(val) // numbers[idx])
        # 해당 연산자 썼으니까 개수 빼기
        operators[key] -= 1
        # 재귀
        cal(idx+1, N, numbers, operators, val)
        # 되돌려주기
        val = temp      # val 값
        operators[key] += 1     # 연산자 개수


cal(1, N, numbers, operators, val)

print(max_v)
print(min_v)


