from collections import deque
# 디큐쓰면 더 빠르게 할 수 있다는 사실! 명심!
def team(num, start):
    global real_answer
    # 작은 값 비교해야하니까
    rink = deque()
    # 링크팀
    start_point = 0
    rink_point = 0
    # 각 팀별 점수 구하기 위한 변수
    if len(start) == N//2:
        # 전부 팀을 꾸렸으면
        for i in range(N):
            if i not in start:
                rink.append(i)
            # start팀에 없는 친구들 rink로 배치해주기

        # ★★ 팀별 점수 더해주기!!!!
        # 주어진 리스트(S)가 멤버들 에너지 합을 알려주는 거라서 그거 사용하면 된다.
        for i in start:
            for j in start:
                start_point += S[i][j]
        for i in rink:
            for j in rink:
                rink_point += S[i][j]
        # 차이값 비교하기
        # for문이 다 끝나고 해야지 전체 포인트 점수를 볼 수 있습니다.
        gap = abs(start_point - rink_point)
        # 최소값만 담아주면 됩니다.
        # global이라서 값을 계속 바꿀 수 있다.
        real_answer = min(gap, real_answer)
        return
    if num >= N:
        # 인덱스를 넘어가는 범위면 안되니까
        return
    # 조합 만드는 느낌!
    team(num+1, start+[num])
    team(num+1, start)


N = int(input())
# N은 짝수! N/2가 한 팀의 인원수
S = [list(map(int, input().split())) for _ in range(N)]
# 1번부터 있다고 나오는데 우리는 0부터 시작하니까 (N-1)까지가 표에 들어가는 수다!

real_answer = 10**1000  # 0xffffffff
# 필요 없는 값 저장하지 않기 위해서 팀별 점수 차이 최소값이랑 비교하기
team(0, [])
print(real_answer)
# 제일 적은 값 프린트합시다!