# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열 모두 구하기
# 1 부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다


def comb(idx, pick_num):
    if idx == pick_num:
        print(*selected)
        return

    for num in numbers:
        selected[idx] = num
        comb(idx + 1, pick_num)


N, M = map(int, input().split())
numbers = [i for i in range(1, N + 1)]
selected = [0] * M


comb(0, M)
