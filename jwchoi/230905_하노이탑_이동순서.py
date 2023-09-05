def hanoi(N,from1,mid1,to1):
    if N ==1:
        print(from1,to1)
        return
    else:
        hanoi(N-1,from1,to1,mid1)
        print(from1,to1)
        hanoi(N-1,mid1,from1,to1)


N = int(input())
from2 = 1
mid2 = 2
to2 = 3

print(2**N-1)
hanoi(N,from2,mid2,to2)
