# 자연수 N, M이 주어짐
# 중복된 수 고를 수 있음
# 사전 순으로 증가하는 순서로 출력하기

def permutation(lst):
    if len(lst) == M:
        print(*lst)
        # 조건만큼 리스트에 담기면 프린트하기
        return
    for i in range(1, N+1):
        permutation(lst+[num_list[i]])
        # 순서대로 뽑으면 되니까 리스트에 있는 거 다 담아주기

N, M = map(int, input().split())
# 1부터 N까지 자연수 중 M개 고르기
num_list = [i for i in range(N+1)]
# 사용하는 수 리스트(1~N만 사용할 예정)
permutation([])