N = int(input())


def hanoi(N, s, t, e):  # N: 원판개수, s:출발기둥, t:중간기둥, e:도착기둥
    if N == 1:
        print(s, e) # 원판이 하나 있을 때는 출발기둥에서 도착기둥으로 옮기기
        return
    else:
        hanoi(N-1, s, e, t) # N-1번째 원판을 출발기둥에서 중간기둥으로 옮기기
        print(s, e)         # N번째 원판을 출발기둥에서 도착기둥으로 옮기기
        hanoi(N-1, t, s, e) # N-1번째 원판을 중간기둥에서 도착기둥으로 옮기기


print(2**N-1)
hanoi(N, 1, 2, 3)
