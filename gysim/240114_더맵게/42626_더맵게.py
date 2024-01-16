from heapq import heapify, heappop, heappush


def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        new_scv = heappop(scoville) + heappop(scoville) * 2
        heappush(scoville, new_scv)
        answer += 1

    if scoville[0] >= K:
        return answer

    return -1