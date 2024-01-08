# 증복 순열

N, M = map(int, input().split())

# 순열을 넣을 리스트
check = [0] * M

def perm(idx, N, M, check):
    # M개 뽑았으면... 리턴
    if idx == M:
        print(*check)
        return
    # N번 까지 순열에 넣기 위해 반복문 돌기
    # 1번부터 N번까지이므로 범위는 1이상 N+1 미만으로 설정
    for i in range(1, N+1):
        check[idx] = i
        perm(idx+1, N, M, check)


perm(0, N, M, check)
