# 유사한 느낌의 문제: 백준_유기농배추, 백준_미로탐색
# 유사한 개념: BFS(너비우선검색)-> 큐/덱 쓰기
from collections import deque
m,n = map(int,input().split())
data  = [list(map(int,input().split()))for _ in range(n)]
# 0: 토마토가 있고, 안 익었음./// 1: 토마토가 있고, 익었음. /// -1: 토마토가 아예 없음.
dir_idx = [[-1,0],[0,1],[1,0],[0,-1]]
ans = None      # 최종 반환을 위한 변수
cnt = 0         # 모든 칸을 도는 것을 표시해줄 용도의 변수
cnt_0 = 0       # 0의 갯수를 세는 변수
cnt_1 = 0       # 1의 갯수를 세는 변수
cnt__1= 0       # -1의 갯수를 세는 변수
vi = [[0]*m for _ in range(n)]
d = deque([])
# print(vi) # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for i in range(n):          # 행 4
    for j in range(m):      # 열 6
        cnt += 1            # 한칸에 도달할때마다 전체 cnt 1씩 올라감
        # 미방문 1을 찾아야함
        # 1 을 만난경우... 주변(상,우,하,좌)에 0 이 있는지 탐색해보자 => 있다면,
        if data[i][j] ==1 and vi[i][j]==0:
            vi[i][j] = 1            # (i,j)에서 1을 만난것을 vi에 표시해줌
            cnt_1 += 1              # cnt_1을 1 더함
            for k in range(4):
                # 주변으로 탐색시작
                ni = i + dir_idx[k][0]
                nj = j + dir_idx[k][1]
                if 0<= ni < n and 0<= nj < m:
                    # 미방문 0을 찾았다! => 그 0자리들을
                    if data[ni][nj] ==0 and vi[ni][nj] ==0:
                        # 익혔다=> 해당자리 data 값이 1로 변하면서, cnt_1이 하나 올라감
                        data[ni][nj] = 1
                        vi[ni][nj] = 1
                        cnt_1 += 1
        # -1 을 만난경우
        elif data[i][j] ==-1 and vi[i][j]==0:
            vi[i][j]=1
            cnt__1 += 1

if cnt == n*m and cnt == cnt_1 + cnt__1:
    print('cnt= cnt_0 + cnt__1 + cnt_1')
    print('cnt:',cnt)
    print('cnt_0:',cnt_0)
    print('cnt__1:',cnt__1)
    print('cnt_1:',cnt_1)
    print()
    ans = 0 # 모두 익어있었따면? 답 = 0

print(ans)