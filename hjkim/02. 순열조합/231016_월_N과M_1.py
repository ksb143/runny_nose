def perm(idx, cnt):

    if idx == N:
        print(chosen)
        return

    if cnt == pick_num:

        return

    for el in range(N):
        if not used[idx]:
            chosen[idx] = numbers[el]
            used[idx] = 1
            perm(idx + 1, cnt + 1)
            used[idx] = 0


N, pick_num = map(int, input().split())
numbers = [num for num in range(1, N + 1)]
used = [0] * N
chosen = [-1] * pick_num
perm(0, 0)