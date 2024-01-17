힙(Heap) 더 맵게

정확성 -- 4개 틀림
테케1
테케3
테케8
테케14

```python
import heapq

def solution(scoville, K):
    # answer = 섞어야 하는 최소 횟수
    answer = 0
    # scoville 을 힙으로 만들기
    heapq.heapify(scoville)
    # 가장 작은 수가 K 이상이 될 때까지 반복하기
    while True:
        if scoville[0] >= K:
            return answer
        # 1단계:제일 작은 수 제거
        least = heapq.heappop(scoville)
        # 2단계:두번째로 작은 수 제거
        less = heapq.heappop(scoville)
        # 3단계:두 음식을 섞은 수 추가
        heapq.heappush(scoville, least + (less * 2))
        # 4단계:섞은 횟수 더해주기
        answer += 1
```

통과코드

```python
import heapq

def solution(scoville, K):
    # answer = 섞어야 하는 최소 횟수
    answer = 0
    # scoville 을 힙으로 만들기
    heapq.heapify(scoville)
    # print(f'scv:{scoville}')
    # 가장 작은 수가 K 이상이 될 때까지 반복하기
    while True:
        if scoville[0] >= K:
            # print(answer)
            return answer
        # 만약 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        # 1단계:제일 작은 수 제거
        least = heapq.heappop(scoville)
        # print(f'least:{least},scv:{scoville}')
        # 2단계:두번째로 작은 수 제거
        less = heapq.heappop(scoville)
        # print(f'less:{less},scv:{scoville}')
        # 3단계:두 음식을 섞은 수 추가
        heapq.heappush(scoville, least + (less * 2))
        # print(f'scv:{scoville}')
        # 4단계:섞은 횟수 더해주기
        answer += 1
        # print(f'answer:{answer}')
```

틀린 이유 : 문제 조건 빼먹음
만약 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우 -1 을 리턴해야 함.
ㄴ 이럴 수 있는 경우를 생각해봄.
ㄴ 이럴 수 있는 경우는 scoville 의 길이가 1 이면서
ㄴ scoville 원소가 K 보다 작은 경우임
ㄴ 즉 한 개 남았는데 그게 K 보다 작은 경우임
ㄴ 그럴 때는 -1 를 리턴하도록 코드를 수정함

정확성 83.9
효율성 16.1
합계 100.0/100.0
