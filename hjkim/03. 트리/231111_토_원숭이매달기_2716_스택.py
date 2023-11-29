def solve(data):
    stack = []
    M = len(data)
    cnt = 0
    if M == 0:
        cnt = 1
        return cnt
    for idx in range(M):
        if data[idx] == '[':
            stack.append(data[idx])
        elif data[idx] == ']':
            stack.pop()
            cnt += 2
    return cnt


T = int(input())
for tc in range(1, T+1):
    data = input()
    answer = solve(data)
    print(answer)