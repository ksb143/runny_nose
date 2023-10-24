
N = int(input())
people = [i for i in range(1, N + 1)]
visited = [0] * N

power = [list(map(int, input().split())) for _ in range(N)]

M = N // 2

score_a = 0
score_b = 0
result = 0xfffff

def comb(idx, cnt):

    global team_a, team_b, score_a, score_b, result

    # 내가 필요한 만큼 다 골랐다
    if cnt == M:
        #여기가 성공케이스
        ## 여기 로직을 짜기가 어려움 !!
        return

    if idx == N:
        return


    visited[idx] = 1
    comb(idx+1, cnt + 1)

    visited[idx] = 0
    comb(idx+1, cnt)

comb(0, 0)

# print(result)