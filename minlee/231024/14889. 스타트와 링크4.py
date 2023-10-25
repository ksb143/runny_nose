from collections import deque

def team(num, start):
    global real_answer

    start_point = 0
    rink_point = 0

    if len(start) == N//2:
        rink = deque()
        for i in menber:
            if i not in start:
                rink.append(i)

            # ★ 대각선 구해서 밑의 것도 더해주기!!
        for i in start:
            # 중복 방지((0,1)과 (1,0) 한 번에 들어가는 거니까 중복할 필요 없다!)
            for j in start:
                start_point += S[i][j]
        for i in rink:
            # 중복 방지((0,1)과 (1,0) 한 번에 들어가는 거니까 중복할 필요 없다!)
            for j in rink:
                rink_point += S[i][j]
        # print(start_point, rink_point)
        gap = abs(start_point - rink_point)
        # print(gap)
        real_answer = min(gap, real_answer)
        # real_real_answer.add(real_answer)
        return
    if num >= N:
        return
    team(num+1, start+[menber[num]])
    team(num+1, start)
# 팀원 넣어주기
# N/2개 묶음 조합([start, rink]) 만들기!
# 각 요소별 더할 수 있도록 예상 작업!

# 각 요소별 더하는 방법 구하기
# def final_point(answer):
#     global real_answer
#     start_point = 0
#     rink_point = 0
#     for start, rink in answer:
#         # ★ 대각선 구해서 밑의 것도 더해주기!!
#         for i in range(N):
#             # 중복 방지((0,1)과 (1,0) 한 번에 들어가는 거니까 중복할 필요 없다!)
#             for j in range(N):
#                 start_point += S[start[i]][start[j]]
#                 rink_point += S[rink[i]][rink[j]]
#     gap = abs(start_point-rink_point)
#     if gap < real_answer:
#         real_answer = gap


N = int(input())
# N은 짝수! N/2가 한 팀의 인원수
S = [list(map(int, input().split())) for _ in range(N)]
# 1번부터 있다고 나오는데 우리는 0부터 시작하니까 (N-1)까지가 표에 들어가는 수다!

menber = [i for i in range(N)]
# 팀을 먼저 구성 후 그걸 가지고 점수를 넣도록!


answer = deque()
real_answer = 10**1000  # 0xffffffff
# real_real_answer = set()
team(0, [])
# final_point(answer)
print(real_answer)