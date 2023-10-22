# 아래 조건을 만족하는 길이가 M인 수열을 모두 출력

# 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열
# 한 줄에 하나씩, 각 수열은 공백으로 구분
# 중복되는 수열은 여러 번 출력하면 안됨
# 사전 순으로 증가하는 순서로 출력


# 1부터 N까지의 자연수 중에서 중복없이 M개를 골라야함
N, M = map(int, input().split())

visited = [0] * (N+1)   # 방문표시할 배열, 1부터 N까지라서 N+1개 만들기
selected = [0] * M      # M개의 고른 숫자를 넣어줄 배열

# 재귀로 구현, cnt는 고른 숫자의 개수
def comb(N, M, visited, cnt):
    # M개를 골랐으면
    if cnt == M:
        # selected[i]에 있는 값을 출력
        for i in range(M):
            print(selected[i], end=' ')
        print()
        return

    # 1부터 N까지 순회
    for i in range(1, N+1):
        # 방문안했으면
        if not visited[i]:
            selected[cnt] = i   # i를 골라서 selected에 넣어주고
            visited[i] = 1      # 방문표시
            comb(N, M, visited, cnt+1)  # 재귀로 다음숫자 찾으러감
            visited[i] = 0      # 재귀 돌아오면 방문표시 해제

# 함수 실행, cnt 초기값은 0
comb(N, M, visited, 0)
