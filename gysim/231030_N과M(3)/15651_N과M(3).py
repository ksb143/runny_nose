# 자연수 N, M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열 모두 구하기
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다 -> 중복 가능

N, M = map(int, input().split())

selected = [0] * M      # 고른 숫자 넣어줄 배열


def comb(cnt):          # cnt : 고른 숫자의 개수
    if cnt == M:        # 숫자를 M개 뽑았으면
        print(*selected)    # 고른 숫자 출력
        return

    for i in range(1, N+1): # 1부터 N 까지 숫자 중에서
        selected[cnt] = i   # i를 고르기
        comb(cnt+1)         # 다음 숫자 뽑으러 가기


comb(0)
