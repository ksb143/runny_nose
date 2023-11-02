def find_mini_dist(find_chicken):
    answer = 0
    for hr, hc in house:
        mini_dist = 10**10
        for cr, cc in find_chicken:
            now_dist = abs(hr-cr)+abs(hc-cc)
            mini_dist = min(mini_dist, now_dist)
        answer += mini_dist
        # 각 집마다 최소값 더해주기!
    return answer

def DFS(idx, find_chicken):
    if how_many_chicken == idx:
        return
    if len(find_chicken) == M:
        final_answer.append(find_mini_dist(find_chicken))
        return
    DFS(idx+1, find_chicken+[chicken[idx]])
    DFS(idx+1, find_chicken)

# 1. 집들과 치킨집 좌표 구하기
# 2. 치킨집 여러 개 중 하나씩 골라서 전부 비교해보기
# 3. 치킨집 골랐으면 그 곳과 집들간의 최소거리 구하기
# ★ 어느 치킨집을 선택했을지는 중요하지 않다!!
#    결국 내가 구하고자하는 건 가장 작은 값의 도시의 치킨거리다!!!

N, M = map(int, input().split())
city = [list(map(int,input().split())) for _ in range(N)]
# 크기가 N*N인 도시이다!
# 1이면 집, 2면 치킨집
# 1<= 집의 개수 <= 2N, M <= 치킨집 <= 13
# 집 리스트랑 치킨집 리스트 따로 넣어놓기(좌표)
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1: # 집이면
            house.append((i, j)) # 집 목록에 넣기
        if city[i][j] == 2: # 치킨집이면
            chicken.append((i, j)) # 치킨집 목록에 넣기

final_answer = []
# 이제 치킨집과 집 거리 비교해주기!
# 3.---------------------------------------------------------------------------
# 치킨집 목록 추리는 게 아니라..
# 다 돌아보기..?
# 이건 dfs로 다 찾아보기
how_many_chicken = len(chicken)
DFS(0, [])
print(min(final_answer))

# 2.--------------------------------------------------------------------------------------------
# 그 다음으로는 모든 집이랑 모든 치킨집이랑 비교하려고 했는데, 그렇게 하면 답이 안나옴
# 근데 치킨집 고른 후 비교해주는 게 맞는 거 같다!
# answer = 0
# for hr, hc in house:
#     for cr, cc in chicken:
#         now_dist = abs(hr-cr)+abs(hc-cc)
#         mini_dist = min(mini_dist, now_dist)
#         # 거리 비교(문제에서 보니까 집을 기준으로 각 치킨집들과의 거리를 비교해준 것 같았음)
#     answer += mini_dist
#     # 각 집마다 최소값 더해주기!

# 1. --------------------------------------------------------------------------------------
# 처음에는 치킨집마다 각 집과의 거리 구해서 제일 적게 나오는 치킨집을 뽑으려고 했는데..
# answer = []
# for cr, cc in chicken:
#     sum_dist = 0
#     for hr, hc in house:
#         now_dist = abs(hr-cr)+abs(hc-cc)
#         sum_dist += now_dist
#     answer.append((sum_dist, cr, cc))
# 이렇게 해버리면 하나를 기준으로 할 때는 괜찮은데,
# 2개 이상이면 각 주변에 가까운 치킨집이 있는 걸 고려하지 못하고
# 그냥 냅다 전체 집과의 거리를 비교하게 되어서 틀리게 된다.