def operations(sum_num, idx, add, sub, multi, div):
    global max_v, min_v
    if add < 0 or sub < 0 or multi < 0 or div < 0:
        return
    if not add and not sub and not multi and not div:
        min_v = min(min_v, sum_num)
        max_v = max(max_v, sum_num)
        return
    if idx >= N:
        return
    operations(sum_num + num_list[idx], idx+1, add-1, sub, multi, div)
    operations(sum_num - num_list[idx], idx+1, add, sub - 1, multi, div)
    operations(sum_num * num_list[idx], idx+1, add, sub, multi - 1, div)
    operations(sum_num // num_list[idx], idx+1, add, sub, multi, div - 1)



N = int(input())
# 숫자 개수
num_list = list(map(int, input().split()))
# 주어진 숫자
add, sub, multi, div = map(int, input().split())
# 더하기, 빼기, 곱하기, 나누기 각각 숫자 넣기

min_v = 10**10
max_v = -(10**10)
# 최댓값, 최솟값 설정

# 수를 하나씩 줄여가면서 계속 돌려보기
# 만약 전체가 다 0이 되면 끝내기!
operations(0, 0, add, sub, multi, div)
print(max_v)
print(min_v)