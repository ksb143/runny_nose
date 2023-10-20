def perm(idx, cnt):

    # 이거 없으면 Index Out of Range
    # 원하는 갯수만큼 못 뽑았는데 Index 넘어가면 탐색을 종료하렴
    if idx == N:
        return

    # 원하는 갯수만큼 뽑았다면 탐색을 종료하렴
    if cnt == pick_num:
        print(chosen)
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