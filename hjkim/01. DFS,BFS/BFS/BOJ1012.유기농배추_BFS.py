# 지난주 금요일에 풀었던 섬 개수 찾는 문제랑 똑같음
def bfs():
    cr, cc = 0, 0
    queue = []
    queue.append((cr, cc))

    while queue:
        next = queue.pop(0)
        if check[next[0]][next[1]] != 0 and land[next[0]][next[1]] == 1:
            check[next[0]][next[1]] = 1
            cr, cc = next[0], next[1]


def dfs():
    pass
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
    # dfs 로 탐색
    dfs()