# 최지의 1번째 풀이: 정확성 2개? 성공 and 효율성 통과 실패
def solution(scoville, K):
    ans = 0
    lsc = len(scoville)
    while True:
        if sum(scoville) > K*lsc:
            False
            break
        else:
            min0 = min(scoville)
            scoville.remove(min0)
            min1 = min(scoville)
            scoville.remove(min1)
            
            new = (min0 + min1*2)
            scoville.append(new)
            # print(sc)
            ans +=1
    return ans

# 최지의 2번째 풀이: chat GPT 의 도움을 받았읍니다.
# heapq를 써야하는 듯!
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # scoville 리스트를 최소 힙으로 변환
    ans = 0

    while scoville[0] < K:  # 힙의 첫 번째 요소(최솟값)가 K보다 작은 동안 반복
        if len(scoville) < 2:  # 더 이상 섞을 수 없는 경우
            return -1

        min1 = heapq.heappop(scoville)  # 최소 요소 추출
        min2 = heapq.heappop(scoville)  # 다음 최소 요소 추출

        new_scoville = min1 + min2 * 2
        heapq.heappush(scoville, new_scoville)  # 새로운 요소를 힙에 추가
        ans += 1

    return ans

# 테스트
scoville0 = [1, 2, 3, 9, 10, 12]
K0 = 7
print(solution(scoville0, K0))
