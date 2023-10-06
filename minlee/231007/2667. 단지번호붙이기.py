# from collections import deque

def find_start(N):
    for i in range(N):
        for j in range(N):
            if jido[i][j] == 1:
                sx = i
                sy = j
                visited[sx][sy] = 1
                DFS(sx, sy, 1)
                return

def DFS(x, y, count):
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            if jido[nx][ny]:
                jido[nx][ny] = count
                DFS(nx, ny, count+1)
            else:
                DFS(nx, ny, count)
    # 가다가 0을 만나면 그대로 지원

N = int(input())
jido = [list(map(int, input())) for _ in range(N)]

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited =[[0]*N for _ in range(N)]

# 시작점 찾기
find_start(N)


# house = []
# queue = deque()
# queue.append((0, 0, 1))
#
# while True:
#     small_house = 0
#     x, y, count = queue.popleft()

print(jido)

# 어디서부터 어디까지 이런게 아니라서 전체 다 봐야하는 거 같아!
# 근데 그럼 어차피 이거 시작점을 마음대로 정해줘야하는 거 같기도..??
# 그럼 DFS로 봐야하는 건가?

# 연결된 건 같은 번호, 떨어진 건 다른 번호?
# 이거는 오히려 가까이 연결된 것들 다 보고 그 다음으로 넘어가서 해서
# BFS로 봐야하는 거 같기도??!

# DFS : 재귀를 돌면서 앞 뒤를 바꿔야한다(=>원상복구가 필요한 상황이라면?!)_순열처럼 (뽑았다가 안뽑아야하니까),,한 번 시작하면 멈출 수 없다!
# BFS : 횟수, 거리 등 그냥 세면 되는 거,, 처음부터 모든 경우의 수 따지기!,, DFS를 제외한 전부
