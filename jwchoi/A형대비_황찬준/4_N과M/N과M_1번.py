# 1개씩만 뽑는 경우 에만 쓸수 있는 함수
# def combi_recur(cnt):
#     while cnt <N+1:
#         vi[cnt] =1
#         print(L[vi.index(1)])
#         vi[cnt] =0
#         cnt += 1
#     return

def combi_recur(cnt,idx):
    # 횟수가 다 찼고, 제대로 모두 뽑은 경우
    if cnt == N+1:
        return
    if cnt == idx:
    # cnt < N+1 (진행 도중의 상태)


N,M = map(int,input().split())
# print(N,M)
vi = [0]*(N+1)
# print(vi) # [0,0,0]
L=[]
for n in range(N+1):
    L.append(n)
# print(L) # [0,1,2,3]
# 구해야 할 것: L에서 M개의 숫자를 뽑는 조합을 한줄씩 반환하기
combi_recur(1)