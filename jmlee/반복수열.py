# 반복수열

A, P = map(int, input().split())
D = [A]           # 시작점 무조건 담아주기

while True:         # 반복문을 계속 돌려라
    multi_sum_v = 0  # multi_sum_v 0으로 초기화하기
    num = len(str(D[-1])) # 맨 마지막 숫자 자릿 수 구하기
    point = str(D[-1])
    # 각 자리 숫자를 P번 곱한 수들의 합을 D에 append
    for i in range(num):      # D의 맨 마지막 숫자의
        multi_sum_v += int(point[i]) ** P   # 각 자리 숫자를 P번 곱하고
    if multi_sum_v in D:    # multi_sum_v가 D안에 있다 = 같은 수다 = 뒤에 값 같을 것
        break
    else:
        D.append(multi_sum_v)            # 값을 D에 append하기

print(D.index(multi  _sum_v))