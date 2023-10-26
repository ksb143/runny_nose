def game(idx, start, rink):
    if len(start) == len(rink) == N/2:
        # print(start)
        # print(rink)
        answer.append(abs(sum(start)-sum(rink)))
        # 리스트 2개 만들어서 각각 더한담에 두 리스트 차이 answer리스트에 넣기!
        return
    if idx >= N:
        return
    for i in range(idx+1, N):
        game(idx+1, start + [S[idx][i]] + [S[i][idx]], rink)
        game(idx+1, start, rink + [S[idx][i]] + [S[i][idx]])

N = int(input())
# N은 짝수! N/2가 한 팀의 인원수
S = [list(map(int, input().split())) for _ in range(N)]
# 1번부터 있다고 나오는데 우리는 0부터 시작하니까 (N-1)까지가 표에 들어가는 수다!

answer = []
game(0, [], [])
print(min(answer))
# 링크와 스타트의 능력치 차이 최소화하기!
# 각 차이 점수 넣고 최소값 찾기