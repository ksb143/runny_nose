def hanoi(N, start, end, sub):
    if N == 1:
        print(start, end)
        return
    # N-1개 원판을 보조 막대로 옮기기
    hanoi(N-1, start, sub, end)
    # 마지막 원판을 시작 막대에서 목표 막대로 옮기기
    print(start, end)
    # N-1개 남은 원판을 보조 막대에서 목표 막대로 옮기기
    hanoi(N-1, sub, end, start)
    

N = int(input())
print(2**N -1)
hanoi(N, 1, 3, 2)