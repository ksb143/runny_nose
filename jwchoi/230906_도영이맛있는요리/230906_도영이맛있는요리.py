# setting1 : 부분집합을 만들어줄 함수
def gen_powerset(data,N):
    result_l =[]
    for i in range(1<<N): # 2진수로 나타낸 모든 경우의 수
        chosen = []
        for j in range(N): # 고를 원소의 갯수
            if i&(1<<j):
                chosen.append(data[j]) # 해당하는 경우만
        # print(i, chosen)
        if chosen:
            chosen_l = len(chosen)
            if chosen_l == 1:
                result = abs(chosen[0][0]-chosen[0][1])
                result_l.append(result)
                # print(chosen,result)
            else:
                S=1
                B=0
                for k in range(chosen_l):
                    S *= chosen[k][0]
                    B += chosen[k][1]
                result = abs(S-B)
                result_l.append(result)
                # print(chosen,result)

    return min(result_l)

# input ###############
N = int(input()) # items의 원소갯수
items = [] # 각 [S,B]를 담을 빈 리스트
for _ in range(N):
    item = list(map(int,input().split()))
    items.append(item)
# input ###############
print(gen_powerset(items,N))
