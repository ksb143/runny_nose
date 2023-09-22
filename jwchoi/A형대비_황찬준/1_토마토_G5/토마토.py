# 유사한 느낌의 문제: 백준_유기농배추, 백준_미로탐색
# 유사한 개념: BFS(너비우선검색)-> 큐/덱 쓰기
from collections import deque
delta_r = [-1,1,0,0]
delta_c = [0,0,-1,1]


def tomato_bfs(row,col,arr):
    unripe = 0

    # 가야할곳의 좌표를 담는 빈덱 만들기(최초 시작좌표는 익은 토마토 자리를 탐색해서 찾아낸후 거기서!)
    dq = deque()

    # visited 만들기.
    vi = [[0] * col for _ in range(row)]

    # delta로 상하좌우 탐색

    for i in range(row):
        for j in range(col):
            # 만약 안익은 토마토를 찾았다면?
            if arr[i][j] ==0:
                # 안익은 토마토 수를 1 더해준다
                unripe += 1
            # 만약 익은 토마토를 찾았다면?
            elif arr[i][j] ==1:
                # 덱에 넣어서, 최초시작점으로 한다
                dq.append((i,j))
                # vi[] 함수에서 시작점을 1로 설정한다
                vi[i][j] = 1

            # 만약 빈칸을 찾았다면? 그냥 넘어간다
            elif arr[i][j] ==-1:
                continue

    # dq가 비어있지 않은 동안 반복
    while dq:
        # 현재 위치의 좌표를 cx,cy로 잡음(c:current)
        cr,cc  = dq.popleft() # (3,5)
        # 사방탐색
        for k in range(4):
            # new_x: 인접자리 x좌표, new_y: 인접자리 y좌표
            new_r, new_c = cr + delta_r[k], cc + delta_c[k]
            # 4방향으로, 2차원배열 범위내에서, 미방문한 자리 라면?
            if 0<= new_r < row and 0<= new_c < col and vi[new_r][new_c] == 0:
                # 그리고 안익은 토마토 라면?
                if arr[new_r][new_c]==0:
                    # 익은 토마토로 변하면서, 안익은 토마토 수가 1줄어든다
                    unripe -= 1
                    # 덱에, 그 안익은 토마토의 자리를 넣고, 다음에 탐색할 준비하기
                    dq.append((new_r, new_c))
                    # 곧 방문할 곳은 현재 방문한 곳의 값보다 1커지면 된다. (방문한 곳의 수)
                    vi[new_r][new_c]= vi[cr][cc]+1

    if unripe ==0:
        return vi[cr][cc]-1
    elif unripe !=0:
        return -1

# 인풋받기
m,n = map(int,input().split())
data = [list(map(int,input().split()))for _ in range(n)]
# print(data)
print(tomato_bfs(n,m,data))