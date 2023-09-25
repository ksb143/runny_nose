# 어떻게 풀것인가?
# 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다.
# 위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면,
# 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.
from collections import deque

# delta로 상하좌우 탐색
delta_r = [-1,1,0,0]
delta_c = [0,0,-1,1]

def bfs(N,DATA):
    # 가야할곳의 좌표를 담는 빈덱 만들기
    dq = deque()
    # visited 만들기.
    vi = [[0] * N for _ in range(N)]
    # 순회하기
    for r in range(N):
        for c in range(N):
            for k in range(10):
                if DATA[r][c] > k:
                    passs

    # # dq가 비어있지 않은 동안 반복
    # while dq:
    #     # 현재 위치의 좌표를 cx,cy로 잡음(c:current)
    #     cr,cc  = dq.popleft() # (3,5)
    #     # 사방탐색
    #     for k in range(4):
    #         # new_x: 인접자리 x좌표, new_y: 인접자리 y좌표
    #         new_r, new_c = cr + delta_r[k], cc + delta_c[k]
    #         # 4방향으로, 2차원배열 범위내에서, 미방문한 자리 라면?
    #         if 0<= new_r < row and 0<= new_c < col and vi[new_r][new_c] == 0:


# 인풋받기
n = int(input())
data = [list(map(int,input().split()))for _ in range(n)]
print(n,data)
# print(bfs(n,data))