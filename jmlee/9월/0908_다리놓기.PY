import math

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    # 조합을 구하는 문제라고 판단하여.
    ans = math.factorial(M)//(math.factorial(N)*math.factorial(M-N))    # 조합 공식을 내장함수로 때려버림
    print(ans)  # 답 나옴