# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해
# Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

# 실패 -> 시간 초과
def solution(scovilles, K):
    # 만들 수 없는 경우
    cnt = 0
    while len(scovilles) >= 2:
        # 스코빌 지수 정렬
        scovilles.sort()

        # 맵지 않은 음식 꺼내기
        min_scov1 = scovilles.pop(0)

        # 가장 맵지 않은 음식이 스코빌 지수 K 이상일 때
        if min_scov1 >= K:
            break
        # 모든 음식이 스코빌 지수 K를 넘은 경우
        else:
            # 두 번째로 맵지 않은 음식 꺼내기
            min_scov2 = scovilles.pop(0)
            # 스코빌 지수 UP
            new_scov = min_scov1 + (min_scov2 * 2)
            scovilles.append(new_scov)
            # 섞은 횟수 증가
            cnt += 1
    # 스코빌 지수를 K 이상으로 만들 수 없는 경우 (음식 하나만 남음)
    else:
        last = scovilles[0]
        if last < K:
            cnt = -1
    return cnt


# heaq 모듈 사용
import heapq

def solution(scovilles, K):
    # 힙구조로 바꿈
    heapq.heapify(scovilles)
    # 바꾸는 횟수 세는 변수
    cnt = 0
    # 스코빌 지수 높일 수 있으려면 최소 2이상의 음식이 있어야 함
    while len(scovilles) >= 2:
        # 맵지 않은 음식 꺼내기
        min_scov1 = heapq.heappop(scovilles)

        # 가장 맵지 않은 음식 스코빌 지수 K 이상일 때
        if min_scov1 >= K:
            break
        else:
            # 두 번재로 맵지 않은 음식 꺼내기
            min_scov2 = heapq.heappop(scovilles)
            # 스코빌 지수 UP
            new_scov = min_scov1 + (min_scov2 * 2)
            heapq.heappush(scovilles, new_scov)
            # 섞었으니 횟수 상승
            cnt += 1
    # 음식이 한 개 남아서 스코빌 지수 더 높일 수 없을 때
    else:
        last = heapq.heappop(scovilles)
        # 한 개 남은 음식이 원하는 스코빌 지수보다 작을 때
        # 이걸 고려 못해서 16, 22, 23이 틀림
        if last < K:
            cnt = -1
    return cnt

# 16, 22, 23의 반례
print(solution([2, 3], 7))