from collections import deque
# visited 되어 있더라도 min 값으로 대체하기
# 익히는 데 걸리는 날짜 수 반환
# 어떤 안 익은 토마토가 익을 수 있는 경우의 수가 2가지면
# 더 작은 수로 갱신
def bfs(row,col):
    basket = deque()
    basket.append((row, col))
    visited[row][col] = 1
    while basket:
        cr, cc = basket.popleft()
        arrow = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for a in range(4):
            nr, nc = cr + arrow[a][0], cc + arrow[a][1]
            if 0 <= nr < height and 0 <= nc < width:
                if tomatoes[nr][nc] == 0:
                    basket.append((nr,nc))


width, height = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(height)]
# 1 익은 토마토 0 안 익은 토마토 -1 토마토 없음
# 익은 토마토가 있을 때 상우하좌 토마토를 cnt 일 후에 익게 됨
# BFS 로 토마토 익히기
# 종료 조건 :
# 처음부터 모든 토마토가 익어 있음 0
# 모든 토마토가 익었을 때 cnt 일(min)
# 익힐 수 있는 토마토가 없을 때 (-1 로 막힘) -1
visited = [[0]*width for _ in range(height)]
ans = 0
for row in range(height):
    for col in range(width):
        # 안 익은 토마토 찾았는데 주위에 다 -1 로 둘러싸여 있으면 다 익힐 수 없으므로 -1 반환
        if tomatoes[row][col] == 0:
            cr, cc = row, col
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            for d in range(4):
                nr, nc = cr + directions[d][0], cc + directions[d][1]
                if 0 <= nr < height and 0 <= nc < width:
                    # 안 익은 토마토 옆에 -1 아니면 0 혹은 1 이므로 익을 수 있음
                    # 탐색을 지속할 필요 없음
                    if tomatoes[nr][nc] != -1:
                        break
                    # 여기가 실행될 경우는 break 가 안 된 경우 (= 다 -1임)
                    ans = -1
        # 익은 토마토 찾았는데 방문 안했으면 주위 안 익은 토마토들 익히기
        elif tomatoes[row][col] == 1:
            bfs(row,col)
            ans = max(visited)
        # 처음부터 다 익은 토마토만 있는 경우
        elif tomatoes[row][col] == -1 or 1:
            ans = 0
print(ans)