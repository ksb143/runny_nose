from collections import deque
def bfs():
    global cr, cc
    basket = deque()
    basket.append((cr,cc))
    times[cr][cc] = 0
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    while basket:
        front = basket.popleft()
        # print(front)
        for d in range(4):
            nr, nc = front[0] + directions[d][0], front[1] + directions[d][1]
            if 0 <= nr < height and 0 <= nc < width:
                if tomatoes[nr][nc] == 0:
                    if times[nr][nc] == 9999:
                        times[nr][nc] = times[front[0]][front[1]] + 1
                        basket.append((nr,nc))



width, height = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(height)]
# print(tomatoes)

# 1 익은 토마토
# 0 익지 않은 토마토
# -1 토마토 없음
times = [[9999]*width for _ in range(height)]

for row in range(height):
    for col in range(width):
        # 익은 토마토인 경우
        if tomatoes[row][col] == 1:
            times[row][col] = 0
            # 근처에 있는 안 익은 토마토까지의 거리만큼 times 를 바꿔주기
            cr, cc = row, col
            bfs()
        # 안 익은 토마토인 경우
        elif tomatoes[row][col] == 0:
            pass
        # 토마토가 없는 경우
        else:
            times[row][col] = 9990

max_v = -9999
for row in range(height):
    for col in range(width):
        if max_v < times[row][col]:
            max_v = times[row][col]
print(max_v)