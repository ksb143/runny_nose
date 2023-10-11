# 미로 거리 문제(swea) 도움됨
# 지난주 금요일에 풀었던 섬 개수 찾는 문제랑 똑같음
def bfs():
    # 시작점에서 시작 (bfs 는 재귀 형태가 아니라 while 문 내부에서 도는 형태라서 인자로 안 넣어줘도 됨)
    cr, cc = 0, 0
    # check 에 방문표시
    check[cr][cc] = 1
    # 시작점에서 갈 수 있는 지점을 queue 에 더해주기

    # queue.pop(0) 의 x,y 지점을 네 방향으로 갈 수 있음
    # 네 방향으로 갈 때 location 범위 내부인지 확인해주기
    # 네 방향으로 간 지점 값이 location 에서 1인지 확인하기 & 방문 안했는지 check 로 확인하기
    # 만약 배추가 있고 방문 안했으면, 방문할 지점으로 queue 에 append 해주기
    # queue 에 append 할 때 (col,row) 이런 형식으로 해야될지 아니면 [col,row] 이렇게 해야될지 아니면 어떻게 해야될지 잘 모르겠음


# def dfs():
#     pass

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    land = [[0]*M for _ in range(N)]
    location = [list(map(int, input().split())) for _ in range(K)]
    # 배추 위치 채우기
    for position in range(K):
        col = location[position][0]
        row = location[position][1]
        land[row][col] = 1
    # check 배열 만들어서 모든 지점 돌았는지 검사하기
    check = [[0]*M for _ in range(N)]
    # bfs 로 탐색
    bfs()
