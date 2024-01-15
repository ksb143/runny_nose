from collections import deque

def solution(arr):
    # append 작업이 많으므로 deque를 사용
    ans = deque()
    # 첫 번째 수는 중복이 아니므로 삽입
    ans.append(arr.pop(0))
    for num in arr:
        # 만약 삽입할 글자와 직전 글자가 동일하면 넘어가기
        if ans[-1] == num:
            continue
        # 다르다면 ans에 삽입
        ans.append(num)
    # deque 리스트화 시키기
    answer = list(ans)
    return answer