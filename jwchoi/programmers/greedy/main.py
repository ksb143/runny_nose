
def solution(n, lost, reserve):
    zero_d = {key: 0 for key in range(1, n+1)}
    # print(zero_d)
    # 옷이 훔쳐진 사람들은 -1 된다.

    for l in lost:
        zero_d[l] -= 1
    # print(zero_d)

    for r in reserve:
        zero_d[r] += 2
    print(zero_d)
    # print(sum(zero_d.values()))

    for a in range(1,n+1):
        if zero_d[a-1] == 2 and zero_d[a] == -1:
            zero_d[a] += 1

    print(zero_d)

    return

n0, lost0, reserve0 = 5,[2, 4],[1, 3, 5]

print(solution(n0,lost0,reserve0))