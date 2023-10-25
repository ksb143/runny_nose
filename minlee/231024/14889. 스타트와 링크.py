def game(idx, start, rink):
    if len(start) == len(rink) == N/2:
        # print(start)
        # print(rink)
        answer.append(abs(sum(start)-sum(rink)))
        # 리스트 2개 만들어서 각각 더한담에 두 리스트 차이 answer리스트에 넣기!
        return
    if idx >= N:
        return



N = int(input())
# N은 짝수! N/2가 한 팀의 인원수
S = [list(map(int, input().split())) for _ in range(N)]
# 1번부터 있다고 나오는데 우리는 0부터 시작하니까 (N-1)까지가 표에 들어가는 수다!

# 각 수 반대로 더한 거 총합계에 들어간다!

# 팀을 먼저 구성 후 그걸 가지고 점수를 넣도록!
# N/2개 묶음 조합


answer = []
start = []
rink = []

game(0, [], [])
print(min(answer))
# 링크와 스타트의 능력치 차이 최소화하기!
# 링크 점수 넣고
