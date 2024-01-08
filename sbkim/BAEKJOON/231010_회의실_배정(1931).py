import sys

# 회의의 수
N = int(input())

meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 회의시간이 시작과 동시에 끝날 수도 있기 때문에 3 3, 1 3, 3 3 인 경우에는 3 3만 넣고 끝나기 때문에 시작시간도 후에 정렬해줌
meetings.sort(key=lambda x: (x[1], x[0]))

# 현재 end 위치
current_end = 0
# 회의 수
cnt = 0

for s, e in meetings:
    # 시작 시간보다 이미 현재 회의 시간 끝보다 같거나 더 늦게하면 넣고 회의시간 끝을 바꿔주기
    if current_end <= s:
        current_end = e
        cnt += 1

print(cnt)
