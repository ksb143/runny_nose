# 최지의 1번째 풀이: 정확성 통과 성공 but 효율성 통과 실패
from collections import deque

def solution(arr):
    ans = []
    # arr의 인덱스를 뽑아내서 i번째, i+1번째를 비교하면 될 일인듯
    d = deque(arr)
    len_d = len(d)
    for i in range(len_d-1):
        if (d[i] != d[i+1]):
            ans.append(d[i])
            
    ans.append(d[-1])
    return ans

# 최지의 2번째 풀이: chat GPT의 도움을 받았읍니다.
# enumerate(array) 메소드를 이용해서 시간과 메모리를 줄였습니다.
def solution(arr):
    ans = []

    for i, value in enumerate(arr):
        if i == len(arr) - 1 or value != arr[i + 1]:
            ans.append(value)

    return ans
