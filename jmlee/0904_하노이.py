def hanoi(N, start, end, sub):
    if N == 1:
        print(start, end)
        return

    hanoi(N-1, start, sub, end) # N-1 이동
    print(start, end)           # N 이동
    hanoi(N-1, sub, end, start) # N-1 이동
    

N = int(input())
print(2**N -1)
hanoi(N, 1, 3, 2)