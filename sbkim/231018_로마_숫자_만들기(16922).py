import sys
sys.setrecursionlimit(10**6)

def comb(cnt, start, N):
    # cnt가 N개 이면!
    if cnt == N:
        # 중복방지를 위해 세트로 구성
        num_lst.add(sum(check))
        return
    for i in range(start, 4):
        check[cnt] = roman_num[i]
        # 재귀 돌 때 start를 바꿔서 중복을 없앰
        comb(cnt+1, i, N)


roman_num = [1, 5, 10, 50]
N = int(input())
check = [0] * N
num_lst = set()

comb(0, 0, N)


print(len(num_lst))