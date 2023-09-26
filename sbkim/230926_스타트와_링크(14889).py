N = int(input())

abilities = [list(map(int, input().split())) for _ in range(N)]
people = [x for x in range(N)]

min_diff = 0xffffffff

# subset 구하기
# 공집합인 것을 없애기 위해 비트마스킹 1부터 시작
for i in range(1, (1<<N)//2):
    team1 = [0] * N
    team2 = [0] * N
    for j in range(N):
        if i & (1<<j):
            team1[people[j]] = 1
        else:
            team2[people[j]] = 1
    ability1 = 0
    ability2 = 0
    # 팀1의 능력치
    for x1 in range(N):
        if team1[x1] == 0:
            continue
        for y1 in range(N):
            if team1[y1] == 1:
                ability1 += abilities[x1][y1]
    # 팀2의 능력치
    for x2 in range(N):
        if team2[x2] == 0:
            continue
        for y2 in range(N):
            if team2[y2] == 1:
                ability2 += abilities[x2][y2]
    diff = abs(ability1 - ability2)
    if min_diff > diff:
        min_diff = diff
print(min_diff)