# 조합 생성하기
# 유사문제: 백준-다리건설
# N 개의 수 중에서 K 개의 수를 뽑아서 (조합한다.)
# type1 - for 을 K개 만큼 사용하기
ls = [1, 2, 3, 4, 5]
lslen = len(ls)
def combi1(N):
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N-0):
                print(ls[i], ls[j], ls[k])

combi1(lslen)
# print()

# type2 - recursion 방법 사용하기.
# 재귀를 사용하면, 재귀의 depth 를 k로 제어하여 구현.
# level : 몇번째 선택을 하는가?
N,K = map(int,input().split()) # 4, 2
arr = [0]*K # [0, 0, 0, 0]
A = [n for n in range(1,1+N)] # [1, 2, 3, 4]
# print(A)
def combi2(level,cnt):
    # 종료조건
    if level == K:
        print(*arr)
        return
    # 진행조건
    for i in range(cnt, N-K+level+1):
        arr[level] = A[i]
        combi2(level+1, i)

combi2(0,0)