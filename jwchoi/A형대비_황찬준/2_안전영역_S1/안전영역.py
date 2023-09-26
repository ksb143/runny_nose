# 어떻게 풀것인가?
# 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다.
# 위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면,
# 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.
from collections import deque

def bfs(n,data):
    # dr dc로 상하좌우 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 가야할곳의 좌표를 담는 빈덱 만들기
    dq = deque([])
    # visited 만들기.
    vi = [[0] * n for _ in range(n)]
    ans = []
    # 순회하기
    for k in range(1,101):
        for r in range(n):
            for c in range(n):
                if data[r][c] >= k: # 높이가 k 초과인 구역은 safe place이다
                    vi[r][c]=1
                else:
                    vi[r][c]=0 # 높이가 k 이하인 구역은 safe place가 아니다
        # print(k,vi)
        ########### 초기화 ##########
        vvi = [[0] * n for _ in range(n)]
        cnt = 0
        ########### 초기화 ##########
        for r in range(n):
            for c in range(n):
                # 만약 미방문 safe place를 발견 한다면?
                if vi[r][c]==1 and vvi[r][c]==0:
                    cnt +=1
                    dq.append((r,c))
                    vvi[r][c] = 1
                    while dq:
                        rr,cc = dq.popleft()
                        for d in range(4):
                            nr,nc = rr + dr[d], cc + dc[d]
                            if 0<= nr < n and 0<= nc <n and vi[nr][nc]==1 and vvi[nr][nc] == 0:
                                vvi[nr][nc] = 1
                                dq.append((nr,nc))
        ans.append(cnt)
    # print(ans)
    final = max(ans)
    return final
# 인풋받기
N = int(input())
DATA = [list(map(int,input().split()))for _ in range(N)]
print(bfs(N,DATA))