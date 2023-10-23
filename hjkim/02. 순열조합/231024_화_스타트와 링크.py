# total_people : 짝수
# N / 2 명 으로 teamA, teamB 나눔
# teamA, teamB 간 능력치 최소화하고 차를 출력
def comb(start, cnt):

    # teamA 다 골랐으면 탐색 중단하고 나머지는 teamB 로 보내기
    if cnt == pick_num:
        return

    # Index Error 방지
    if start == total_people:
        return

    # person : start 부터 마지막까지 번호 사람들 중에 고를 사람의 번호
    for person in range(start, total_people):
        selected[person] = 1



total_people = int(input())
power = [list(map(int, input().split())) for _ in range(total_people)]
# power[r][c] 랑 power[c][r] 은 다름

# 풀이 방법
# 순열과 조합
# pick_num = 팀 멤버 수
pick_num = total_people // 2
selected = [-1] * pick_num
power_a = 0
power_b = 0
power_a_lst = []
power_b_lst = []
comb(0, 0)













# 서로소집합 활용 (UNION - FIND)
