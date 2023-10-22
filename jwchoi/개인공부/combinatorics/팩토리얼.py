# https://www.acmicpc.net/problem/10872
# 팩토리얼
N = int(input())

def fact(n):
    global ans
    # 종료조건
    # N 이 1이라면? 종료한다.
    if n == 1:
        ans = 1
        print(ans)
        return
    # 진행조건
    # N 이 2 이상이라면? 진행한다.
    else:
        ans = fact(n-1) * n
fact(N)
