# 가로 세로 중에 가장 긴 길이를 비교
# 정렬하고 긴것부터 비교
# 두개 다 만족하지 않으면 갱신


def solution(sizes):
    long, short = 1, 1

    for size in sizes:
        # 크기순으로 정렬
        size.sort()
        if size[1] >= long:
            long = size[1]

        if size[0] >= short:
            short = size[0]

    return long * short


# pythonic 하게 푼 코드
def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


# pythonic 하게 푼 코드2
solution3 = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)


# 이해하기 편한 코드
def solution4(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col
