def find_su(tem):
    if len(tem) == M:
        # M개를 뽑았으면
        print(*tem)
        # 언패킹해서 숫자만 뽑아주기
        return
    for i in range(1, N+1):
        # 범위 내에서
        if not visited[i]:
            # 방문하지 않으면
            visited[i] = 1
            # 방문했다고 하고
            find_su(tem+[nums[i]])
            # 리스트에 숫자추가해서 넣기
            visited[i] = 0
            # 함수 다 끝나고 나면 다음 숫자들도 써야하니까
            # (중복 있게 해야하니까!)
            # 비지티드 0 만들어주기!

# 1부터 N까지 자연수 중 중복있는 M개를 고른 수열
N, M = map(int, input().split())
# 숫자(주어진 범위의 자연수) 리스트
nums = [i for i in range(1, N+1)]
# 방문 기록
visited = [0] * (N+1)
# 생길 수 있는 순열마다 담아주기
tem = []
# 함수에는 리스트 담아주기
find_su(tem)