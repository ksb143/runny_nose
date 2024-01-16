from heapq import heapify

def solution(scoville, K):
    heapify(scoville)
    answer = 0

    # 모든 음식의 스코빌 지수를 K 이상으로 만들기기
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    # 모든 음식의 스코빌 지수가 K 이상 될 때까지 섞기
    while scoville[answer] > K: # 1. = 을 붙여야 하나?
        pass

    return answer

scoville = [3, 2, 1, 9, 12, 10]
solution(scoville, 7)