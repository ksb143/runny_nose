# delta
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+리스트
    farm1):
    # M : 배추밭 가로길이, N : 배추밭 세로길이, K : 배추가 심어져 있는 위치의 개수
    M, N, K = map(int, input().split())
    # 배추밭  = [[0] * M for _ in range(N)]

    # 배추가 심어져 있는 위치 표시 (인접리스트 생성)
    lst = []
    for i in range(K):
        # X, Y : 배추의 위치
        X, Y = map(int, input().split())
        lst.append((X, Y))

    for j in range(K):
        farm[lst[j][1]][lst[j][0]] = 1

    # 방문표시 리스트
    visited = [[0] * M for _ in range(N)]

    # 배추밭 방문하면서
    # 연속적으로 이어진 부분 갯수 세기
    cnt = 0     # 지렁이 갯수
    for a in range(M):
        for b in range(N):
            check = farm[a][b]
            # 4방향 확인하기 (동서남북)
            for k in range(4):
                ni, nj = a+di[k], b+dj[k]
                # 인덱스 범위 내에 있으면서 방문하지 않았고 갈 곳이 있다면
                if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0 and farm[ni][nj] == 1:
                    visited[ni][nj] = 1
        else:
            cnt += 1

    print(cnt)