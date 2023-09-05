N = int(input())


def hanoi1(N, s, e, t):  # N: 원판개수, s:출발기둥, t:중간기둥, e:도착기둥
    if N == 1:
        print(s, e)
        return
    
    hanoi1(N-1, s, t, e)
    print(s, e)
    hanoi1(N-1, t, e, s)


def hanoi2(N, s, t, e):  # N: 원판개수, s:출발기둥, t:중간기둥, e:도착기둥
    if N == 1:
        print(s, e)
        return
    
    hanoi2(N-1, s, e, t)
    print(s, e)
    hanoi2(N-1, t, s, e)


print(2*N+1)
# hanoi1(N, 1, 2, 3)
hanoi2(N, 1, 2, 3)

# 첫째 줄에 옮긴 횟수 K 출력
# 두번째 줄부터 수행 과정 출력
# K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력
# 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻
