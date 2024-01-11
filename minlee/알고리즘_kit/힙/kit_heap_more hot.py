from heapq import heappush, heappop, heapify

def solution(scoville, K):
    scv = 0
    count = 0
    heapify(scoville)
    while scoville[0]<K:
        if len(scoville)==1:
            return -1
        scv = heappop(scoville) + heappop(scoville)*2
        heappush(scoville, scv)
        count += 1
    return count