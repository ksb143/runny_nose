from collections import deque
# width, height 가 0 0 이면 입력이 끝임

def dfs():
    # island : 갈 수 있는 곳을 담는 스택
    island = deque()
    island.append((row,col))
    # 가로 세로 대각선 - 걸어갈 수 있음
    # 8방향 (상, 우상, 우, 우하, 하, 좌하, 좌, 좌상)
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    while island:
        cr, cc = island.pop()
        visited[cr][cc] = 1
        for d in range(8):
            nr, nc = cr + directions[d][0], cc + directions[d][1]
            if 0<= nr < height and 0<= nc < width:
                if my_map[nr][nc] and not visited[nr][nc]:
                    island.append((nr,nc))


while True:
    width, height = map(int, input().split())
    if width == 0 and height == 0:
        break
    my_map = [list(map(int, input().split())) for _ in range(height)] # 1 땅 0 바다
    visited = [[0] * width for _ in range(height)]
    cnt = 0
    for row in range(height):
        for col in range(width):
            # 방문 안했으면
            if not visited[row][col]:
                # 바다라면
                if not my_map[row][col]:
                    # 방문 체크
                    visited[row][col] = 1
                # 땅이라면
                else:
                    dfs()
                    # dfs 돌면서 갈 수 있는 곳 전부 가서 방문 체크해주기
                    cnt += 1
            # 방문 했으면 그냥 넘어가기
    print(cnt)