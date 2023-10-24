# 조합 : 전체에서 주어진 개수만큼 선택
# 각 요소가 조합에 포함되는지 아닌지 결정하는 것은 동일
# 포함되는 요소의 개수가 정해져 있는것이 다르다..
# cnt : 여태까지 몇개의 요소가 선택되었는지 알려주는 변수
def comb(idx, cnt):

    # 내가 필요한 만큼 다 골랐다
    if cnt == M:
        #여기가 성공케이스
        for el in range(4):

        return

    # 모든 요소에 대해서 조합 포함여부 결정
    # 여기는 마지막 인덱스 까지 결정했는데..
    # 필요한 개수만큼 선택하지 못함
    if idx == N:
        return

    # idx 번째 요소 고르기
    selected[idx] = 1
    comb(idx+1, cnt + 1)
    # idx 번째 요소 안 고르기
    selected[idx] = 0
    comb(idx+1, cnt)

# 전체 사람 수
N = int(input())
people = [i for i in range(1, N + 1)]
# 한 팀 당 사람 수
M = N // 2
#각 요소 포함여부 표시배열
selected = [0] * N
groups = []
g1 = []
g2 = []

# idx : people 내부 도는 idx
# cnt : 선택된 요소의 개수
# comb(idx,cnt)
comb(0, 0)