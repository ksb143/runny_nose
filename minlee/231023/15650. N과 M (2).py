def johap(idx, answer):
    if len(answer) == M:
        # 원하는 개수만큼 다 뽑았으면
        print(*answer)
        # 언패킹해서 프린트하기
        return
    if idx >= N:
        # idx의 길이가 주어진 숫자보다 크면
        return
        # 함수 끝내기
    johap(idx+1, answer + [nums[idx]])
    # 인덱스 계속 올라가고 리스트에 담아주기
    johap(idx+1, answer)
    # 이건 이 인덱스일때 안뽑은 경우 처리하기


N, M = map(int, input().split())
# 1부터 N까지/ 중복 없이 M개(예시보니까 조합임)
# 오름차순으로 뽑기
nums = [i for i in range(1, N+1)]
answer = []
# 조합 뽑은 것들 담아두는 거
johap(0, answer)