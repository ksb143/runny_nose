# 1부터 49 중 k개 수 고르기
# 집합 만들기
# 그 중에서 6개씩 뽑기
# 결국 답은 S에서 k개 뽑아서 조합으로 구성하는 거!

def johap(idx, lst, count):
    if count == 6:
        # 6개 다 담았으면 프린트
        print(*lst)
        return
    if idx >= k:
        # 인덱스가 주어진 집합보다 크면 안되니까
        # S의 길이인 k보다 작기!
        # 인덱스니까 k-1개라고 생각
        return

    johap(idx + 1, lst + [S[idx]], count + 1)
    johap(idx + 1, lst, count)
    # 조합은 순서대로 경우의 수 따져서 보면 되니까!

S = list(map(int, input().split()))
# 전체 주어진 것에서
k = S.pop(0)
# 첫째자리 빼주기
while k != 0:
    # 맨 마지막은 0이 나온다고 했으니까
    johap(0, [], 0)
    print()
    # 한 줄 띄우는 걸로 나왔으니까
    S = list(map(int, input().split()))
    k = S.pop(0)