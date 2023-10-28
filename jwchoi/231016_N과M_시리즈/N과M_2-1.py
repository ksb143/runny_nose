def comb(start, cnt):

    if cnt == pick_num:

        if sorted(chosen) not in result:

            result.append(sorted(chosen))
            return

        return

    if start == total_num + 1:
        return

    for num in range(start, total_num):

        if not visited[num]:
            chosen[start] = numbers[num]
            visited[num] = 1
            comb (start + 1, cnt + 1)
            visited[num] = 0

total_num, pick_num = map(int, input().split())

numbers = [num for num in range(1, total_num + 1)]

chosen = [-1] * pick_num

visited = [0] * total_num

result = []
comb(0, 0)

r = len(result)
for el in range(r):
    print(*result[el])