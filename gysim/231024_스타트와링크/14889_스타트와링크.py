from collections import deque


# 중복 없고 순서 없는 조합, i는 인덱스, cnt는 뽑은 숫자의 개수
def comb(i, cnt):
    # 최소값 변수를 글로벌로 설정
    global min_v
    # start 팀을 N//2만큼 뽑았으면
    if cnt == (N//2):
        # link 팀 배열 초기화
        links = deque()
        # N만큼 순회하면서
        for i in range(N):
            # i번째 사람이 start 팀에 속하지 않았으면
            if i not in starts:
                # link 팀에 넣기
                links.append(i)

        startv = 0  # start 팀 능력치 초기화
        linkv = 0   # link 팀 능력치 초기화
        # 팀 별 능력치 계산
        # start 팀 안의 한 사람 당
        for i in starts:
            # start 팀 안의 모든 사람 비교
            for j in starts:
                # start 팀 능력치 더해주기
                startv += S[i][j]

        # link 팀 안의 한 사람 당
        for i in links:
            # link 팀 안의 모든 사람 비교
            for j in links:
                # link 팀 능력치 더해주기
                linkv += S[i][j]

        # start 팀 능력치와 link 팀 능력치 차이의 절대값 구하기
        tmp = abs(startv - linkv)
        # 현재 능력치 차이와 최소값 비교하기
        min_v = min(tmp, min_v)
        return
    
    # 배열의 끝까지 갔는데 다 못 뽑았으면
    if i == N:
        # 돌아가기
        return
    
    # i번째 사람을 start 팀에 넣어주기
    starts[cnt] = i
    # i번째 사람 뽑고 다음 사람 찾으러 가기
    comb(i+1, cnt+1)
    # i번째 사람 안 뽑고 다음 사람 찾으러 가기
    comb(i+1, cnt)


# 사람은 총 N 명이고 N은 반드시 짝수
# 사람 번호를 1부터 N 까지로 배정 -> 이 문제는 인덱스 0부터 써도 상관없음
N = int(input())

# 능력치 Sij 는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
# Sij 는 Sji 는 다를 수 있으며, 같은 팀에 속했을 때 더해지는 능력치는 Sij 와 Sji 이다.
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij 의 합이다.
S = [list(map(int, input().split())) for _ in range(N)]

# N/2 명으로 이루어진 스타팀과 링크 팀으로 나눠야 한다.
starts = [0] * (N//2)
# 최소값 초기값 설정
min_v = 0xffffff
# 함수 실행
comb(0, 0)

# 능력치 차이의 최소값 출력
print(min_v)
