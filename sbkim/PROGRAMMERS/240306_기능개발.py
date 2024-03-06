def solution(progresses, speeds):
    answer = []
    # 진행도가 있을 경우 동안 계속 진행
    while progresses:
        count = len(progresses)
        # 진행도 올리기
        for i in range(count):
            progresses[i] += speeds[i]
        # 제일 첫 기능이 100% 이상일 때
        if progresses[0] >= 100:
            completion = 0
            # 100%가 아니면 반복문 중단
            while progresses and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                completion += 1
            answer.append(completion)
    return answer
