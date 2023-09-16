result=0
def dfs(i,n,result): # i는 시작 인덱스 , n은 dfs에서 탐색한 도시 갯수, result는 탐색한 곳들의 합계
    global minminus   #최솟값 글로벌 변수로 받기
    if n==N:   # 탐색한 도시 갯수가 전체 도시 갯수랑 같을때
        chaE=abs(result-(sum(people)-result)) # 두 지역구의 차이값 절대값으로 계산
        if chaE<minminus: # 계산한 것이 최소값보다 작을떄
            minminus=chaE #최소값 재 설정

    for a in range(N): # dfs2호기 계속 돌리기
        if adj[i][a] and not visited[a]: # 탐색안한곳 길이 있으면
            visited[a]=1 # 비지티드 찍고
            dfs(a,n+1,result+people[a]) # 2호기 계속돌리기
            dfs(i,n+1,result+people[a]) # 시작점을 2개로 해서 돌리기
                                        # 두개로 돌리는 이유 중간지점과 연결됐지만 마지막 도착 지점이랑은 연결안된 곳도
                                        #보게하기 위해서서
            #백준 게리맨더링 예를 들면 1-2-3-4 순으로 탐색하면 2에서 5랑 6도 연결되있는데 4에서 못가니까 그 부분 보완
            visited[a]=0 #다시 재귀 돌아오면서 원상복구
    # 이렇게 dfs2호기 다돌면 다시 밑의 1호기 함수로

def dfs1(i,n,result):
    for a in range(N): # dfs1호기가 1단계씩 돌아갈 떄마다 새로운 dfs2호기 돌려서 1호기가 간 곳 말고 나머지 다 탐색하기
        if adj[i][a] and not visited[a]: #아직 탐색안한곳이 잇을떄
            visited[a]=1      # dfs 2호기가 갈곳 비지티드 찍기
            dfs(a, n, result) # dfs 2호기 가동  -> 맨위의 함수 주석으로
            dfs1(a,n+1,result) # 여기도 똑같이 DFS 1호기를 갈 수 있는 모든 경우로 보내기
            dfs1(i,n+1,result)
            visited[a]=0 #갔다와서 원상복구
    # 즉 1호기가 한칸씩 갈때마다 2호기를 나머지 다 돌게해서 그 두개의 차이를 구해 최소값을 구하는 방식




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]
    people = list(map(int, input().split()))
    visited = [0] * N
    minminus = 215252525252 # 최소 차이값(2지역구) 초기 설정
    for i in range(N): #(지역구 하나씩 다 시작해보기(모든 경우의 수 다보기))
        visited[i]=1   # 시작할 지역구 비지티드 먼저찍고
        dfs1(i,1,result) # dfs1호기 돌리기
        visited[i]=0 # 다돌고오면 다시 비지티드 초기화
    print(f'#{tc} {minminus}') # 위 함수에서 구한 제일 최소값