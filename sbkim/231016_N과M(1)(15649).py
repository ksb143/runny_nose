# pop, append 작업이 많아서 deque로 작업
from collections import deque


def comb(N, M, check, temp):
    # 종료 조건
    if M == 0:
        print(*temp)
        return
    for i in range(1, N+1):
        #  해당 함수 사용 안했으면
        if check[i] == 0:
            # 임시로 수열을 넣을 리스트에 넣어주기
            temp.append(i)
            # 넣었으니 체크하기
            check[i] = 1
            # 길이 하나 줄이기
            M -= 1
            # 재귀
            comb(N, M, check, temp)
            # 다시 되돌리기
            temp.pop()
            check[i] = 0
            M += 1


# N까지 수를 길이가 M인 수열을 모두 구하기 위해 N, M을 받아옴
N, M = map(int, input().split())
# 수열 썼는지 체크할 리스트
check = [0] * (N+1)
# 한개의 수열을 임시로 저장할 변수
temp = deque()

comb(N, M, check, temp)

