# 모든 경우의 수에 해당하는 조합을 다 만드는게 아니라
# 경우의 수 개수만 구하면 된다
# import sys
# input = sys.stdin.readline

tc = int(input())   # 테스트 케이스 수
for _ in range(tc):
    n = int(input())    # 해빈이가 가진 의상 수

    # 공집합을 제외한 경우의 수는 어떻게 구할까?

    cloth_dict = {}
    for i in range(n):
        a, b = input().split()
        # cloth_dict[b].append(a)
        if b in cloth_dict.keys():
            cloth_dict[b] += 1
        else:
            cloth_dict[b] = 1

    ans = 1
    for k in cloth_dict.keys():
        ans *= (cloth_dict[k] + 1)

    # 아무것도 안입는 경우의 수 빼주기
    print(ans-1)
