def solution(n, times):
    left, right = 1, max(times) * n  # 탐색 범위 설정
    answer = right  # 최대 시간으로 초기화

    while left <= right:
        mid = (left + right) // 2  # 중간값 계산
        # mid 시간 동안 심사할 수 있는 총 인원 수
        total = 0
        for time in times:
            total += mid // time

        if total >= n:  # 심사할 수 있는 인원 수가 n보다 크거나 같으면
            answer = mid  # 답을 갱신하고
            right = mid - 1  # 더 짧은 시간 탐색
        else:
            left = mid + 1  # 더 긴 시간 탐색

    return answer
