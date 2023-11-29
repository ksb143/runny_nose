def solve(data):
    if data == '':
        return 1
    M = len(data)
    cnt = 0
    for idx in range(M):
        if data[idx] == '[':
            cnt += 2
    return cnt


T = int(input())
for tc in range(1, T+1):
    data = input()
    answer = solve(data)
    print(answer)