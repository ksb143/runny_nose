# 비트 연산자 1 << n 이란 1을 n번 밀라는 뜻

def solve(N, ts, tb, min_v):
    # 공집합을 없애기 위해서 1부터 시작
    for i in range(1, 1<<N):
        for j in range(N):
            # 비트 & 연산 통해서 1 있는지 검사하고 1이면 해당 재료 넣기
            if i&(1<<j):
                ts *= sour[j]
                tb += bitter[j]
        # 해당 연산자가 최소값보다 작으면 바꿔주기
        if min_v > abs(ts - tb):
            min_v = abs(ts - tb)
        # ts, tb 초기화
        ts = 1
        tb = 0
    return min_v

N = int(input())

sour = []
bitter = []
min_v = 0xffffffff
ts = 1
tb = 0

for tc in range(N):
    S, B = map(int, input().split())
    sour.append(S)
    bitter.append(B)

print(solve(N, ts, tb, min_v))
