# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.
# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다.
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
from collections import deque
def lab(n,m,data):
    # 준비1: visited, deque 준비
    dq = deque()
    vi = [[-1]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if data[r][c]==0:
                vi[r][c]=0 # 벽을 세울수 있는곳에만 0으로 설정. (이후 방문시 1로 변경)
    # print(vi) [[0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, -1], [-1, -1, -1, 0, 0, -1], [0, 0, 0, 0, 0, -1]]
    # 준비2: 벽을 세우는 방식은 어떻게?
    for r in range(n):
        for c in range(m):
            if vi[r][c]==0:

N, M = map(int,input().split())
DATA = [list(map(int,input().split())) for _ in range(N)]
# print(data)
# 추론1: 꼭 2와 인접한 곳에 벽(1)3개를 안세워도 된다.
# 추론2: 벽의 갯수는 1,2,3... 다양할 수 있지만. 주어진 문제에선 3개 이다.
# 좀더 그리디 하게 풀수있는 방법은 없어보임. 완탐->가지치기 해야할듯
lab(N,M,DATA)