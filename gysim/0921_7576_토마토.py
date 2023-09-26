# queue를 그냥 리스트로 하면 시간초과 나서 deque 씀
from collections import deque


def bfs():
    queue = deque()

    # 시작지점 전부 queue에 넣기
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                queue.append((i, j))

    while queue:
        i, j = queue.popleft()

        # 상 하 좌 우 확인
        for d in range(4):
            ni, nj = i + delta[d][0], j + delta[d][1]
            if 0 <= ni < N and 0 <= nj < M and not tomato[ni][nj]:
                queue.append((ni, nj))
                # 날짜 구하려면 누적해서 더해주기
                tomato[ni][nj] = tomato[i][j] + 1

    # 모든 방문이 끝난 후
    max_v = 0
    for i in range(N):
        for j in range(M):
            # 토마토가 모두 익지는 못하는 상황이면 -1 출력
            if tomato[i][j] == 0:
                return -1

            if tomato[i][j] > max_v:
                max_v = tomato[i][j]

    # 만약 저장될때부터 모든 토마토가 익어있는 상태면 0 출력
    # 시작지점을 1로 시작했기 때문에 날짜를 구하려면 -1 해줘야함
    return max_v - 1


# M : 상자의 가로 칸 수, N : 상자의 세로 칸 수
M, N = map(int, input().split())
# 1 : 익은 토마토, 0 : 익지않은 토마토, -1 : 토마토 없음
tomato = [list(map(int, input().split())) for _ in range(N)]

# 익은 토마토의 왼쪽, 오른쪽, 앞, 뒤의 토마토는 하루가 지나면 익음
# 상 하 좌 우
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 토마토가 모두 익을 때까지의 최소 날짜 출력
ans = bfs()
print(ans)
