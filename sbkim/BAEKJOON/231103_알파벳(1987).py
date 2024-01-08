# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다.
# 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오.

from sys import stdin
from collections import deque

# R (row), C (column)
R, C = map(int, stdin.readline().split())
# 대문자 알파벳 -> 개행문자가 포함되어서 strip 포함
alpha = [list(stdin.readline().strip()) for _ in range(R)]


# 4방향 탐색
dr = (-1, 1, 0, 0)
dc = (0, 0 ,-1, 1)


def dfs(r, c):
    max_num = 0
    # 스택 만들기
    stack = deque()
    stack.append((r, c, 1, alpha[r][c]))

    # 스택이 빌 때까지
    while stack:
        cr, cc, cnt, word = stack.pop()
        # cnt가 max_num보다 큰 경우 바꿔주기
        if max_num < cnt:
            max_num = cnt
        # 4방향 탐색
        for i in range(4):
            # 다음 갈 곳 미리 넣어두고
            nr, nc = cr + dr[i], cc + dc[i]
            # 범위 안에 넣고 방문하지 않았을 경우, 해 위치 알파벳이 used_set에 없다면...?
            if 0 <= nr < R and 0 <= nc < C and alpha[nr][nc] not in word:
                # 해당 위치 알파벳이 lst에 없다면...? 방문 표시 및 스택에 넣고 그 알파벳 lst에 넣기
                stack.append((nr, nc, cnt+1, word+alpha[nr][nc]))

    return max_num

max_num = dfs(0, 0)

print(max_num)