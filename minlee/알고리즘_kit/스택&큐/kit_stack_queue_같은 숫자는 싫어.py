from collections import deque
# 연속되는 숫자만 넣지 않는다!
def solution(arr):
    answer = deque()
    for i in arr:
        if not answer or i != answer[-1]:
            answer.append(i)
    return list(answer)

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))