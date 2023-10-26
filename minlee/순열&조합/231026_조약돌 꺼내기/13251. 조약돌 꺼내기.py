M = int(input())
# 조약돌 색상
# stone_color의 길이
stone_color = list(map(int, input().split()))
# 각 색상별 조약돌 개수
all_stone = sum(stone_color)
K = int(input())
# 뽑아야되는 조약돌

# 조합 문제
# (K개 뽑았을 때 전부 같은 색일 경우의 수) / (전체 중 K개 뽑을 경우의 수) 구하기! => all_stone 중에서 K개 뽑기

# 분자 : 리스트 순회하면서 더한 거 넣기, 만약 수가 안맞으면 넘어가는 걸로!
jip_son = [0] * M
for i in range(M):
    son_num = 1
    find_son = stone_color[i]
    if find_son < K:
        continue
    for k in range(K):
        son_num *= find_son
        find_son -= 1
    jip_son[i] = son_num

# 분모 : all_stone에서 K개만큼 빼서 곱하기
mom_num = 1
check = K
for i in range(K):
    mom_num *= all_stone
    all_stone -= 1
answer = sum(jip_son)/mom_num

print(answer)
