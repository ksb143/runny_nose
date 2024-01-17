def solution(sizes):
    answer = 0
    w, h = [], []
    # [가로, 세로] 의 크기 비교해서 따로 모아주기
    for size in sizes:
        w.append(max(size))  # 큰 값은 가로 w 에 추가
        h.append(min(size))  # 작은 값은 세로 h 에 추가
    # 가로 중 가장 큰 값 * 세로 중 가장 큰 값 = answer
    answer = max(w) * max(h)
    return answer