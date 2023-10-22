# K개 중에서 중복 없고, 순서 상관없이 6개를 뽑는 조합 함수
# i는 인덱스, cnt는 뽑은 숫자의 개수
def comb(i, cnt):
    # 숫자를 6개 뽑았으면
    if cnt == 6:
        # 뽑은 숫자를 저장한 selected를 출력
        print(*selected)
        return

    # 배열 S 끝까지 갔는데 숫자를 다 못 뽑았으면
    if i == K:
        # 돌아가시오
        return

    # selected에 현재 인덱스 i에 해당하는 숫자를 넣어주기
    selected[cnt] = S[i]
    # i번째 값을 썼다고 표시
    visited[i] = 1
    # 숫자를 1개 뽑았고, i+1번째 숫자 고르러 가기
    comb(i + 1, cnt + 1)
    # i번째 값을 안 썼다고 표시
    visited[i] = 0
    # 숫자 1개 안뽑았고, i+1번째 숫자 고르러 가기
    comb(i + 1, cnt)


# 테스트 케이스 돌리기
while True:
    # 0번째 값은 K, 나머지는 조합할 숫자, S는 오름차순으로 주어진다
    S = list(map(int, input().split()))
    # K는 숫자 집합의 개수
    K = S.pop(0)

    # 만약 K가 0이면 테스트 케이스 종료
    if K == 0:
        break

    # 주어진 S 안의 숫자 K개 중에서 중복없이 6개를 고르는 조합
    # 수를 고르는 모든 방법을 사전 순으로 출력

    visited = [0] * K   # i번째 숫자를 사용했는지 표시할 배열
    selected = [0] * 6  # 뽑은 숫자를 저장할 배열

    # 조합 재귀 함수 실행
    comb(0, 0)

    # 각 테스트케이스 사이에는 빈줄 하나 출력
    print()


