def comb(idx, start, M):
    # 종료 조건
    if idx == M:
        print(*check)
        return
    for i in range(start, N+1):
        check[idx] = i
        # start를 한칸 밀어버림으로 써 같은 것을 뽑지 않음
        comb(idx+1, i+1, M)


# N까지 수를 길이가 M인 수열을 모두 구하기 위해 N, M을 받아옴
N, M = map(int, input().split())
# 수열 썼는지 체크할 리스트
check = [0] * M

comb(0, 1, M)


# pop, append 작업이 많아서 deque로 작업
from collections import deque


def comb2(N, M, check, temp, start):
    # 종료 조건
    if M == 0:
        print(*temp)
        return
    for i in range(start, N+1):
        #  해당 함수 사용 안했으면
        if check[i] == 0:
            # 임시로 수열을 넣을 리스트에 넣어주기
            temp.append(i)
            # 넣었으니 체크하기
            check[i] = 1
            # 길이 하나 줄이기
            M -= 1
            # 재귀
            comb2(N, M, check, temp, i+1)
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

comb2(N, M, check, temp, 1)

def comb3(idx, cnt, check):
    # 종료조건 M개 다 뽑았을 경우
    if cnt == M:
        for i in range(N+1):
            if check[i] == 1:
                print(i, end=' ')
        print()
        return
    # 종료조건 N개 다 뽑았을 경우
    if idx == (N+1):
        return

    check[idx] = 1
    comb3(idx+1, cnt+1, check)
    check[idx] = 0
    comb3(idx+1, cnt, check)

N, M = map(int, input().split())

check = [0] * (N+1)

comb3(1, 0, check)