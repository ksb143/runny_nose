# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 블록별로 핀볼 방향 바꾸기
cd = [[],
      [1, 3, 0, 2],     # 1번 블록
      [3, 0, 1, 2],     # 2번 블록
      [2, 0, 3, 1],     # 3번 블록
      [1, 2, 3, 0],     # 4번 블록
      [1, 0, 3, 2]]

def dfs(sr, sc):
    max_score = 0
    for i in range(4):
        cr, cc = sr, sc
        score = 0
        while True:
            cr, cc = cr + dr[i], cc + dc[i]
            if (cr, cc) == (sr, sc) or board[cr][cc] == -1:
                    break
            # 블록을 만났을 때
            elif 1 <= board[cr][cc] <= 5:
                score += 1
                i = cd[board[cr][cc]][i]
            # 웜홀을 만났을 때
            elif 6 <= board[cr][cc] <= 10:
                cr, cc = wormhole_info[(cr, cc)]
        # 최대값 구하기
        if max_score < score:
            max_score = score           
    return max_score
                

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 벽을 블록 5로 감싸기
    board = [[5] + list(map(int, input().strip().split())) + [5] for _ in range(N)]
    board.insert(0, [5]*(N+2))
    board.append([5]*(N+2))
    # 웜홀 쌍 정보 저장
    wormhole_check = [0] * 11
    wormhole_info = dict()      
    for i in range(1, N+1):
        for j in range(1, N+1):
            if 6 <= board[i][j] <= 10:
                num = board[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else:   # 같은 번호 웜홀끼리 위치 정보 저장
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]
    max_score = 0
    for r in range(1, N+1):
        for c in range(1, N+1):
            # 현재 위치
            sr, sc = r, c
            result = 0
            # 상하좌우 dfs 해보기(블럭이 없는 곳에서만 출발)
            if board[sr][sc] == 0:
                result = dfs(sr, sc)
            if max_score < result:
                max_score = result
    print(f'#{tc} {max_score}')       

