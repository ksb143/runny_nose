N = int(input())
board = [[0] * N for _ in range(N)]

def nqueen(row):
    global cnt
    if row == N:
        cnt += 1
        return
    # 해당 row에 모든 col에 퀸 놓아보기
    for col in range(N):
        # 열, 대각선에 모두 퀸이 없으면 놓을 수 있음
        if not col_check[col] and not dia1_check[row+col] and not dia2_check[N-1 + row - col]:
            col_check[col] += 1
            dia1_check[row + col] += 1
            dia2_check[N-1 + row - col] += 1
            nqueen(row+1)
            # 해당 col에 놓을 수 없으면 다음 col 넘어갈 때 그전에 col에 넣었던 것 초기화
            col_check[col] -= 1
            dia1_check[row+col] -= 1
            dia2_check[N-1 + row - col] -= 1


# 열 체크
col_check = [0] * N
# 대각선 체크
# r + c
dia1_check = [0] * (2 * N - 1) 
# r - c
dia2_check = [0] * (2 * N - 1)
# n-queen 개수 세는 변수
cnt = 0
nqueen(0)
print(cnt)

