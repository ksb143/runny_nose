# 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다.
# 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

# BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
# 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며,
# i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

# 축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.

# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다.
# 각 줄은 N개의 수로 이루어져 있고,
# i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고,
# 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

from collections import deque


# 중복 없는 조합
def comb(idx, cnt, check):
    global min_diff
    if cnt == N // 2:
        # print(check)
        # 2명 뽑아서 능력치 뽑아내기 캬하하ㅏㅎ
        team1, team2 = deque(), deque()
        for i in range(N):
            if check[i] == 1:
                team1.append(i)
            else:
                team2.append(i)
        team1_ability, team2_ability = 0, 0
        for i in range(N//2):
            for j in range(N//2):
                # 중복 방지 코드 (대각선만 구해요)
                if i < j:
                    team1_ability += S[team1[i]][team1[j]] + S[team1[j]][team1[i]]
                    team2_ability += S[team2[i]][team2[j]] + S[team2[j]][team2[i]]

        diff = abs(team1_ability - team2_ability)
        if diff < min_diff:
            min_diff = diff
        return

    if idx == N:
        return

    check[idx] = 1
    comb(idx+1, cnt+1, check)
    check[idx] = 0
    comb(idx+1, cnt, check)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

check = [0] * N

min_diff = 0xffffffff

# 0번째 idx를 안 뽑았다 치기
comb(1, 0, check)

print(min_diff)